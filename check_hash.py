import os
import sys

def run(cmd):
    if cmd != None:
        print cmd
        os.system(cmd)

def main():
    argv = sys.argv
    argc = len(argv)

    cmd = None

    if ".apk" == argv[1][-4:]:
        apk_path = argv[1]
        cmd = "keytool -list -printcert -jarfile %s | grep \"SHA1: \" | cut -d \" \" -f 3 | xxd -r -p | openssl base64" % apk_path

    if ".keystore" == argv[1][-9:]:
        alias = "androiddebugkey"
        if argc == 3:
            alias = argv[2]
        keystore_path = argv[1]
        cmd = "keytool -exportcert -alias %s -keystore %s | openssl sha1 -binary | openssl base64" % (alias, keystore_path)

    run(cmd)

if __name__ == '__main__':
    main()