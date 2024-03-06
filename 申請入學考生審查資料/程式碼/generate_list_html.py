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
Dep=[]
folder = '040'
sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
for num in range(0, len(sub_folders)):
    Dep.append(sub_folders[num])  

 #B    科系資料夾名稱 
for i in range(len(Dep)):
        

    dep = Dep[i][3:]
    
    folder = '040/040' +dep

    
     
    sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
    B=[]
    for i in range(0,len(sub_folders)):
        
        B.append(sub_folders[i])  
    for i in range(0,len(B)):
        GEN_HTML =dep +"/"+"list"+B[i]+".html"
        
        folder = dep     
        f = open(GEN_HTML,'w', encoding='utf-8-sig')
        with open( folder+'/list'+B[i]+'.txt', 'r' ,encoding='utf-8') as g:
            str1 = g.read() 
          
        message = """
        <html><head>
        <link href="../首頁.css" rel="stylesheet" type="text/css">
        <script src="new.js"></script>       </head>
        <body>
        %s
        </body>
        </html>
        """%(str1)
        
        #写入文件
        f.write(message) 
        
        #关闭文件
        f.close() 