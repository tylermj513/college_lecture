css_content = '''
table,
td {
    border: 1px solid #333;
    font-size: 25px;
    text-align: center;
    letter-spacing: 2px;
    margin-left: auto; 
    margin-right: auto;
    overflow-wrap: break-word;
}
th {
    font-size: 30px;
}
thead,
tfoot {
    background-color: #333;
    color: #fff;
}
'''

css_file_path = '首頁.css'  # 請替換為您想要儲存CSS檔案的路徑

# 創建並寫入CSS內容到檔案
with open(css_file_path, 'w') as css_file:
    css_file.write(css_content)

print(f"已生成CSS檔案: {css_file_path}")
