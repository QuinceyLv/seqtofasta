#!usr/bin/env python3
# -*- coding:utf-8 -*-
# seqToFasta v0.4
# Coding by Quincey, Shuyi Zhang's Lab

import glob
import re

print(f"=========================================\n"
      f"              seqToFasta v0.4\n"
      f"=========================================\n"
      f"Usage: Paste full path of a directory contains .seq files here.\n")
pattern0 = re.compile(r'\\')
pattern1 = re.compile(r'\(\w+\)')
count = 0

while True:
    folder = input('Please enter a directory: ')
    folder = folder.replace('\\','/')
    if folder == 'quit':
        break
    else:
        print(f'\nYour working directory is {folder}. \n')
        fileName = input('Please enter name of the output file: ')
        fileList = glob.glob(f'{folder}/*.seq')

        for file in fileList:
            with open(f'{folder}/{fileName}.fasta','a') as fout:
                fin = file.split('/').pop().split('\\').pop()
                print(f'Processing {fin}.')
                fastaHead = re.search(pattern1,file).group()[1:-1]
                print(f'>{fastaHead}',file=fout)
                with open(file) as f:
                    for lines in f:
                        lines = lines.rstrip()
                        print(lines,file=fout)
                count += 1

        print(f'\nComplete. {count} file(s) processed. Please check the output file.\n'
              f'\n'
              f'Paste another directory to continue, or enter "quit" to quit.\n')
