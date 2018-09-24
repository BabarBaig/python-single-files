import sys

def main():
    for i in range (10):
        print("Hello, world!!!")
    print(sys.argv)    # print command line arguments as a list [hello.py aaa bbb ccc]

if __name__ == '__main__':
    main()
