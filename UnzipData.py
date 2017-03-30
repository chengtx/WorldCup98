import os
import fnmatch


def main():

    print "Start to unzip file"

    pattern = '*.gz'
    root_path = './input'
    tool_path = '/Users/tcheng/Downloads/benchmark/ita_public_tools/'

    list_dirs = os.walk(root_path)
    for root, dirs, files in list_dirs:
        for f in fnmatch.filter(files, pattern):
            cmd = 'gzip -dc input/' + f + ' | ' + tool_path + 'bin/recreate ' + tool_path + 'state/object_mappings.sort > output/' + f[:-3] + '.log'
            os.system(cmd)


if __name__ == "__main__":
    main()