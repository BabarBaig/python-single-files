<<<<<<< HEAD
# ==== start ====================
import os
import shutil

def dir_list(directory):
    os.chdir(directory)
    num_files=0
    for filename in os.listdir():
        print(filename)
        counter += 1
        if counter > 1000:
            break
    print(num_files)

def dir_rename_01():
    base_dir = "G:/000.Sync/08.Baig.Pics"
    fn_old = ''
    fn_new = ''
    for fn_old in os.listdir(base_dir):
        if len(fn_old) < 10 or fn_old[0] != '2' or fn_old[4] != '.':
            continue
        date_old = fn_old[0:10]
        name_str = fn_old[10:]
        date_new = fn_old[0:4] + '-' + fn_old[5:7] + '-' + fn_old[8:10]
        fn_new   = date_new + name_str
#       print(fn_old+'\t'+fn_new)
        os.rename(os.path.join(base_dir, fn_old), os.path.join(base_dir, fn_new))

def dir_rename_02():
    base_dir = "G:/000.Sync/08.Baig.Pics/2008 or earlier"
    fn_old = ''
    fn_new = ''
    for fn_old in os.listdir(base_dir):
        if len(fn_old) < 7 or fn_old[6] != '.':
            continue
        date_old = fn_old[0:6]
        name_str = fn_old[7:]
        date_new = "20" + fn_old[0:2] + '-' + fn_old[2:4] + '-' + fn_old[4:6] + " "
        fn_new   = date_new + name_str
#       print(fn_old+'\t'+fn_new)
        os.rename(os.path.join(base_dir, fn_old), os.path.join(base_dir, fn_new))

def file_move(src_path, dest_path):
    shutil.move(src_path, dest_path)

def file_rename_01(name_old, name_new):
    os.rename(name_old, name_new)

def file_rename_01(directory, phrase_old, phrase_new):
    print(phrase_old, phrase_new)
    os.chdir(directory)
    filename_new = ""
    for filename_old in os.listdir():
        if (phrase_old not in filename_old):
            continue
        print(filename_old)
        index = filename_old.find(phrase_old)
        filename_new = filename_old[0:index] + phrase_new + filename_old[len(phrase_old):]
        print(filename_new)
        shutil.move(filename_old, filename_new)

def file_rename_pattern(chg_dir, pattern_old, pattern_new):
    os.chdir(chg_dir)
    for fname_old in os.listdir():
        if (pattern_old in fname_old):
            fname_new = fname_old.replace(pattern_old, pattern_new)
            if input ("Rename:\n[" + fname_old + "] to\n[" + fname_new + "]?\nPress: 'n' or 'x' to exit") in ['n', 'x']:
                break
            os.rename(fname_old, fname_new)

def main():
    file_rename_pattern("C:/Users/Baig-Admin/SkyDrive/Sync/02.Babar",
        "#Misc_2014-04-28", "#Misc_2014-05-09")
#   file_rename_01("C:/Users/Baig-Admin/SkyDrive/Sync/02.VDI-Systems/114_CTRI-3_5DSS0353",
#       "14649900",
#       "114.f_14649900")
#   rename_file_01("C:/Users/Baig-Admin/SkyDrive/Sync/02.VDI-Systems/121_CTRI-5_5DSS0504/14649900.pdf",
#               "C:/Users/Baig-Admin/SkyDrive/Sync/02.VDI-Systems/121_CTRI-5_5DSS0504/121.f_14649900.pdf")
#   file_move("C:/Users/Baig-Admin/SkyDrive/Sync/02.VDI-Systems/14649900.pdf",
#             "C:/Users/Baig-Admin/SkyDrive/Sync/02.VDI-Systems/114_CTRI-3_5DSS0353")
#   rename_dir02()

if __name__ == '__main__':
    main()
=======
# ==== start ====================
import os
import shutil

def dir_list(directory):
    os.chdir(directory)
    num_files=0
    for filename in os.listdir():
        print(filename)
        counter += 1
        if counter > 1000:
            break
    print(num_files)

def dir_rename_01():
    base_dir = "G:/000.Sync/08.Baig.Pics"
    fn_old = ''
    fn_new = ''
    for fn_old in os.listdir(base_dir):
        if len(fn_old) < 10 or fn_old[0] != '2' or fn_old[4] != '.':
            continue
        date_old = fn_old[0:10]
        name_str = fn_old[10:]
        date_new = fn_old[0:4] + '-' + fn_old[5:7] + '-' + fn_old[8:10]
        fn_new   = date_new + name_str
#       print(fn_old+'\t'+fn_new)
        os.rename(os.path.join(base_dir, fn_old), os.path.join(base_dir, fn_new))

def dir_rename_02():
    base_dir = "G:/000.Sync/08.Baig.Pics/2008 or earlier"
    fn_old = ''
    fn_new = ''
    for fn_old in os.listdir(base_dir):
        if len(fn_old) < 7 or fn_old[6] != '.':
            continue
        date_old = fn_old[0:6]
        name_str = fn_old[7:]
        date_new = "20" + fn_old[0:2] + '-' + fn_old[2:4] + '-' + fn_old[4:6] + " "
        fn_new   = date_new + name_str
#       print(fn_old+'\t'+fn_new)
        os.rename(os.path.join(base_dir, fn_old), os.path.join(base_dir, fn_new))

def file_move(src_path, dest_path):
    shutil.move(src_path, dest_path)

def file_rename_01(name_old, name_new):
    os.rename(name_old, name_new)

def file_rename_01(directory, phrase_old, phrase_new):
    print(phrase_old, phrase_new)
    os.chdir(directory)
    filename_new = ""
    for filename_old in os.listdir():
        if (phrase_old not in filename_old):
            continue
        print(filename_old)
        index = filename_old.find(phrase_old)
        filename_new = filename_old[0:index] + phrase_new + filename_old[len(phrase_old):]
        print(filename_new)
        shutil.move(filename_old, filename_new)

def file_rename_pattern(chg_dir, pattern_old, pattern_new):
    os.chdir(chg_dir)
    for fname_old in os.listdir():
        if (pattern_old in fname_old):
            fname_new = fname_old.replace(pattern_old, pattern_new)
            if input ("Rename:\n[" + fname_old + "] to\n[" + fname_new + "]?\nPress: 'n' or 'x' to exit") in ['n', 'x']:
                break
            os.rename(fname_old, fname_new)

def main():
    file_rename_pattern("C:/Users/Baig-Admin/SkyDrive/Sync/02.Babar",
        "#Misc_2014-04-28", "#Misc_2014-05-09")
#   file_rename_01("C:/Users/Baig-Admin/SkyDrive/Sync/02.VDI-Systems/114_CTRI-3_5DSS0353",
#       "14649900",
#       "114.f_14649900")
#   rename_file_01("C:/Users/Baig-Admin/SkyDrive/Sync/02.VDI-Systems/121_CTRI-5_5DSS0504/14649900.pdf",
#               "C:/Users/Baig-Admin/SkyDrive/Sync/02.VDI-Systems/121_CTRI-5_5DSS0504/121.f_14649900.pdf")
#   file_move("C:/Users/Baig-Admin/SkyDrive/Sync/02.VDI-Systems/14649900.pdf",
#             "C:/Users/Baig-Admin/SkyDrive/Sync/02.VDI-Systems/114_CTRI-3_5DSS0353")
#   rename_dir02()

if __name__ == '__main__':
    main()
>>>>>>> 3a3eeac04cbe757a5a977da746abe95ab991826d
