from selenium import webdriver
from selenium.webdriver.common.by import By 
import pandas as pd
from logger_config import logger

class DataScrapper:
    def get_table_data(self):
        logger.info("opening browser for web scraping")
        driver=webdriver.Chrome()
        driver.get("https://datatables.net/examples/data_sources/dom.html")

        rows=driver.find_elements(By.XPATH,"//table[@id='example']/tbody/tr")
        table=[]
        for row in rows:
            cols=row.find_elements(By.TAG_NAME,"td")
            table.append([col.text for col in cols])

        driver.quit()
        logger.info("web scraping over")

        df=pd.DataFrame(table,columns=["Name","Position","Office","Age","Startdate", "salary"])
        return df