import sys
sys.path.append('''E:\lectures\python\programs\module_example\ecommerce1''')
import converters
from converters import lbs_to_kg
# from ecommerce import shipping
import shipping
import openpyxl as xl
wb = xl.load_workbook('transactions.xlsx')

print(converters.kg_to_lbs(24))



