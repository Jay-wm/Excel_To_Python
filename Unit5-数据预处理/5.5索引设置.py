import pandas as pd

df = pd.read_excel(r"C:\Users\Administrator.DESKTOP-74UB6TU\Jupyter notebook\test.xlsx",
                   sheet_name = 'Sheet3')
df.columns = ['编号', '年龄', '性别', '注册时间']
print(df.set_index("年龄"))
print(df.rename(columns= {"年龄": "新年龄"}))
print(df.rename(index= {0: "一", 1: "二"}))

print(df)
