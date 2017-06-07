import sys
import trivia
import check_hash

def dump(apk_path):
    cmd = "aapt dump badging %s" % apk_path
    ret, out, err = trivia.popen(cmd)
    return out

def extract_package_name(content):
    return trivia.extract(content, "package: name='", "'")

def extract_launchable_activity(content):
    return trivia.extract(content, "\nlaunchable-activity: name='", "'")

def extract_version_code(content):
    return trivia.extract(content, "versionCode='", "'")

def extract_version_name(content):
    return trivia.extract(content, "versionName='", "'")

def extract_min_sdk(content):
    return trivia.extract(content, "sdkVersion:'", "'")

def extract_target_sdk(content):
    return trivia.extract(content, "targetSdkVersion:'", "'")

def main():
    argv = sys.argv
    argc = len(argv)

    if argc == 2:
        apk_path = argv[1]
        dump_content = dump(apk_path)
        apk_hash = check_hash.get_apk_hash(apk_path)

        print "package_name: " + extract_package_name(dump_content)
        print "launchable_activity: " + extract_launchable_activity(dump_content)
        print "version_code: " + extract_version_code(dump_content)
        print "version_name: " + extract_version_name(dump_content)
        print "min_sdk: " + extract_min_sdk(dump_content)
        print "target_sdk: " + extract_target_sdk(dump_content)
        print "hash: " + apk_hash

if __name__ == '__main__':
    main()
