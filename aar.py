import os
import sys

def run(cmd):
    print cmd
    return os.system(cmd)

argv = sys.argv
argc = len(argv)

if argc < 2:
    print "arg missing"
    quit()

path = argv[1]

if not os.path.exists(path) or not os.path.isfile(path):
    print "path error:" + path
    quit()

path = os.path.abspath(path)

dirpath = os.path.dirname(path)
print "dirpath:" + dirpath
filename = os.path.basename(path) # path[len(dirpath) + 1:]
print "filename:" + filename

output_path = os.path.join(dirpath, filename[:-4])
print "output_path:" + output_path

run("rm -rf " + output_path)
run("mkdir " + output_path)
os.chdir(output_path)
run("jar -xf " + path)

target_jar1 = "libs/%s.jar" % filename[:-4]
target_jar2 = "../%s.jar" % filename[:-4]
run("mv classes.jar " + target_jar1)
# run("cp %s %s" % (target_jar1, target_jar2))

run("rm R.txt")
check_list_dir = ["aidl", "assets", "jni"]
for d in check_list_dir:
    files = os.listdir(d)
    if len(files) == 0:
        run("rm -rf " + d)

run("mkdir src")
