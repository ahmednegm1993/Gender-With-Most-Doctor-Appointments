import pandas as pd

df = pd.read_excel(r'E:\\Data_analysis_projects\\Gender With Most Doctor Appointments\\dataset\\Gender With Most Doctor Appointments.xlsx')

df_pivot = df.pivot_table(values='appointmentid', 
                          index=None, 
                          columns='gender', 
                          aggfunc='count')

print(df_pivot)
