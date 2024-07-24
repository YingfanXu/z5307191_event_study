import numpy as np
import pandas as pd

data_array=np.array([[1,4],[2,5],[3,6]])
df_numpy=pd.DataFrame(data_array,index=['c','d','e'],columns=['a','b'])

print(df_numpy)

