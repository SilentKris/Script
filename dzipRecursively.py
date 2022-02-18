#!/usr/bin/env python

import os
import shutil
import zipfile

RELEASE_PATH = 'release'
release_dir = os.path.join(os.getcwd(), 'release')

if not os.path.exists(release_dir):
    os.mkdir(release_dir)
curPATH = os.getcwd()

def dzip(curPATH):
    zfileList = os.listdir(curPATH)
    for file in zfileList:
        file = os.path.join(curPATH, file)
        if zipfile.is_zipfile(file):
            zfilePath = file
            zFile = zipfile.ZipFile(zfilePath, "r")
            dzFilePath = zfilePath[:-len('.zip')]
            if os.path.exists(dzFilePath):
                shutil.rmtree(dzFilePath)
            os.mkdir(dzFilePath)
            for zipFile in zFile.namelist():
                zFile.extract(zipFile, dzFilePath)
                dzip(dzFilePath)
        else:
            continue
def Search(Suffix, curPath, release_Dir):
    fileList = os.listdir(curPath)
    if 'release' in fileList:
        fileList.remove('release')
    for file in fileList:
        filePath = os.path.join(curPath, file) 
        if os.path.isdir(filePath):
            Search(Suffix, filePath, release_Dir)
        elif os.path.isfile(filePath):
            if filePath[-len(Suffix):] == Suffix:
                shutil.copy2(filePath, release_Dir)
        else:
            continue
    
    
     
dzip(curPATH)
Search('.fnt', curPATH, release_dir)
for file in os.listdir(curPATH):
    filePath = os.path.join(curPATH, file)
    if os.path.isdir(filePath) and filePath != release_dir:
        shutil.rmtree(filePath)
if __name__ == '__main__':
    print('preform complete!')