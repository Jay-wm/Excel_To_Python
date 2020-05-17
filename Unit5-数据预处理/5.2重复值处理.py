import pandas as pd

df = pd.read_excel(r"C:\Users\Administrator.DESKTOP-74UB6TU\Jupyter notebook\test.xlsx",
                   sheet_name='Sheet2', index_col=0, header=0)

print(df.drop_duplicates())
print('\n')
print(df.drop_duplicates(subset="编号"))
print('\n')
print(df.drop_duplicates(subset="编号", keep='last'))