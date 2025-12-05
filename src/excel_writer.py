import os
from logger_config import logger

class ExcelWriter:
    def save_employee_data(self,df):
        df.to_excel("Reports/Employee_data.xlsx",index=False)
        logger.info("data saved")
    

    def save_avg_salary(self,df):
        df.to_excel("Reports/salary_details.xlsx",index=False)
        logger.info("Work experience report generated")
