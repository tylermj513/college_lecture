import os
import re
import shutil

def remove_special_characters(input_string): 
    pattern = r'[\\/:*?"<>|]'
    cleaned_string = re.sub(pattern, '', input_string)
    return cleaned_string

file_path = 'dep.txt'   

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    int=0
    for line in lines: 
        folder_name = line.strip()
        cleaned_string = remove_special_characters(folder_name) 

        if not os.path.exists(cleaned_string):
            os.makedirs(cleaned_string)     
              
             

        folder_path = '040'

        if os.path.exists(folder_path) and os.path.isdir(folder_path): 
            items = os.listdir(folder_path)
            folder_names = [item for item in items if os.path.isdir(os.path.join(folder_path, item))]
             
           

            source_folder = folder_names[int][3:]
            destination_folder = os.path.join(cleaned_string, folder_names[int][3:] )
            shutil.copytree(source_folder, destination_folder)


            source = '首頁.css'
            destination = cleaned_string+'/首頁.css'
             
            shutil.copy(source, destination)
            
            
            source2 = 'index'+ folder_names[int][3:]+'.html'
            destination2= cleaned_string+'/index'+ folder_names[int][3:]+'.html'
  
            shutil.copy(source2, destination2)

 
            source3 = '040/' + folder_names[int]
            destination3 = cleaned_string + '/040/'  + folder_names[int]

            
            shutil.copytree(source3, destination3)

            source4 = '040_grade6/' + folder_names[int]
            destination4 = cleaned_string + '/040_grade6/'  + folder_names[int]

            
            shutil.copytree(source4, destination4)

            print(cleaned_string)
        int=int+1
