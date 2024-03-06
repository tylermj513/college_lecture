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
 
from numpy import loadtxt 


Dep=[]
folder = '040'
sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
for num in range(0, len(sub_folders)):
    Dep.append(sub_folders[num])  

 #B    科系資料夾名稱 
for i in range(len(Dep)):
        

    dep = Dep[i][3:]


    folder = '040/040'+dep
    sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
    B=[]
    for i in range(0,len(sub_folders)):
        
        B.append(sub_folders[i]) 
 

    for x in range(0, len(B)): 
        result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(
            folder+"/"+B[x]) for f in filenames if f.lower().endswith('基本資料.json')]
        with open(dep+'/list'+B[x]+'.txt', 'w', encoding='utf-8-sig') as g:
            g.write(" <table>    <thead>      <tr>        <th colspan="+'"'+str(6)+'"'+">考生基本資料</th>      </tr>    </thead>    <tbody>")
            def get_from_json(jdata: dict, *keys):
                try:
                    data = jdata[keys[0]]
                except KeyError:
                    return None
                if len(keys) > 1:
                    return get_from_json(data, *keys[1:])
                return data
            for i in range(0, len(result)): 

 
                jsonpath = Path(result[0])
 
                with jsonpath.open('r', encoding='utf-8-sig') as dat_f:
                    data = json.loads(dat_f.read()) 
                    json_str = json.dumps(data) 
                    resp = json.loads(json_str)
                    
            
                g.write("    <tr>  <td>國民身分證統一編號</td>  ")
                g.write("<td>")    
                g.write(data['國民身分證統一編號'])
                
                g.write("</td></tr>")  
                
                g.write("    <tr>  <td>就讀學校代碼</td><td>  ")  
                g.write(data['就讀學校代碼'])
                
                g.write("</td></tr>")  
                g.write("    <tr>  <td>就讀學校或單位名稱</td><td>  ")  
                g.write(data['就讀學校或單位名稱'])


                g.write("</td></tr>")  
                g.write("    <tr>  <td>學生出生年月日</td><td>  ")  
                g.write(data['學生出生年月日'])

                

                g.write("</td></tr>")  
                g.write("    <tr>  <td>部別代碼</td><td>  ")  
                if data['部別代碼'] is None:
                    g.write("無")
                else:
                    g.write(data['部別代碼']['名稱'])


                g.write("</td></tr>")  
                g.write("    <tr>  <td>班別</td><td>  ")   
                if data['班別'] is None:
                    g.write("無")
                else:
                    g.write(data['班別']['名稱'])

                g.write("</td></tr>")  
                g.write("    <tr>  <td>群別代碼</td><td>  ")   
                if data['群別代碼'] is None:
                    g.write("無")
                else:
                    g.write(data['群別代碼']['名稱'])


                g.write("</td></tr>")  
                g.write("    <tr>  <td>科班學程別代碼</td><td>  ")   
                if data['科班學程別代碼'] is None:
                    g.write("無")
                else:
                    g.write(data['科班學程別代碼']['名稱'])

                g.write("</td></tr>")  
                g.write("    <tr>  <td>實驗教育學生學習型態</td><td>  ")  
                g.write(data['實驗教育學生學習型態'])

                g.write("</td></tr>")  
        
                