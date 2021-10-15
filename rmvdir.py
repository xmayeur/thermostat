import os


def rmvdir(dir):
    for i in os.ilistdir(dir):
        if i[1] == 0x4000:
            rmvdir('{}/{}'.format(dir, i))
        elif i[1] == 0x8000:
            os.remove('{}/{}'.format(dir, i)[0])
    os.rmdir(dir)
