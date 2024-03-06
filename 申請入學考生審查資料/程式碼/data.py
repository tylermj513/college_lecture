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




    for a in range(0,len(B)): 
        folder = '040/040'+dep+'/'+B[a] 
        result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(folder) for f in filenames if f.lower().endswith('課程學習成果.pdf')]
        result5 = [os.path.join(dp, f) for dp, dn, filenames in os.walk(folder) for f in filenames if f.lower().endswith('多元表現綜整心得.pdf')]
        result2 = [os.path.join( f) for dp, dn, filenames in os.walk(folder) for f in filenames if f.lower().endswith('.pdf')]
        result3 = [os.path.join(dp,  f) for dp, dn, filenames in os.walk(folder) for f in filenames if f.lower().endswith('課程學習成果.json')]
        result4 = [os.path.join(dp, f) for dp, dn, filenames in os.walk(folder) for f in filenames if f.lower().endswith('多元表現.json')] 

    
        with open(dep+'/'+'data'+B[a]+'.txt', 'w', encoding='utf-8-sig') as g:
            def get_from_json(jdata: dict, *keys):
                try:
                    data = jdata[keys[0]]
                except KeyError:
                    return None
                if len(keys) > 1:
                    return get_from_json(data, *keys[1:])
                return data

            if(len(result5)==1 and len(result4)==0   ):
                g.write(" <table>        <thead>            <tr>   <th colspan="+'"'+str(len(result2))+'"'+">課程學習成果暨多元表現</th>    </tr>        </thead>        <tbody>            <tr>")
                for i in range(0,len(result2)):  
                    g.write("<td>"+result2[i]+"</td>")     
                g.write("</tr><tr>")
                for i in range(0,len(result2)):  
                    g.write( "<td><button onclick="+'"'+"window.location.href='"+"../040/040"+dep +"/"+B[a]+"/" +result2[i]    +"'"+'"'+">"+  "檢視</button></td>")
                g.write("</tr>        </tbody>    </table>") 

            elif(len(result)==1):
                g.write(" <table>        <thead>            <tr>   <th colspan="+'"'+str(len(result2))+'"'+">課程學習成果暨多元表現</th>    </tr>        </thead>        <tbody>            <tr>")
                for i in range(0,len(result2)):  
                    g.write("<td>"+result2[i]+"</td>")     
                g.write("</tr><tr>")
                for i in range(0,len(result2)):  
                    g.write( "<td><button onclick="+'"'+"window.location.href='"+"../040/040"+dep +"/"+B[a]+"/" +result2[i]    +"'"+'"'+">"+  "檢視</button></td>")
                g.write("</tr>        </tbody>    </table>") 


            if len(result3) > 0:
                jsonpath = Path(result3[0])
                print(jsonpath)
                with jsonpath.open('r', encoding='utf-8-sig') as dat_f:
                    data = json.loads(dat_f.read())
                    json_str = json.dumps(data)
                    resp = json.loads(json_str)

                g.write("<table>        <thead>            <tr>                <th colspan='"+str(10)+"'"+">課程學習成果</th>            </tr>        </thead>        <tbody> <tr>                <td>科目名稱</td>                <td>實際修課學年度</td>                <td>實際修課學期</td>  <td>課程學習成果簡述</td>                <td>課程學習成果文件檔案連結</td>            </tr>")
                for i in range(0, len(resp)):  
                    g.write("<tr><td>")
                    g.write(data[i]['科目名稱'])
                    g.write("</td><td>")
                    g.write(str(data[i]['實際修課學年度']))
                    g.write("</td><td>")
                    g.write(str(data[i]['實際修課學期']))
                    g.write("</td><td>")
                    g.write(data[i]['課程學習成果簡述'])
                    g.write("</td><td>")
                    g.write("<a href="+'"'+".."+"/040/040"+dep +"/"+B[a]+"/"+data[i]['課程學習成果文件檔案連結']+'"'+">檢視</a>")
                    g.write("</td></tr>")
                g.write("</tbody>    </table> ")
            

            







            if(len(result4)==1):
                
                jsonpath2 = Path(result4[0])

                with jsonpath2.open('r', encoding='utf-8-sig') as dat_f:
                    data = json.loads(dat_f.read())
                    json_str = json.dumps(data)
                    resp2 = json.loads(json_str)

                    data = data["校方建立幹部經歷紀錄"]
                if(len(data)>0):
                    g.write("<br></br> <table><thead><tr><th colspan="+'"'+str(10)+'"'+">校方建立幹部經歷紀錄</th></tr></thead><tbody><tr><td>單位名稱</td><td>開始日期</td><td>結束日期</td><td>擔任職務名稱</td></tr>")
                    for i in range(0, len(data)):    
                        g.write(" <tr><td>")   
                        g.write(data[i]['單位名稱'])
                    
                        g.write("</td><td>")
                        g.write(data[i]['開始日期'])
                        g.write("</td><td>")
                        g.write(data[i]['結束日期'])
                        g.write("</td><td>")
                        g.write(data[i]['擔任職務名稱'])      
                    
                        g.write("</td></tr> ")

                    g.write("</tbody>    </table> ")













                jsonpath2 = Path(result4[0])

                with jsonpath2.open('r', encoding='utf-8-sig') as dat_f:
                    data = json.loads(dat_f.read())
                    json_str = json.dumps(data)
                    resp2 = json.loads(json_str)

                    data = data["幹部經歷暨事蹟紀錄"]
                if( len(data)>0):
                    g.write("<br></br> <table><thead><tr><th colspan="+'"'+str(10)+'"'+">幹部經歷暨事蹟紀錄</th></tr></thead><tbody><tr>        <td>單位名稱</td>                <td>開始日期</td><td>結束日期</td>                <td>擔任職務名稱</td><td>內容簡述</td>                <td>證明文件連結</td></tr>")
                    for i in range(0, len(data)):    
                        g.write("<tr><td>")    
                        g.write(data[i]['單位名稱'])
                    
                        g.write("</td><td>")
                        g.write(data[i]['開始日期'])
                        g.write("</td><td>")
                        g.write(data[i]['結束日期'])
                        g.write("</td><td>")
                        g.write(data[i]['擔任職務名稱'])
                        g.write("</td><td>")
                        g.write(data[i]['內容簡述'])
                        g.write("</td><td>")
                        g.write("<a href="+'"'+".."+"/040/040"+dep +"/"+B[a]+"/"+data[i]['證明文件連結']+'"'+">檢視</a>")
                    
                        g.write("</td></tr> ")

                    g.write("</tbody>    </table> ")














                jsonpath2 = Path(result4[0])

                with jsonpath2.open('r', encoding='utf-8-sig') as dat_f:
                    data = json.loads(dat_f.read())
                    json_str = json.dumps(data)
                    resp2 = json.loads(json_str)

                    data = data["競賽參與紀錄"]
                if(len(data)>0):
                    g.write(" <br></br> <table>        <thead>            <tr>                <th colspan="+'"'+str(10)+'"'+">競賽參與紀錄</th>    </tr>        </thead>        <tbody>            <tr>                <td>競賽名稱</td>                <td>競賽獎項</td><td>結果公布日期</td>                <td>項目</td>  <td>內容簡述</td>                <td>證明文件連結</td> </tr>")
                    for i in range(0, len(data)):    
                        g.write("<tr><td>")    
                        g.write(data[i]['競賽名稱'])
                    
                        g.write("</td><td>")
                        g.write(data[i]['競賽獎項'])
                        g.write("</td><td>")
                        g.write(data[i]['結果公布日期'])
                        g.write("</td><td>")
                        g.write(data[i]['項目'])
                        g.write("</td><td>")
                        g.write(data[i]['內容簡述'])
                        g.write("</td><td>")
                        g.write("<a href="+'"'+".."+"/040/040"+dep +"/"+B[a]+"/"+data[i]['證明文件連結']+'"'+">檢視</a>")
                        g.write("</td></tr> ")      


                    g.write("</tbody>    </table> ")


                











                    
                jsonpath2 = Path(result4[0])

                with jsonpath2.open('r', encoding='utf-8-sig') as dat_f:
                    data = json.loads(dat_f.read())
                    json_str = json.dumps(data)
                    resp2 = json.loads(json_str)

                    data = data["檢定證照紀錄"]
                if( len(data)>0):
                    g.write(" <br></br> <table>        <thead>            <tr>                <th colspan="+'"'+str(10)+'"'+">檢定證照紀錄</th>            </tr>        </thead>        <tbody>            <tr>                <td>證照區域</td>                <td>證照類別</td>                <td>證照名稱</td>                <td>取得證照日期</td>                <td>分項結果</td>                 <td>證明文件連結</td>            </tr>")
                    for i in range(0, len(data)):    
                        g.write("<tr><td>")    
                        g.write(data[i]['證照資訊']['證照區域'])
                        g.write("</td><td>")
                        g.write(data[i]['證照資訊']['證照類別'])
                        g.write("</td><td>")
                        g.write(data[i]['證照資訊']['證照名稱'])
                        g.write("</td><td>")
                        g.write(data[i]['取得證照日期'])
                        g.write("</td><td>")
                        g.write(data[i]['分項結果'])
                        g.write("</td><td>")
                        g.write("<a href="+'"'+".."+"/040/040"+dep +"/"+B[a]+"/"+data[i]['證明文件連結']+'"'+">檢視</a>")
                        g.write("</td></tr> ")     

                    g.write("</tbody>    </table> ")
                    
                jsonpath2 = Path(result4[0])

                with jsonpath2.open('r', encoding='utf-8-sig') as dat_f:
                    data = json.loads(dat_f.read())
                    json_str = json.dumps(data)
                    resp2 = json.loads(json_str)

                    data = data["服務學習紀錄"]
                if( len(data)>0):
                    
                    g.write(" <br></br> <table>        <thead>            <tr>                <th colspan="+'"'+str(10)+'"'+">服務學習紀錄</th>            </tr>        </thead>        <tbody>            <tr>                <td>服務名稱</td>                <td>服務單位名稱</td>                <td>開始日期</td>                <td>結束日期</td>                <td>服務學習時數</td>                <td>內容簡述</td>                 <td>證明文件連結</td>            </tr>")
                    for i in range(0, len(data)):    
                        g.write("<tr><td>")    
                        g.write(data[i]['服務名稱'])
                        g.write("</td><td>")
                        g.write(data[i]['服務單位名稱'])
                        g.write("</td><td>")
                        g.write(data[i]['開始日期'])
                        g.write("</td><td>")
                        g.write(data[i]['結束日期'])
                        g.write("</td><td>")
                        g.write(str(data[i]['服務學習時數']))
                        g.write("</td><td>")
                        g.write(data[i]['內容簡述'])
                        g.write("</td><td>")
                        g.write("<a href="+'"'+".."+"/040/040"+dep +"/"+B[a]+"/"+data[i]['證明文件連結']+'"'+">檢視</a>")
                        g.write("</td></tr> ")     
                        
                    g.write("</tbody>    </table> ")


                with jsonpath2.open('r', encoding='utf-8-sig') as dat_f:
                    data = json.loads(dat_f.read())
                    json_str = json.dumps(data)
                    resp2 = json.loads(json_str)

                    data = data["彈性學習時間紀錄"]
                if( len(data)>0):
                    g.write(" <br></br> <table>        <thead>            <tr>                <th colspan="+'"'+str(10)+'"'+">彈性學習時間紀錄</th>            </tr>        </thead>        <tbody>            <tr>                  <td>學年度</td>                <td>學期</td>                <td>彈性學習時間類別代碼</td>                <td>內容_開設名稱</td>                <td>開設單位</td>                <td>每週節數</td>                <td>開設週數</td>                <td>內容簡述</td>                <td>證明文件連結</td>             </tr>")

                    for i in range(0, len(data)):    
                        g.write("<tr><td>")    
                        g.write(str(str(data[i]['學年度'])))
                        g.write("</td><td>")
                        g.write(str(str(data[i]['學期'])))
                        g.write("</td><td>")
                        g.write(str(data[i]['彈性學習時間類別代碼']))
                        g.write("</td><td>")
                        g.write(data[i]['內容_開設名稱'])
                        g.write("</td><td>")
                        g.write(data[i]['開設單位'])
                        g.write("</td><td>")
                        g.write(str(data[i]['每週節數']) )
                        g.write("</td><td>")
                        g.write(str(data[i]['開設週數']))
                        g.write("</td><td>")  
                        g.write(data[i]['內容簡述'])
                        g.write("</td><td>")
                        g.write("<a href="+'"'+".."+"/040/040"+dep +"/"+B[a]+"/"+data[i]['證明文件連結']+'"'+">檢視</a>")
                        g.write("</td></tr> ")     

                    g.write("</tbody>    </table> ")

                
                with jsonpath2.open('r', encoding='utf-8-sig') as dat_f:
                    data = json.loads(dat_f.read())
                    json_str = json.dumps(data)
                    resp2 = json.loads(json_str)

                    data = data["職場學習紀錄"]
                if( len(data)>0):
                    
                    g.write(" <br></br> <table>        <thead>            <tr>                <th colspan="+'"'+str(10)+'"'+">職場學習紀錄</th>            </tr>        </thead>        <tbody>            <tr>                <td>職場學習類別代碼</td>       <td>職場學習單位</td>     <td>開始日期</td>    <td>結束日期</td>    <td>時數</td>    <td>內容簡述</td>   <td>證明文件連結</td>        </tr> ")
                    for i in range(0, len(data)):    
                        g.write("<tr><td>")            
                        g.write(str(data[i]['職場學習類別代碼']))
                        g.write("</td><td>")
                        g.write(data[i]['職場學習單位']) 
                        g.write("</td><td>")
                        g.write(data[i]['開始日期'])
                        g.write("</td><td>")
                        g.write(data[i]['結束日期'])
                        g.write("</td><td>")
                        g.write(str(data[i]['時數']))
                        g.write("</td><td>")  
                        g.write(data[i]['內容簡述'])
                        g.write("</td><td>")
                        g.write("<a href="+'"'+".."+"/040/040"+dep +"/"+B[a]+"/"+data[i]['證明文件連結']+'"'+">檢視</a>")
                        g.write("</td></tr> ")    

                    g.write("</tbody>    </table> ")





                    
                jsonpath2 = Path(result4[0])

                with jsonpath2.open('r', encoding='utf-8-sig') as dat_f:
                    data = json.loads(dat_f.read())
                    json_str = json.dumps(data)
                    resp2 = json.loads(json_str)

                    data = data["作品成果紀錄"]
                if( len(data)>0):
                    g.write(" <br></br> <table>        <thead>            <tr>                <th colspan="+'"'+str(10)+'"'+">作品成果紀錄</th> </tr>        </thead>        <tbody>            <tr>                <td>名稱</td>                <td>作品日期</td>                <td>內容簡述</td>                    <td>作品成果連結</td>            </tr>")
                    for i in range(0, len(data)):    
                        g.write("<tr><td>")    
                        g.write(data[i]['名稱'])
                        g.write("</td><td>")
                        g.write(data[i]['作品日期'])
                        g.write("</td><td>")
                        g.write(data[i]['內容簡述'])  
                        g.write("</td><td>")
                        g.write("<a href="+'"'+".."+"/040/040"+dep +"/"+B[a]+"/"+data[i]['作品成果連結']+'"'+">檢視</a>")
                        g.write("</td></tr> ")     


                    g.write("</tbody>    </table> ")




                with jsonpath2.open('r', encoding='utf-8-sig') as dat_f:
                    data = json.loads(dat_f.read())
                    json_str = json.dumps(data)
                    resp2 = json.loads(json_str)

                    data = data["團體活動時間紀錄"]
                if( len(data)>0):
                    g.write("<br></br> <br></br> <table>        <thead>            <tr>                <th colspan="+'"'+str(10)+'"'+">團體活動時間紀錄</th>            </tr>        </thead>        <tbody>            <tr>                <td>學年度</td>                <td>學期</td>                                <td>團體活動時間類別代碼</td>                <td>辦理單位</td>                <td>團體活動內容名稱</td>                <td>節數或時數</td>                <td>內容簡述</td>                <td>證明文件連結</td>             </tr>")

                    for i in range(0, len(data)):    
                        g.write("<tr><td>")    
                        g.write(str(data[i]['學年度']))
                        g.write("</td><td>")
                        g.write(str(data[i]['學期']))
                        g.write("</td><td>") 
                        g.write(str(data[i]['團體活動時間類別代碼']))
                        g.write("</td><td>")
                        g.write(data[i]['辦理單位'])
                        g.write("</td><td>")
                        g.write(data[i]['團體活動內容名稱']) 
                        g.write("</td><td>")
                        g.write(str(data[i]['節數或時數']))
                        g.write("</td><td>")  
                        g.write(data[i]['內容簡述'])
                        g.write("</td><td>")
                        g.write("<a href="+'"'+".."+"/040/040"+dep +"/"+B[a]+"/"+data[i]['證明文件連結']+'"'+">檢視</a>")
                        g.write("</td></tr> ")    

                    g.write("</tbody>    </table> ")


                        



                with jsonpath2.open('r', encoding='utf-8-sig') as dat_f:
                    data = json.loads(dat_f.read())
                    json_str = json.dumps(data)
                    resp2 = json.loads(json_str)

                    data = data["其他多元表現紀錄"]
                if( len(data)>0):
                    g.write(" <br></br> <table>        <thead>            <tr>                <th colspan="+'"'+str(10)+'"'+">其他多元表現紀錄</th>            </tr>        </thead>        <tbody>            <tr>                <td>名稱</td>                <td>主辦單位</td>                <td>開始日期</td>                <td>結束日期</td>                 <td>內容簡述</td>                <td>證明文件連結</td>    </tr>")

                    for i in range(0, len(data)):    
                        g.write("<tr><td>")    
                        g.write(data[i]['名稱'])
                        g.write("</td><td>")
                        g.write(data[i]['主辦單位'])
                        g.write("</td><td>")
                        g.write(data[i]['開始日期'])
                        g.write("</td><td>")
                        g.write(data[i]['結束日期']) 
                        g.write("</td><td>")
                        g.write(data[i]['內容簡述'])
                        g.write("</td><td>")
                        g.write("<a href="+'"'+".."+"/040/040"+dep +"/"+B[a]+"/"+data[i]['證明文件連結']+'"'+">檢視</a>")
                        g.write("</td></tr> ")    
                    g.write("</tbody>    </table> ")


                        








                with jsonpath2.open('r', encoding='utf-8-sig') as dat_f:
                    data = json.loads(dat_f.read())
                    json_str = json.dumps(data)
                    resp2 = json.loads(json_str)

                    data = data["大學及技專校院先修課程紀錄"]
                if( len(data)>0):
                    g.write(" <br></br> <table>        <thead>            <tr>                <th colspan="+'"'+str(10)+'"'+">大學及技專校院先修課程紀錄</th>            </tr>        </thead>        <tbody>            <tr>     <td>計畫專案</td>                <td>開設單位</td>      <td>課程名稱</td>                         <td>開始日期</td>                <td>結束日期</td>                 <td>內容簡述</td>                <td>證明文件連結</td>             </tr>")
                    
                    for i in range(0, len(data)):    
                        g.write("<tr><td>")      
                        g.write(data[i]['計畫專案'])
                        g.write("</td><td>")
                        g.write(data[i]['開設單位'])
                        g.write("</td><td>")
                        g.write(data[i]['課程名稱'])
                        g.write("</td><td>")
                        g.write(data[i]['開始日期']) 
                        g.write("</td><td>")
                        g.write(data[i]['結束日期']) 
                        g.write("</td><td>")
                        g.write(data[i]['內容簡述'])
                        g.write("</td><td>")
                        g.write("<a href="+'"'+".."+"/040/040"+dep +"/"+B[a]+"/"+data[i]['證明文件連結']+'"'+">檢視</a>")
                        g.write("</td></tr> ")    
    
                    g.write("</tbody>    </table> ")








