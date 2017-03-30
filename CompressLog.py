import os


def main():
    print "Start to unzip file"

    root_path = './output'
    os.chdir(root_path)

    list_dirs = os.walk('.')
    for root, dirs, files in list_dirs:
        for f in files:
            cmd = 'tar czvf '+f[:-3]+'tgz '+ f
            #print cmd
            os.system(cmd)


if __name__ == "__main__":
    main()