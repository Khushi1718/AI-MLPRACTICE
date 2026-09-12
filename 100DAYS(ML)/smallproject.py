# 0 = preprocess +eda+feature selction 
# 1- extract input output
# 2 = 2scale the values
# 3= train test split
#4 train the model
#5 evaulate 
#deploy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
df = pd.read_csv("100DAYS(ML)/placement.csv")
print(df.head())

print(df.info())
df= df.iloc[:,1:1]

plt.scatter(df[internships],df[placement])
plt.xlabel('Internships')
plt.ylabel('Placement')
plt.title('Placement vs Internships')
plt.show()

x = df.iloc[:0,0:2]
y = df.iloc[:,-1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
