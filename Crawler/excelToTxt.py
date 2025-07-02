import pandas as pd

# 读取 Excel 文件
excel_file = 'LoveLive_视频列表.xlsx'
df = pd.read_excel(excel_file)

# 创建输出文本文件
output_file = 'lovelive_table_rows.txt'

with open(output_file, 'w', encoding='utf-8') as f:
    for _, row in df.iterrows():
        title = str(row[0]).strip()
        date = str(row[1]).strip()
        group = str(row[2]).strip()
        
        html_row = f"""<tr>
  <td>{title}</td>
  <td>{date}</td>
  <td>{group}</td>
</tr>
"""
        f.write(html_row)

print(f"✅ 成功生成 HTML 表格行，并保存为：{output_file}")
