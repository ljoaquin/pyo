import sys
import trivia

def run(cmd):
    return trivia.run(cmd)

def popen(cmd):
    return trivia.popen(cmd)

def reinstall(apk_path):

    cmd = "aapt dump badging %s" % apk_path
    ret, out, err = popen(cmd)
    # print ret, out, err

    pt_package_name = "package: name='"
    pt_launch_activity = "\nlaunchable-activity: name='"
    package_name = trivia.extract(out, pt_package_name, "'")
    launch_activity_name = trivia.extract(out, pt_launch_activity, "'")

    cmds = [ 
        "adb uninstall %s" % package_name,
        "adb install %s" % apk_path,
        "adb shell am start -n %s/%s" % (package_name, launch_activity_name),
    ]
    for cmd in cmds:
        run(cmd)


def main():
    argv = sys. argv
    argc = len(argv)

    apk_path = None

    if argc == 2:
        apk_path = argv[1]
        print "apk_path:" + apk_path

    if apk_path == None or not trivia.exists(apk_path):
        print "install failed, apk_path:", apk_path
        exit(-1)

    reinstall(apk_path)

if __name__ == '__main__':
    main()
