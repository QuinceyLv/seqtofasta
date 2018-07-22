#!usr/bin/env python3
# -*- coding:utf-8 -*-
# seqToFasta v0.3
# Coding by Quincey, Shuyi Zhang's Lab

import glob
import re

pattern0 = re.compile(r'\\')
pattern1 = re.compile(r'\(\w+\)')

while True:
    folder = input('Please enter the directory: ')
    folder = folder.replace('\\','/')
    if folder == 'quit':
        break
    else:
        print(f'Your working directory is {folder}. \n')
        fileName = input('Please enter name of the output file: ')

        fileList = glob.glob(f'{folder}/*.seq')

        for file in fileList:
            fout = open(f'{folder}/{fileName}.fasta','a')
            print(f'Processing {file}.')
            fastaHead = re.search(pattern1,file)
            print(f'>{fastaHead.group()[1:-1]}', file=fout)
            with open(file) as f:
                for lines in f:
                    lines= lines.rstrip()
                    print(lines, file=fout)

        print('''Complete. Please check the output file.
        
        Paste another directory to continue, or enter "quit" to quit.\n''')
