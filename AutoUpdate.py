import os
import sys
import subprocess


def pull(path):
    listdir = os.walk(path)
    for root, dirs, files in listdir:
        if '.git' in dirs:
            a = os.getcwd()
            print(root)
            os.chdir(root)
            try:
                out_bytes = subprocess.check_output(['git', 'pull'])
                print(out_bytes.decode('utf-8'))
            except:
                pass
            os.chdir(a)


if __name__ == "__main__":
    pull(path = sys.argv[1])
