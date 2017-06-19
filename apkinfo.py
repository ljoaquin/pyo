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

def print_with_frame(title):
    middle = "|" + title + "|"
    side = "-" * len(middle)
    print side
    print middle
    print side

def extract_md5(content):
    return trivia.extract(content, "MD5: ", "\n")
    
def extract_sha1(content):
    return trivia.extract(content, "SHA1: ", "\n")
    
def extract_sha256(content):
    return trivia.extract(content, "SHA256: ", "\n")

def main():
    argv = sys.argv
    argc = len(argv)

    if argc == 2:
        apk_path = argv[1]
        dump_content = dump(apk_path)
        sign_info = check_hash.get_apk_hash_raw(apk_path)
        key_hash = check_hash.get_apk_hash(apk_path)

        print_with_frame("APK Info")
        print "package_name:        " + extract_package_name(dump_content)
        print "launchable_activity: " + extract_launchable_activity(dump_content)
        print "version_code:        " + extract_version_code(dump_content)
        print "version_name:        " + extract_version_name(dump_content)
        print "min_sdk:             " + extract_min_sdk(dump_content)
        print "target_sdk:          " + extract_target_sdk(dump_content)
        print "key_hash:            " + key_hash
        print "md5:     " + extract_md5(sign_info)
        print "sha1:    " + extract_sha1(sign_info)
        print "sha256:  " + extract_sha256(sign_info)

if __name__ == '__main__':
    main()
