#!/usr/bin/python3

import os, sys;

def get_size(path) -> int:
    size = 0;
    if os.path.isfile(path):
        size = os.path.getsize(path);
    else:
        for dpath, dnames, fnames in os.walk(path):
            for fname in fnames:
                fp = os.path.join(dpath, fname);
                if os.path.isfile(fp):
                    size += os.path.getsize(fp);
    return size;

def human_readable_size(size: int) -> str:
    for unit in ['B', 'Kb', 'Mb', 'Gb', 'Tb']:
        if size < 1024:
            break;
        size /= 1024;
    return "{:.1f} {}".format(size, unit);

def main():

    mode_flag: bool = True;

    if len(sys.argv) > 1 and sys.argv[1] == '-l':
        mode_flag = False;
    elif len(sys.argv) > 1 and sys.argv[1] == '-m':
        mode_flag = True;
    elif len(sys.argv) > 1 and sys.argv[1] == '-h':
        print("-l sort by decreasing size, -m sort by increasing size, -h to print help");
        sys.exit(0);

    pwd = os.getcwd();
    items = os.listdir(pwd);
    result = [];

    for item in items:
        full_path = os.path.join(pwd, item);
        size = get_size(full_path);
        result.append((size, item));

    result.sort(key=lambda x: x[0], reverse=mode_flag);
    for size, item in result:
        print(f"{human_readable_size(size):10} {item:10}");

if __name__ == "__main__":
    main();
