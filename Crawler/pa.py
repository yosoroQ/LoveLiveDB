from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl

# 设置 Selenium，无头浏览器
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 打开页面
url = "https://ll-fans.jp/data/videogram"
driver.get(url)
driver.implicitly_wait(5)

# 抓取视频标题
elements = driver.find_elements(By.CSS_SELECTOR, "a.llfans-17h4mhl")
titles = [el.text.strip() for el in elements if el.text.strip()]

# 写入 Excel
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "视频标题"
ws.append(["标题"])

for title in titles:
    ws.append([title])

# 保存文件
wb.save("LoveLive_视频列表.xlsx")
print("已保存到 LoveLive_视频列表.xlsx")

driver.quit()
