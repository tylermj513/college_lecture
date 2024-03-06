import os
 
folder_prefix = ""
with open('dep.txt', 'r',encoding="utf-8-sig") as file:
    # 读取文件内容并移除换行符
    lines = file.read().splitlines()

# 将内容存储为列表
dep_list = lines 
for i in range(len(dep_list)):  
    print(dep_list[i])
B=[]

folder = '040'
sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
for num in range(0, len(sub_folders)):
    B.append(sub_folders[num][3:])  

num_folders=len(B)

for i in range(num_folders): 
    folder_name = B[i]   
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"成功")
    else:
        print(f"已存在")
