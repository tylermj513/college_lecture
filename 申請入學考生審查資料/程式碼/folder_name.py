import os
import json
from pathlib import Path

folder = '040'
sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]

num_folders = len(sub_folders)
x = 0
y = 0

for i in range(len(sub_folders)):
    b = sub_folders[i][3:]
    num_file_path = f"{b}num.txt"
    name_file_path = f"{b}name.txt"

    with open(num_file_path, 'w', encoding='utf-8-sig') as num_file, open(name_file_path, 'w', encoding='utf-8-sig') as name_file:
        folder_path = os.path.join(folder, '040' + str(b))
        sub_folders_in_folder = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]
        
        for sub_folder in sub_folders_in_folder:
            print(sub_folder, end=",", file=num_file)
            x += 1

        result = [
            os.path.join(os.path.join(dp, f))
            for dp, dn, filenames in os.walk(os.path.join('040', '040' + str(b)))
            for f in filenames
            if f.lower().endswith('基本資料.json')
        ]

        result2 = [os.path.basename(f).split('_')[0] for dp, dn, filenames in os.walk(os.path.join('040', '040' + str(b))) for f in filenames if
                   f.lower().endswith('基本資料.json')]
        result3 = [item if item in result2 else 'none' for item in sub_folders_in_folder]

        none_indices = [index for index, value in enumerate(result3) if value == 'none']
        for none_index in none_indices:
            print(f"'none' 在 result3 中的位置是第 {none_index} 個元素")
            result.insert(none_index, 'none')

        for json_file_path in result:
            if json_file_path == 'none':
                print("沒有名字", end=",", file=name_file)
                print("沒有名字", end=",")
            else:
                json_path = Path(json_file_path)
                with json_path.open('r', encoding='utf-8-sig') as json_file:
                    data = json.loads(json_file.read())
                    if '學生中文姓名' in data:
                        student_name = data['學生中文姓名']
                    else:
                        student_name = "沒有名字"
                    
                    print(student_name, end=",", file=name_file)
                    print(student_name, end=",")
                    
            y += 1

print(x)
print(y)
