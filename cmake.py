import trivia
import sys

BUILD_PATH = "./build"

def run_and_check(cmd):
    r = trivia.run(cmd)
    if r != 0:
        print "[error]cmd:" + cmd
        return False
    return True

def main():
    cmds = [
        "rm -rf %s" % BUILD_PATH,
        "cmake -H. -B%s" % BUILD_PATH,
        "cmake --build %s" % BUILD_PATH,
    ]

    if sys.platform == "win32":
        cmds[1] = "cmake -H. -Bbuild -G \"Visual Studio 12 2013\""

    index = None
    if len(sys.argv) == 2:
        index = int(sys.argv[1])

    if index != None and index >= 0 and index < len(cmds):
        cmd = cmds[index]
        trivia.run(cmd)
        return

    for cmd in cmds:
        succ = run_and_check(cmd)
        if not succ:
            return

if __name__ == '__main__':
    main()
