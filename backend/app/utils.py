import pandas as pd
from typing import List, Dict


def load_dataset_csv(path: str) -> List[Dict]:
df = pd.read_csv(path)
# normalize columns that can be lists
for col in ['categories','images']:
if col in df.columns:
df[col] = df[col].apply(lambda x: eval(x) if isinstance(x,str) and x.startswith('[') else ([x] if pd.notna(x) else []))
# enforce required columns
required = ['uniq_id','title','brand','description','price','categories','images','manufacturer','package dimensions','country_of_origin','material','color']
for col in required:
if col not in df.columns:
df[col] = None
return df.to_dict(orient='records')
