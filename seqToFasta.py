#!usr/bin/env python3
# -*- coding:utf-8 -*-
# seqToFasta v1.00
# Coding by Quincey, Shuyi Zhang Lab

from glob import glob
from re import compile, findall, match
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


# function
def run_script():
    button.configure(text='Running', state='disabled')
    name_pattern = compile(r'[(](.*?)[)]')      # get string in bracers
    count = 0       # number of files
    folder = dirText.get().replace('\\', '/')
    file_list = glob(f'{folder}/*.seq')
    if not file_list:       # if wrong path was entered, end this function
        outBox.configure(state='normal')
        outBox.insert(tk.END, '\nNo .seq files found. Please enter a correct folder path.\n\n')
        outBox.see(tk.END)
        outBox.configure(state='disabled')
        button.configure(text='Start', state='normal')
        return
    out_file_name = folder.split('/').pop()

    with open(f'{folder}/{out_file_name}.fasta', 'w') as fileOut:
        for file in file_list:
            fileIn = file.split('\\').pop()
            if match(name_pattern, fileIn) is None:
                sampleName = fileIn
                print(f'>{sampleName}', file=fileOut)
            else:
                sampleName = findall(name_pattern, fileIn)[0]
                print(f'>{sampleName}', file=fileOut)

            with open(file) as readFile:
                for lines in readFile:
                    print(lines.rstrip(), file=fileOut)
            outBox.configure(state='normal')
            outBox.insert(tk.END, f'Processed {fileIn}.\n')
            outBox.see(tk.END)
            outBox.configure(state='disabled')
            count += 1

    outBox.configure(state='normal')
    outBox.insert(tk.END, f'''\nComplete. {count} file(s) processed. \nPlease check {fileOut.name}.\n\nEnter another path to continue, or close to quit.\n''')
    outBox.see(tk.END)

    button.configure(text='Start', state='normal')
    outBox.configure(state='disabled')


# User interface
head = f'''            ===========================================
                                                seqToFasta v 1.00
            ===========================================   
Enter full path of a folder contains .seq files (e.g. D:\测序结果) here and click Start.   '''

welcomePage = f'''\
Coded by Quincey, Shuyi Zhang Lab\n\n\
Make sure you're processing Sanger sequencing files by Sangon.\n\n\
If you have any problems using it, please contact quincey@bemani.cn.\n\n'''

window = tk.Tk()
window.title('SeqToFasta')
window.resizable(0,0)

topLabel = ttk.Label(window, text=head)
topLabel.grid(row=0, column=0, sticky='NS', columnspan=10, pady=10)

dirText = tk.StringVar()
dirInput = ttk.Entry(window, width=65, textvariable=dirText)
dirInput.grid(row=1, column=0, columnspan=9, sticky=tk.E, padx=5)
dirInput.focus()

button = ttk.Button(window, text='Start', width=10, command=run_script)
button.grid(row=1, column=9, padx=5)

labelsFrame = ttk.LabelFrame(window, text='Running status')
labelsFrame.grid(row=4, column=0, columnspan=10, sticky=tk.W, padx=5, pady=10)

outBox = scrolledtext.ScrolledText(labelsFrame, width=75, height=30, wrap=tk.WORD)
outBox.grid(row=0, column=0)
outBox.insert(tk.END, welcomePage)
outBox.configure(state='disabled')

window.mainloop()

