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
 
 
B=[]
folder = '040'
sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
for num in range(0, len(sub_folders)):
    B.append(sub_folders[num])  

 
file_path = 'dep.txt'  # 替换为实际的文件路径

department = ()  # 创建一个空元组

with open(file_path, 'r', encoding='utf-8-sig') as file:
    lines = file.readlines()  # 读取文件的所有行

    for line in lines:
        line = line.rstrip('\n')  # 去除换行符
        department += (line,)  # 将每行内容添加到元组中


Dep=[]
folder = '040'
sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
for num in range(0, len(sub_folders)):
    Dep.append(sub_folders[num])  

 #B    科系資料夾名稱 
for i in range(len(Dep)):
        

    dep = Dep[i][3:]
    
    folder = '040/040' + dep
    sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]

    B=[]
    print(department[i])


    for num in range(0,len(sub_folders)):
        
        B.append(sub_folders[num])  


    def percentage(progress, total):
        return round((progress / total) * 100)
 

    percentages_to_print = [10, 20, 30, 40, 50, 60, 70, 80, 90,100]
    printed_percentages = []

    for num in range(0,len(B)):
        current_percentage = percentage(num, len(B))
        if current_percentage in percentages_to_print and current_percentage not in printed_percentages:
            print(current_percentage)
            printed_percentages.append(current_percentage)
 
        result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(
            folder+"/"+B[num]) for f in filenames if f.lower().endswith('修課紀錄.json')]
            
        result2 = [os.path.join(dp, f) for dp, dn, filenames in os.walk(
            folder+"/"+B[num]) for f in filenames if f.lower().endswith('修課紀錄.pdf')]



        with open(dep+'/sem'+B[num]+'.txt', 'w', encoding='utf-8-sig') as g:
            def get_from_json(jdata: dict, *keys):

                try:
                    data = jdata[keys[0]]
                except KeyError:
                    return None
                if len(keys) > 1:
                    return get_from_json(data, *keys[1:])
                return data 
            if len(result2) > 0 and result2[0] is not None:
                g.write("  <a href="+'"'+"../040/040"+str(dep)+"/"+ str(B[num])+"/"+str(B[num       ])+"_修課紀錄.pdf"+'"'+">修課紀錄</a>")

            elif len(result) > 0 and result[0] is not None:
                g.write(" <h2>修課紀錄</h2>    <table>        <thead>            <tr>                <th colspan="+'"'+str(9)+'"'+">學期成績與學習相對表現資訊</th>            </tr>        </thead>        <tbody>            <tr>                <td width="+'"'+str(5)+"%"+'"'+">學年度</td>                <td width="+'"'+str(5)+"%"+'"'+">學期</td>                <td width="+'"'+str(10)+"%"+'"' +
                        ">學生學期成績</td>                <td width="+'"'+str(13.5)+"%"+'"'+">校學習相對表現資訊_母體人數</td>                <td width="+'"'+str(15)+"%"+'"'+">群別學習相對表現資訊_母體人數 </td>                <td width="+'"'+str(19)+"%"+'"'+">科班學程別學習相對表現資訊_母體人數 </td>                <td>校學習相對表現資訊_PR</td>                <td>群別學習相對表現資訊_PR</td>                <td>科班學程別學習相對表現資訊_PR</td>            </tr>    ")
                jsonpath = Path(result[0])
        
                with jsonpath.open('r', encoding='utf-8-sig') as dat_f:
                    data = json.loads(dat_f.read()) 
                    json_str = json.dumps(data)
        
                    resp = json.loads(json_str)

                jsonData = data["學期成績與學習相對表現資訊"]  


            

                
                for i in range(1,len(jsonData)):

                    g.write("<tr>")
        
                    jsonpath = Path(result[0])
        
                    with jsonpath.open('r', encoding='utf-8-sig') as dat_f:
                        data = json.loads(dat_f.read()) 
                        json_str = json.dumps(data)
        
                        resp = json.loads(json_str)

                    jsonData = data["學期成績與學習相對表現資訊"] 
                    g.write("<td>")
                    g.write(str(jsonData[i]['學年度']))

                    g.write("</td><td>")
                    g.write(str(jsonData[i]['學期']))

                    g.write("</td><td>")
                    g.write(str(jsonData[i]['學生學期成績']))

                    g.write("</td><td>")
                    g.write(str(jsonData[i]['校學習相對表現資訊']['母體人數']))

                    g.write("</td><td>")
                    g.write(str(jsonData[i]['群別學習相對表現資訊']['母體人數']))

                    g.write("</td><td>")
                    g.write(str(jsonData[i]['科班學程別學習相對表現資訊']['母體人數']))

                    g.write("</td><td>")
                    a = jsonData[i]['校學習相對表現資訊']['母體人數']

                    b = jsonData[i]['學生學期成績']
                    grade = math.ceil(b)

                    c = 0
                    for x in range(grade, len(jsonData[i]['校學習相對表現資訊']['分數級距分布'])):
                        j = str(x)
                        k = str(x+1)
                        z = '組距'+j+'_'+k+'的人數'
                        a = jsonData[i]['校學習相對表現資訊']['分數級距分布'][z]
                        d = int(a)
                        c = c+d
                    g.write(str(int(
                        100*round((jsonData[i]['校學習相對表現資訊']['母體人數']-(c+1))/jsonData[i]['校學習相對表現資訊']['母體人數'], 2))))

                    g.write("</td><td>")
                    grade = math.ceil(b)

                    c = 0
                    for x in range(grade, len(jsonData[i]['群別學習相對表現資訊']['分數級距分布'])):
                        j = str(x)
                        k = str(x+1)
                        z = '組距'+j+'_'+k+'的人數'
                        a = jsonData[i]['群別學習相對表現資訊']['分數級距分布'][z]
                        d = int(a)
                        c = c+d
                    g.write(str(int(
                        100*round((jsonData[i]['群別學習相對表現資訊']['母體人數']-(c+1))/jsonData[i]['群別學習相對表現資訊']['母體人數'], 2))))

                    g.write("</td><td>")
                    grade = math.ceil(b)

                    c = 0
                    for x in range(grade, len(jsonData[i]['科班學程別學習相對表現資訊']['分數級距分布'])):
                        j = str(x)
                        k = str(x+1)
                        z = '組距'+j+'_'+k+'的人數'
                        a = jsonData[i]['科班學程別學習相對表現資訊']['分數級距分布'][z]
                        d = int(a)
                        c = c+d
                    g.write(str(int(
                        100*round((jsonData[i]['科班學程別學習相對表現資訊']['母體人數']-(c+1))/jsonData[i]['科班學程別學習相對表現資訊']['母體人數'], 2))))
                    g.write("</td>")

                    g.write("</tr>   ")

                g.write("    </tbody>    </table>")
                g.write("    <a href="+'"'+"../040_grade6/040"+str(dep)+"/"+   str(B[num])+"/"+str(B[num])+"_第6學期成績單.pdf"+'"'+">第6學期成績單</a>")
            
            else:
                g.write("none")

        with open(dep+'/sem'+B[num]+'.txt', 'a', encoding='utf-8-sig') as g:
            if len(result2) > 0 and result2[0] is not None:
                g.write(" ")
            elif len(result) > 0 and result[0] is not None:
                    
                g.write("  <h2>學習紀錄</h2>    <table>        <tr>                             <td width="+'"'+str(7)+"%"+'"'+">實際修課學年度 </td>  <td width="+'"'+str(8)+"%"+'"'+">實際修課學期</td>        <td width="+'"'+str(15)+"%"+'"'+">科目名稱</td>            <td width="+'"'+str(10)+"%"+'"'+">學分數</td>            <td width="+'"'+str(15)+"%"+'"'+">課程類別 </td>           <td width="+'"'+str(10)+"%"+'"'+">課程領域資訊 </td>            <td width="+'"'+str(10)+"%"+'"'+">學業成績</td>            <td width="+'"'+str(10)+"%"+'"'+">母體人數</td>    <td width="+'"'+str(10)+"%"+'"'+">PR</td>")
                def get_from_json(jdata: dict, *keys):
                    try:
                        data = jdata[keys[0]]
                    except KeyError:
                        return None
                    if len(keys) > 1:
                        return get_from_json(data, *keys[1:])
                    return data
                
                
                jsonpath = Path(result[0])

                
                with jsonpath.open('r', encoding='utf-8-sig') as dat_f:
                    data = json.loads(dat_f.read()) 
                    json_str = json.dumps(data)
        
                    resp = json.loads(json_str)
                jsonData = data["學習紀錄"]
                        
                for i in range(0, len(jsonData)): 



        
                    jsonpath = Path(result[0])
        
                    with jsonpath.open('r', encoding='utf-8-sig') as dat_f:
                        data = json.loads(dat_f.read()) 
                        json_str = json.dumps(data)
        
                        resp = json.loads(json_str)
                        

                    g.write("<tr>") 
                    jsonData = data["學習紀錄"]
                    g.write("<td>") 
                    g.write(str(jsonData[i]['實際修課學年度']))
                    
                    g.write("</td><td>") 
                    g.write(str(jsonData[i]['實際修課學期']))
                    
                    g.write("</td><td>") 
                    g.write(jsonData[i]['科目名稱'])

                    g.write("</td><td>") 
                    g.write(str(jsonData[i]['學分數']))

                    
                    g.write("</td><td>") 
                    g.write(jsonData[i]['課程類別'])

                    g.write("</td><td>")  
                    if jsonData[i]['課程領域資訊'] is None:
                        g.write("無")
                    else:
                        g.write(jsonData[i]['課程領域資訊']['名稱'])

                    g.write("</td><td>") 
                    g.write(str(jsonData[i]['學業成績']['分數']))

                    
                    g.write("</td><td>") 
                    g.write(str(jsonData[i]['母體人數']))
                    g.write("</td><td>") 


                    a=jsonData[i]['母體人數']

                    b=jsonData[i]['學業成績']['分數']
                    d = int(float(b))

                    grade=math.ceil(d) 
                    
                    c=0
                    if(jsonData[i]['本科目分數級距分布']==None):
                        g.write("null")
                    else:

                        for x in range(grade,len(jsonData[i]['本科目分數級距分布'])):
                            j=str(x)
                            k=str(x+1) 
                            z='組距'+j+'_'+k+'的人數'
                            a=jsonData[i]['本科目分數級距分布'][z]
                            d=int(a)
                            c=c+d  
                        g.write(str(int(100*round((jsonData[i]['母體人數']-(c+1))/jsonData[i]['母體人數'],2))))

                    
                g.write("</td></tr>")
                g.write(" </table>")
    
            else:
                g.write("none")
 


