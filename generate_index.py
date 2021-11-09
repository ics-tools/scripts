#!/usr/bin/env python3
import sys
import os

path = sys.argv[1]
http_path = sys.argv[2]
template_input = sys.argv[3]
output = sys.argv[4]

files = os.listdir(path)
files.sort()

tmp = ""

for f in files:
    if not os.path.isdir(f):
        tmp += f"- [{f}]({http_path}{f})\n"


with open(template_input, "r") as file1:
    l = file1.read()

with open(output, 'w') as file:
    file.writelines(l.replace("[[indextree]]", tmp))

