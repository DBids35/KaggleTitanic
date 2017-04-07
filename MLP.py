import pandas as pd
data=pd.read_csv('Data/train.csv')
data=data.drop(['Name', 'Ticket','Cabin', 'Embarked'],1)
sexDict={'male':0, 'female':1}
data['Sex']=data['Sex'].apply(lambda x: sexDict[x])
data['Age'].fillna(data['Age'].mean(), inplace=True)
print(data.head(10))