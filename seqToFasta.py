#!usr/bin/env python3
# -*- coding:utf-8 -*-
# seqToFasta v0.7
# Coding by Quincey, Shuyi Zhang's Lab

from glob import glob
import re

print(f"===========================================\n"
      f"              seqToFasta v0.7\n"
      f"===========================================\n"
      f"Usage: Paste full path of a directory contains .seq files here.\n")

p1 = re.compile(r'\([^()]+\)')
count = 0

while True:
    folder = input('Please enter a directory: ')
    folder = folder.replace('\\', '/')
    fileName = input('Please enter name of the output file: ')
    fileList = glob(f'{folder}/*.seq')

    for file in fileList:
        with open(f'{folder}/{fileName}.fasta', 'a') as fout:
            fin = file.split('/').pop().split('\\').pop()
            print(f'Processing {fin}.')
            fastaHead = re.findall(p1, file)[0][1:-1]
            print(f'>{fastaHead}', file=fout)
            with open(file) as f:
                for lines in f:
                    lines = lines.rstrip()
                    print(lines, file=fout)
            count += 1

    print(f'\nComplete. {count} file(s) processed. Please check the output file.\n'
          f'\n'
          f'Paste another directory to continue, or close the window to quit.\n')
