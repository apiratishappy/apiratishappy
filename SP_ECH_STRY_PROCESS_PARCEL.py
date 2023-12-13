##################################
#### อ่าน json แล้วเก็บเป็น excel ####
##################################
### SP_ECH_STRY_PROCESS_PARCEL ###

import json
import pandas as pd

json_file_path = r'D:\DOL\Transaction\Test66.json'
excel_file_path = r'D:\DOL\Transaction\Test66.xlsx'

with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
df = pd.DataFrame(data["result"])
df = df.astype(str)
df['cd:ProcessOrderSeq'] = df['cd:ProcessOrderSeq'].str.rstrip('.0')
df.to_excel(excel_file_path, index=False)
print(f"Data successfully exported to {excel_file_path}")