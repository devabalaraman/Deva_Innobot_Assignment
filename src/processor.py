import pandas as pd
from datetime import datetime

class DataProcessor:
    def __init__(self,df):
        self.df=df
    
    def calculate_average_salary(self):
        self.df["Salary"]=self.df["Salary"].replace('[\$,]','',regex=True).astype(float)
        avg_salary_df=self.df.groupby("Position")["Salary"].mean().reset_index()
        avg_salary_df.columns=["Position","Average Salary"]
        return avg_salary_df

    def calculate_work_experience(self):
        self.df["Start Date"]=pd.to_datetime(self.df["Start Date"])
        self.df["Work Experience"]=datetime.now().year - self.df["Start Date"].dt.year()
        self.df.rename(columns={"Office":"Location"},inplace=True)
        return self.df.sort_values(by="Work Experience", ascending=False)