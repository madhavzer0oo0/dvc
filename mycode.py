import os 
import pandas as pd 

data={
    'name':['Alice','Bob','Charlie'],
    'age':[25, 30, 35],
    'city':['New York', 'Los Angeles', 'Chicago']
}
df=pd.DataFrame(data)
path=os.path.join('data','mydata.csv')
df.to_csv(path, index=False)