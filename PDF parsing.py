# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 00:06:46 2023

@author: alici
"""
import pdfminer
from pdfminer.high_level import extract_text
# Ref for above package to install: https://stackoverflow.com/questions/73831425/modulenotfounderror-no-module-named-pdfminer-high-level
import os
import re


os.chdir("file location")
filename = "pretraining.pdf"
text = extract_text(filename)

print(text)

# Split the text by lines, filter lines, and join them back
filtered_lines = [line for line in text.splitlines() if len(line.strip()) > 1]
filtered_text = '\n'.join(filtered_lines)

# Split the filtered text by lines and store in the 'lines' variable
lines = filtered_text.splitlines()

text = filtered_text.lower()

#Extracting Title and Authors
abstract_start_index = text.find("abstract")
title_author = text[0:abstract_start_index]

# Extracting abstract
abstract_end_index = text.find("index", abstract_start_index)  # Find index of "index"
if abstract_end_index == -1:
    abstract_end_index = text.find("keyword", abstract_start_index)  # Find index of "keyword"
    if abstract_end_index == -1:
        abstract_end_index = text.find("introduction\n", abstract_start_index)  # Find index of "introduction"

abstract = text[abstract_start_index+8:abstract_end_index]

# Extracting introduction
intro_start_index = text.find("introduction")
intro_end_index = text.find("conclusion\n", intro_start_index)  # The end of the Content might be another section
introduction = text[intro_start_index+12:intro_end_index]


print("Title And Authors:\n", title_author)
# print("\nAbstract:\n", abstract)
# print("\nIntroduction:\n", introduction)


# Open the file in write mode
file_path = 'output.txt'
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(introduction)

# File is automatically closed when you exit the 'with' block
print("pdf content from introduction has been written to the file.")


