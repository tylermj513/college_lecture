import webbrowser
import json
import sys
import pandas as pd
from pathlib import Path
import json
import math
import json2table
import json
from json2html import *
import os
import webbrowser
result = []
DEP=[]
folder = '040'
sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
for num in range(0, len(sub_folders)):
    DEP.append(sub_folders[num])  
 
for i in range(len(DEP)):
        

    dep = DEP[i][3:] 
    with open('index' + dep + '.txt', 'w', encoding='utf-8-sig') as f:
        def read_file_to_list(file_path):
            with open(file_path, 'r', encoding='utf-8-sig') as file:
                data = file.read().split(',')
                data = [line.strip() for line in data]
            return data

        file_path = dep + "name.txt"
        file_path2 = dep + "num.txt"
        A = read_file_to_list(file_path)
        B = read_file_to_list(file_path2)
        for i in range(0, len(B)-1):
            print("     <tr>   <td><font id=" + "num" + str(i) + ">" + B[i] + "</font></td>                ", file=f)
            print("   <td><font id=" + "name" + str(i) + ">" + A[i] + "</font></td>                ", file=f)
            print("<td><button onclick=" + '"' + "window.location.href='" +dep+ "/list" + B[i] + ".html'" + '"' + ">檢視</button></td>", file=f)
            print("<td><button onclick=" + '"' + "window.location.href='" +dep+ "/grade" + B[i] + ".html'" + '"' + ">檢視</button></td>", file=f)
            print("<td><button onclick=" + '"' + "window.location.href='" +dep+ "/data" + B[i] + ".html'" + '"' + ">檢視</button></td></tr>", file=f)
    print(dep)