# A reference implementation of a "Python launcher", as described
# in XXXX
#
# Note that as this launcher is Windows specific and the actual 
# implementation will be in C, this reference is written in the
# style of C rather than attempting to be truly Pythonic.  In that
# vein:
# * win32 api functions are used even where a Python module
#   could offer similar functionality.
# * we work with a command-line rather than an argv array primarily
#   to avoid "requoting" arguments when building the command-line of
#   the child process and where possible, we directly pass the tail of
#   our command-line directly to the child.
# * We avoid dictionaries etc in preference to arrays so the C implementation
#   can directly port the logic without needing a complex implementation.

# TODO (and to be specified!)
# * 64 vs 32 bit considerations

import sys
import os
import re
import winreg

# Use pywin32 for all the process creation functioality.
from win32process import STARTUPINFO
from win32api import (GetCommandLine, DuplicateHandle, GetCurrentProcess,
                      GetStdHandle, GetLastError, MessageBox,
                      STD_INPUT_HANDLE, STD_OUTPUT_HANDLE, STD_ERROR_HANDLE)
from win32api import error as win32api_error
from win32process import GetExitCodeProcess, CreateProcess, STARTF_USESTDHANDLES
from win32event import WaitForSingleObject, INFINITE
from win32con import DUPLICATE_SAME_ACCESS
from winerror import ERROR_INVALID_HANDLE


# Special process return codes for when we can't do the right thing...
RC_NO_STD_HANDLES = 100
RC_CREATE_PROCESS = 101
RC_BAD_VIRTUAL_PATH = 102
RC_NO_PYTHON  = 103


# Picture IS_W as a C #define - a compile-time constant.  But for
# this reference implementation, we determine it at runtime based on
# whether we are running python or pythonw.
IS_W = sys.executable.endswith("w.exe")


VIRT_PATHS = [
    "/usr/bin/",
    "/usr/bin/env ",
]


class VirtualPath: # think a C struct...
    def __init__(self, version, bits, executable):
        self.version = version
        self.bits = bits
        self.executable = executable


def debug(msg):
    #print("DEBUG:", msg, file=sys.stderr)
    pass


def error(msg, rc):
    winerr = GetLastError()
    if winerr:
        msg += "\n" + "Windows error code is %d" % (GetLastError(),)
    if IS_W:
        MessageBox(0, msg, "Python Launcher")
    else:
        print(msg, file=sys.stderr)
    sys.exit(rc)

# Locate all installed Python versions, reverse-sorted by their version
# number - the sorting allows a simplistic linear scan to find the higest
# matching version number.
def locate_all_pythons():
    infos = []
    executable = "pythonw.exe" if IS_W else "python.exe"
    python_path = r"SOFTWARE\Python\PythonCore"
    for root in (winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER):
        core_root = winreg.OpenKey(root, python_path)
        try:
            i = 0
            while True:
                try:
                    verspec = winreg.EnumKey(core_root, i)
                except WindowsError:
                    break
                try:
                    ip_path = python_path + "\\" + verspec + "\\" + "InstallPath"
                    key_installed_path = winreg.OpenKey(root, ip_path)
                    try:
                        install_path, typ = winreg.QueryValueEx(key_installed_path,
                                                                None)
                    finally:
                        winreg.CloseKey(key_installed_path)
                    if typ==winreg.REG_SZ:
                        for check in ["", "pcbuild", "pcbuild/amd64"]:
                            maybe = os.path.join(install_path, check, executable)
                            if os.path.isfile(maybe):
                                if " " in maybe:
                                    maybe = '"' + maybe + '"'
                                infos.append(VirtualPath(verspec, 32, maybe))
                                debug("found version %s at '%s'" % (verspec, maybe))
                                break
                except WindowsError:
                    pass
                i += 1
        finally:
            winreg.CloseKey(core_root)
    return sorted(infos, reverse=True, key=lambda info: info.version)


# locate a specific python version - some version must be specified (although
# it may be just a major version)
def locate_python_ver(spec, all):
    assert spec
    for info in all:
        if info.version.startswith(spec):
            return info.executable
    return None


def locate_python(spec):
    all = locate_all_pythons()
    if len(spec)==1:
        # just a major version was specified - see if the environment
        # has a default for that version.
        spec = os.environ.get("PY_DEFAULT_PYTHON"+spec, spec)
    if spec:
        return locate_python_ver(spec, all)
    # No python spec - see if the environment has a default.
    spec = os.environ.get("PY_DEFAULT_PYTHON")
    if spec:
        return locate_python_ver(spec, all)
    # hrmph - still no spec - prefer python 2 if installed.
    ret = locate_python_ver("2", all)
    if ret is None:
        ret = locate_python_ver("3", all)
    # may still be none, but we are out of search options.
    return ret


# *** Process creation ***
# Duplicate a handle.  Return True if successful or id the source
# handle is a "known invalid" handle.
def safe_duplicate_handle(h):
    try:
        h = DuplicateHandle(GetCurrentProcess(),
                            h,
                            GetCurrentProcess(),
                            0, # create flags
                            True, # inheritable
                            DUPLICATE_SAME_ACCESS)
        return True, h
    except win32api_error as exc:
        if exc.winerror == ERROR_INVALID_HANDLE:
            return True, None
    return False, None


# spawn a child process.  Never returns - this process terminates with
# the exit code of the child (or with one of our RC_* exit codes)
def run_child(cmdline):
    # This function is implemented using pywin32 modules instead
    # of 'multiprocessing' etc to act as a reference for the C
    # implemented runner.
    debug("executing child cmdline %r" % (cmdline,))
    si = STARTUPINFO()
    ok, si.hStdInput = safe_duplicate_handle(GetStdHandle(STD_INPUT_HANDLE))
    if not ok:
        error("can't duplicate stdin", RC_NO_STD_HANDLES);
    ok, si.hStdOutput = safe_duplicate_handle(GetStdHandle(STD_OUTPUT_HANDLE))
    if not ok:
        error("can't duplicate stdout", RC_NO_STD_HANDLES);
    ok, si.hStdError = safe_duplicate_handle(GetStdHandle(STD_ERROR_HANDLE))
    if not ok:
        error("can't duplicate stderr", RC_NO_STD_HANDLES);

    si.dwFlags = STARTF_USESTDHANDLES;
    try:
        info = CreateProcess(None,
                             cmdline,
                             None, # process attributes
                             None, # thread attributes
                             1, # inherit handles
                             0, # create flags
                             None, # new environment
                             None, # cwd,
                             si) # startup info
    except win32api_error as exc:
        error("can't create process", RC_CREATE_PROCESS)
    hProcess, hThread, dwProcessId, dwThreadId = info
    hThread.Close()
    try:
        WaitForSingleObject(hProcess, INFINITE)
    except KeyboardInterrupt:
        pass
    exitcode = GetExitCodeProcess(hProcess)
    debug("child exit code is %d" % (exitcode,))
    sys.exit(exitcode)


# *** Shebang parsing ***
# Parse a shebang line given the "head" of some file.  Returns (is_virt, cmd).
# If cmd is None, no shebang line could be parsed.  Otherwise, if  is_virt 
# is true, cmd will be a 'virtual' Python reference, such as 'python2'.
# If is_virt is False, cmd will be a fully qualified path to an executable
# (which may or may not exist).
def parse_shebang(head):
    match = re.compile(r"#!\s*(\S[^\r\n]*)[\r\n]", re.MULTILINE).match(head)
    if match is None:
        return False, None
    cmd = match.group(1)
    for vp in VIRT_PATHS:
        if cmd.startswith(vp):
            return True, cmd[len(vp):]
    return False, cmd


def maybe_handle_shebang(argv, cmdline):
    # Look for a shebang line in the first argument.  If found
    # and we spawn a child process, this never returns.  If it
    # does return then we process the args "normally".

    # argv[0] might be a filename with a shebang.
    shebang_script = argv[0]
    try:
        with open(shebang_script, "rb") as f:
            is_virt, cmd = parse_shebang(f.read(128))
    except IOError:
        is_virt = cmd = None
    if cmd is None:
        return
    # found a shebang line
    if is_virt:
        if " " in cmd:
            virt, rest = cmd.split(" ", 1)
        else:
            virt = cmd
            rest = ""
        if not virt.startswith("python"):
            error("unknown virtual path '%s'" % virt, RC_BAD_VIRTUAL_PATH)
        wanted_ver = virt[6:]
        exe = locate_python(wanted_ver)
        if exe is not None:
            run_child(exe + " " + rest + " " + shebang_script)
        error("Can't find a python matching version '%s'" % wanted_ver, RC_NO_PYTHON)
    else:
        # assumed to be a fully-qualified path to the executable...
        run_child(cmd + " " + cmdline)


# *** command-line handling
# Given the cmdline of the current process, skip past all references to
# this launcher (ie, references to this executable)
def skip_me_on_cmdline(cmdline):
    # only in .py version - strip sys.executable from cmdline
    quoted = cmdline.startswith('"')
    if quoted:
        cmdline = cmdline[1:]
    endchar = '"' if quoted else " "
    cmdline = cmdline[cmdline.index(endchar)+1:].lstrip()
    # Now strip argv[0] (ie, in the Python version, this launcher script)
    assert cmdline.startswith(sys.argv[0]), (cmdline, sys.argv)
    cmdline = cmdline[len(sys.argv[0]):].lstrip()
    return cmdline


def main(argv):
    cmdline = GetCommandLine()
    cmdline = skip_me_on_cmdline(cmdline)
    argv.pop(0) # remove my script from argv
    if len(argv) > 1 and argv[1] != "-":
        maybe_handle_shebang(argv, cmdline)
    # No file with shebang or unrecognised shebang - see if the first arg
    # is a special version qualifier.
    if argv and len(argv[0])==2 and argv[0][0]=='-' and \
       argv[0][1].isdigit():
        # A major version only is specified.
        exe = locate_python(argv[0][1:])
        cmdline = cmdline[2:].lstrip()
    elif argv and len(argv[0])==4 and argv[0][0]=='-' and \
         argv[0][1].isdigit() and argv[0][2]=='.' and argv[0][3].isdigit():
        # A major.minor version is specified.
        exe = locate_python(argv[0][1:])
        cmdline = cmdline[4:].lstrip()
    else:
        # no version if specified - use the default.
        exe = locate_python("")
        if exe is None:
            error("Can't find a default python", RC_NO_PYTHON)
    if exe is None:
        error("Can't find that python version installed", RC_NO_PYTHON)
    cmd = exe + " " + cmdline
    run_child(cmd)


if __name__=='__main__':
    main(sys.argv)
