#!/usr/bin/env python

import os
import shutil
import zipfile

RELEASE_PATH = 'release'
release_dir = os.path.join(os.getcwd(), 'release')

if not os.path.exists(release_dir):
    os.mkdir(release_dir)
curPATH = os.getcwd()

def dzip(PATH):
    curPATH = PATH
    zfileList = os.listdir(curPATH)
    for zfile in zfileList:
        if zfile.endswith('.fnt'):
            fntFile = os.path.join(curPATH, zfile)
            shutil.copy2(fntFile, release_dir)
        elif zfile.endswith('.zip'):
            filePath = os.path.join(curPATH, zfile)
            zFile = zipfile.ZipFile(filePath, "r")
            dzFile = filePath[:-len('.zip')]
            if os.path.exists(dzFile):
                shutil.rmtree(dzFile)
            else:
                os.mkdir(dzFile)
            for zipFile in zFile.namelist():
                zFile.extract(zipFile, dzFile)
                dzip(dzFile)
        else:
            continue
        
dzip(curPATH)
for file in os.listdir(curPATH):
    filePath = os.path.join(curPATH, file)
    if os.path.isdir(filePath) and filePath != release_dir:
        shutil.rmtree(filePath)
if __name__ == '__main__':
    print('preform complete!')