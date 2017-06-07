import os
import sys
import trivia

def run(cmd):
    if cmd != None:
        print cmd
        os.system(cmd)

def get_apk_hash(apk_path):
    cmd = "keytool -list -printcert -jarfile %s | grep \"SHA1: \" | cut -d \" \" -f 3 | xxd -r -p | openssl base64" % apk_path
    ret, out_msg, err_msg = trivia.popen(cmd)
    return out_msg

def get_keystore_hash(keystore_path, alias):
    cmd = "keytool -exportcert -alias %s -keystore %s | openssl sha1 -binary | openssl base64" % (alias, keystore_path)
    ret, out_msg, err_msg = trivia.popen(cmd)
    return out_msg

def main():
    argv = sys.argv
    argc = len(argv)

    cmd = None

    if ".apk" == argv[1][-4:]:
        apk_path = argv[1]
        result = get_apk_hash(apk_path)

    if ".keystore" == argv[1][-9:]:
        alias = "androiddebugkey"
        if argc == 3:
            alias = argv[2]
        keystore_path = argv[1]
        result = get_keystore_hash(keystore_path, alias)

    print "hash:" + result

if __name__ == '__main__':
    main()