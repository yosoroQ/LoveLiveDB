from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ll-fans.jp/data/videogram")

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.llfans-17h4mhl"))
    )

    # 找所有包含标题和日期的容器，观察页面结构后修改这个选择器
    # 假设标题和日期都在 class=“llfans-item” 的div里（请你根据页面具体结构修改）
    containers = driver.find_elements(By.CSS_SELECTOR, "div.llfans-item")

    data = []
    for container in containers:
        try:
            title_el = container.find_element(By.CSS_SELECTOR, "a.llfans-17h4mhl")
            date_el = container.find_element(By.CSS_SELECTOR, "p.llfans-e127h0")
            title = title_el.text.strip()
            date = date_el.text.strip()
            data.append({"标题": title, "日期": date})
        except:
            # 如果某个container没有标题或日期，跳过
            continue

    df = pd.DataFrame(data)
    df.to_excel("llfans_videogram_corrected.xlsx", index=False)
    print(f"爬取完成，条目数：{len(data)}，数据已写入 llfans_videogram_corrected.xlsx")

finally:
    driver.quit()
