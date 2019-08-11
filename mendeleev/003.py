from mendeleev import get_table
import pandas as pd

ptable = get_table('elements')

cols = ['atomic_number', 'symbol', 'atomic_radius', 'en_pauling', 'block', 'vdw_radius_mm3']

ptable=ptable[cols].head()

ptable=ptable[cols].describe()


isotopes = get_table('isotopes', index_col='id')

merged = pd.merge(ptable[cols], isotopes, how='outer', on='atomic_number')

