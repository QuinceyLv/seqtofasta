#!usr/bin/env python3
# -*- coding:utf-8 -*-
# seqToFasta v0.8
# Coding by Quincey, Shuyi Zhang's Lab

from glob import glob
import re

print(f"===========================================\n"
      f"              seqToFasta v0.9\n"
      f"===========================================\n"
      f"Usage: Paste full path of a directory contains .seq files here.\n")

namePattern = re.compile(r'[(](.*?)[)]', re.S)

while True:
    count = 0
    folder = input('Please enter a directory: ').replace('\\', '/')
    fileList = glob(f'{folder}/*.seq')
    outFileName = folder.split('/')[-1]

    with open(f'{folder}/{outFileName}.fasta', 'w') as fileOut:
        for file in fileList:
            fileIn = file.split('\\').pop()
            sampleName = re.findall(namePattern, fileIn)[0]
            print(f'>{sampleName}', file=fileOut)
            with open(file) as readFile:
                for lines in readFile:
                    print(lines.rstrip(), file=fileOut)
            print(f'Processed {fileIn}.')
            count += 1

    print(f'\nComplete. {count} file(s) processed. Please check the output file.\n'
          f'\n'
          f'Paste another directory to continue, or close to quit.\n')
