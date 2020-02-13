
import shutil
import os
import sys

''' 打印脚本用法'''
def usage():
    print("usage:"+sys.argv[0]+" <source_path> <target_path>")

def copy_files(source, target):
    shutil.copytree(source, target)


def get_path(path:str, if_exit=False):
    if not os.path.exists(path) :
        if not if_exit:
            os.makedirs(path)
        else:
            print("path: %s is not exists!"% (path))
            exit()


    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        exit()
    source = sys.argv[1]
    target = sys.argv[2]
    
    get_path(source, True)
    get_path(target)
    copy_files(source, target)
