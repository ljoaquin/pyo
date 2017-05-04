import os
import shutil
import subprocess
import hashlib

def abspath(path):
    return os.path.abspath(path)

def dirpath(path):
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
        print "[error]no such:" + path

def move(src, dst):
    if not exists(dst):
        mkdirs(dst)
    shutil.move(src, dst)

def copy(src, dst):
    dir_path = dirpath(dst)
    if not exists(dir_path):
        mkdirs(dir_path)
    shutil.copy2(src, dst)

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

def run(cmd):
    print cmd
    return os.system(cmd)

def popen(cmd):
    print cmd
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out_msg, err_msg = p.communicate()
    return p.returncode, out_msg, err_msg

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
