import pandas as pd

df = pd.read_excel(r"C:\Users\Administrator.DESKTOP-74UB6TU\Jupyter notebook\test.xlsx",
                   sheet_name = 'Sheet2', index_col = 0, header = 0)

print(df["编号"].dtype)
print(df["性别"].dtype)
print(df["年龄"].dtype)
print(df["年龄"].astype("float"))
print(df["注册时间"].dtype)
