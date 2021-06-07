<<<<<<< HEAD
def isPal(s):
   print s
   if (len(s) <= 1):    return True
   if (s[0] != s[-1]):  return False
   return isPal(s[1 : -1])

def toAlNumLower(s):
   s = s.lower()
   s1 = ''
   match_str = 'abcdefghijklmnopqrstuvwxyz0123456789'
   for c in s:
      if c in match_str:
         s1 += c
   return s1

def isPalindrome(s):
   s1 = toAlNumLower(s)
   return isPal(s1)

print isPalindrome('A bcd Ef G~0@1#2$3%2^1&0*G( f)e-D= cba ')
#
=======
def isPal(s):
   print s
   if (len(s) <= 1):    return True
   if (s[0] != s[-1]):  return False
   return isPal(s[1 : -1])

def toAlNumLower(s):
   s = s.lower()
   s1 = ''
   match_str = 'abcdefghijklmnopqrstuvwxyz0123456789'
   for c in s:
      if c in match_str:
         s1 += c
   return s1

def isPalindrome(s):
   s1 = toAlNumLower(s)
   return isPal(s1)

print isPalindrome('A bcd Ef G~0@1#2$3%2^1&0*G( f)e-D= cba ')
#
>>>>>>> 3a3eeac04cbe757a5a977da746abe95ab991826d
