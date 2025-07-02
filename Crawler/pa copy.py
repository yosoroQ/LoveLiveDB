from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook

chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://ll-fans.jp/data/videogram")

    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td.llfans-vis03a"))
    )

    td_elements = driver.find_elements(By.CSS_SELECTOR, "td.llfans-vis03a")
    print(f"找到 {len(td_elements)} 个 td.llfans-vis03a 元素")

    dates = []
    for td in td_elements:
        # 先打印 td.innerHTML 看看结构
        # print(td.get_attribute('innerHTML'))

        # 用 find_elements 找匹配的 p 标签，避免找不到抛异常
        p_elements = td.find_elements(By.CSS_SELECTOR, "p")
        date_text = ""
        for p in p_elements:
            text = p.text.strip()
            # 简单用日期格式判断过滤，比如包含“年”字，排除无关文本
            if "年" in text:
                date_text = text
                break
        if not date_text:
            # 如果 p标签没拿到，可以尝试直接用 td.text
            full_text = td.text.strip()
            if "年" in full_text:
                date_text = full_text
        if date_text:
            dates.append([date_text])

    print(f"抓取到 {len(dates)} 条日期数据")

    wb = Workbook()
    ws = wb.active
    ws.title = "日期数据"
    ws.append(["日期"])
    for date in dates:
        ws.append(date)
    wb.save("llfans_videogram_dates.xlsx")
    print("数据已写入 llfans_videogram_dates.xlsx")


finally:
    driver.quit()
