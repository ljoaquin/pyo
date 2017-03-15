import trivia

def print_with_frame(title):
    middle = "|" + title + "|"
    side = "-" * len(middle)
    print side
    print middle
    print side


def main():

    print_with_frame("test")

    path = "./tmp"
    print trivia.abspath(path)

    print "trivia.exists:" + str(trivia.exists(path))
    print "trivia.isdir:" + str(trivia.isdir(path))
    print "trivia.isfile:" + str(trivia.isfile(path))

    print_with_frame("trivia.mkdir:" + path)
    trivia.mkdir(path)

    print "trivia.exists:" + str(trivia.exists(path))
    print "trivia.isdir:" + str(trivia.isdir(path))
    print "trivia.isfile:" + str(trivia.isfile(path))

    print_with_frame("trivia.mkdir and trivia.remove:" + path)
    trivia.mkdir(path)
    trivia.remove(path)

    print "trivia.exists:" + str(trivia.exists(path))
    print "trivia.isdir:" + str(trivia.isdir(path))
    print "trivia.isfile:" + str(trivia.isfile(path))

    print_with_frame("create file:" + path)
    trivia.run("touch " + path)

    print "trivia.exists:" + str(trivia.exists(path))
    print "trivia.isdir:" + str(trivia.isdir(path))
    print "trivia.isfile:" + str(trivia.isfile(path))

    print_with_frame("trivia.remove:" + path)
    trivia.remove(path)

    print "trivia.exists:" + str(trivia.exists(path))
    print "trivia.isdir:" + str(trivia.isdir(path))
    print "trivia.isfile:" + str(trivia.isfile(path))

    print_with_frame("test files_filter")
    path = "/Users/xxx/Documents/tmp"

    def foo(path):
        return path[-4:] == ".jar"
    filepaths = trivia.files_filter(path, foo)
    print filepaths

    print_with_frame("test trivia.popen")
    r, out, err = trivia.popen("ls -al")
    print "r:\n" + str(r)
    print "out:\n" + out
    print "err:\n" + err
    
    r, out, err = trivia.popen("ls -z")
    print "r:\n" + str(r)
    print "out:\n" + out
    print "err:\n" + err

    print_with_frame("test trivia.md5")
    content = ""
    result = trivia.md5(content)
    print "string:%s, md5:%s" % (content, result)
    content = "test"
    result = trivia.md5(content)
    print "string:%s, md5:%s" % (content, result)

if __name__ == '__main__':
    main()
