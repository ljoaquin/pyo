import trivia
import sys

BUILD_PATH = "./build"

def main():
    cmds = [
        "rm -rf %s" % BUILD_PATH,
        "cmake -H. -B%s" % BUILD_PATH,
        "cmake --build %s" % BUILD_PATH,
    ]
    if sys.platform == "win32":
        cmds[1] = "cmake -H. -Bbuild -G \"Visual Studio 12 2013\""
    for cmd in cmds:
        r = trivia.run(cmd)
        if r != 0:
            print "[error]cmd:" + cmd
            return

if __name__ == '__main__':
    main()
