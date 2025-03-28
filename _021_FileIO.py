import sys, os

def sys_demo():
    print(sys.version)
    print(sys.argv)
    if len(sys.argv) >= 3:
        print(int(sys.argv[1]) + int(sys.argv[2]))
    print(sys.path)

def os_demo():
    cwd = os.getcwd()
    print(cwd)
    # print(os.listdir(cwd))

    demodir = os.path.join(cwd, "demo_dir")
    if os.path.exists(demodir):
        print("Folder already exists")
    else:
        os.mkdir(demodir)
        print("Folder created!")

    demofile = os.path.join(demodir, "demo.txt")
    with open(demofile, "w") as f1:
        """
        if f1.readable:             # Why is this readable?
            print("File is readable")
            print(f1.read())
        else:
            print("This file is not readable")
        """    
        if f1.writable:
            # f1.write("This is a test file\nSecondline\nThird line")
            f1.writelines(['This is a test file', 'Secondline', 'Third line'])
        else:
            print("Can't write into this file")

        # f1.flush()
        # f1.tell()
        # f1.seek()

    with open(demofile, "r") as f1:
        if f1.readable:
            # s1 = f1.read(512)
            # s1 += "!!"
            # print(s1)
            # print(f1.readline())
            print(f1.readlines(100))
        else:
            print("Can't read this file")

    if os.path.exists(demofile):
        os.remove(demofile)
        print("Removed the file")
    else:
        print("File not present")

    if os.path.exists(demodir):
        os.rmdir(demodir)
        print("Removed the folder")
    else:
        print("Folder not present")

# sys_demo()
os_demo()