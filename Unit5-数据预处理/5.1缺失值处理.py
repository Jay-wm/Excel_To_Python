import pandas as pd

df = pd.read_excel(r"C:\Users\Administrator.DESKTOP-74UB6TU\Jupyter notebook\test.xlsx",
                   sheet_name = 'Sheet2', index_col = 0, header = 0)
print(df)
print('\n')
print(df.info())
print('\n')
print(df.isnull())
print('\n')
print(df.dropna())
print('\n')
print(df.dropna(how = 'all'))
print('\n')
print(df.fillna({"性别": "男", "年龄": "30"}))

