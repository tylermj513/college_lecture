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

with open('index.txt', 'w', encoding='utf-8-sig') as f:
 
    file_path = 'dep.txt'  # 替换为实际的文件路径

    department = ()  # 创建一个空元组

    with open(file_path, 'r', encoding='utf-8-sig') as file:
           lines = file.read().splitlines()

# 将内容存储为列表
    dep_list = lines  
    
B=[]
folder = '040'
sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
for num in range(0, len(sub_folders)):
    B.append(sub_folders[num])  
 
for i in range(len(B)):
 
    print( dep_list[i])
    dep = B[i][3:]
        
    
    GEN_HTML = "index"+dep+".html"
    
    f = open(GEN_HTML,'w', encoding='utf-8-sig')
    with open('index'+dep+'.txt', 'r' ,encoding='utf-8') as g:
        str1 = g.read() 
        print(str1)
    message = """
    <html><head>
        <link href="首頁.css" rel="stylesheet" type="text/css">
 
    </head>

    <body>


        <table>
            <thead>
                <tr>
                <th colspan="6">{}</th>

                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>學測應試號碼</td>
                    <td>考生姓名</td>
                    <td>基本資料</td>
                    <td>修課紀錄</td>
                    <td>書審資料</td>
                </tr>
                {}

                
            </tbody>
        </table>
        <script src="new.js"></script>


    </body></html>
    """.format(dep_list[i], str1)
        
    f.write(message) 
        
    f.close()  




