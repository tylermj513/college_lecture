import os

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
        

        dep = B[i][3:]

        print('       <tr>                <td><a href="' + dep + '/index' + dep + '.html">' + dep_list[i] + '</a></td> </tr>', file=f)
