import os
import shutil
import subprocess
import hashlib

def run(cmd):
    print cmd
    return os.system(cmd)

def popen(cmd):
    print cmd
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out_msg, err_msg = p.communicate()
    return p.returncode, out_msg, err_msg

def abspath(path):
    return os.path.abspath(path)

def dirname(path):
    return os.path.dirname(path)

def exists(path):
    path = abspath(path)
    return os.path.exists(path)

def isdir(path):
    path = abspath(path)
    return os.path.isdir(path)

def isfile(path):
    path = abspath(path)
    return os.path.isfile(path)

def mkdir(path):
    path = abspath(path)
    if exists(path):
        print "[error]already exists:" + path
        return
    os.mkdir(path)

def mkdirs(path):
    path = abspath(path)
    if exists(path):
        print "[error]already exists:" + path
        return
    os.makedirs(path)

def remove(path):
    path = abspath(path)
    if exists(path):
        if isfile(path):
            os.remove(path)
        elif isdir(path):
            shutil.rmtree(path)
        else:
            print "[error]not file or dir"
    else:
        print "[error]no such path:" + path

# src: file only, no dir
def copy(src, dst):
    if not exists(src) or not isfile(src):
        print "[error]no such file:" + src
        return
    dir_path = dirname(dst)
    if not exists(dir_path):
        mkdirs(dir_path)
    shutil.copy2(src, dst)

# move file or directory
def move(src, dst):
    if not exists(src):
        print "[error]no such src:" + src
        return
    if not exists(dst):
        mkdirs(dst)
    shutil.move(src, dst)

def path_fix(path):
    return path.replace("\\", "/")

def path_join(dirpath, filename):
    return os.path.join(dirpath, filename)

def path_split(path):
    path = path_fix(path)
    return (dirname(path), path[path.rfind("/") + 1:])

def files_filter(rootdir, func):
    if not exists(rootdir) or not isdir(rootdir):
        print "[error]invalid rootdir:" + rootdir
        return
    filepaths = []
    for curroot, subdirs, fns in os.walk(rootdir):
        for fn in fns:
            if func(fn):
                filepath = curroot + "/" + fn
                filepath = abspath(filepath)
                filepaths.append(filepath)
    return filepaths

# extract("[hello]", "[", "]")
def extract(full_string, pattern_front, pattern_end):
    index0 = full_string.find(pattern_front)
    if index0 == -1:
        return
    index1 = index0 + len(pattern_front)
    result = full_string[index1:]
    index2 = result.find(pattern_end)
    if index2 == -1:
        return
    return result[:index2]

def md5(content):
    m = hashlib.md5()
    m.update(content)
    return m.hexdigest()
