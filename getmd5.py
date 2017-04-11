import trivia
import sys

def main():
    argv = sys.argv
    argc = len(argv)
    
    if argc < 2:
        print "missing file path"
        return

    filepath = argv[1]
    if not trivia.exists(filepath):
        print "no such file:" + filepath
        return

    f = open(filepath, "rb")
    content = f.read()
    f.close()

    print "md5:" + trivia.md5(content)

if __name__ == '__main__':
    main()
