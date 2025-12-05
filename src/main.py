from .scraper import DataScraper
from .processor import DataProcessor
from .excel_writer import ExcelWriter
from .logger_config import logger

def main():

    logger.info("start automating")

    scraper=DataScraper()
    data=scraper.get_table_data()
    writer=ExcelWriter()
    writer.save_employee_data(data)

    processor=DataProcessor(data)
    avg_salary=processor.calculate_average_salary()

    writer.save_avg_salary(avg_salary)

    exp_df=processor.calculate_work_experience()
    writer.save_work_experience(exp_df)

    logger.info("program finished")
