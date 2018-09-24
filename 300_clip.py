
def clip( lo, x, hi):
    ''' Take in three numbers and return a value between lo and hi.
    Return:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise '''
    return (min(max(x, lo), hi))

def main():
    print(clip(1, 4, 3))

if __name__ == '__main__':
    main()
