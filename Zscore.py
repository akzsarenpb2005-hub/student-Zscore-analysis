import pandas as pd
import numpy as np
Student=pd.read_csv('Student.csv')
Student_data=pd.DataFrame(Student)
print(Student_data)
y=0
while y<Student_data['Maths'].count():
    if Student_data.loc[y,'Maths']=='AB':
        Student_data.drop(y,axis=0,inplace=True)
        Student_data.to_csv('Student.csv',index=False)
        Student_data.reset_index(inplace=True)
        
    y=y+1

mh=Student_data['Maths']
arr=mh.to_numpy(dtype=np.int8)
avg=(np.mean(arr))
stdi=(np.std(arr))

x=0
while x<Student_data['Name'].count():
    Student_data.loc[x,'Z score']=(arr[x]-avg)/stdi
    x=x+1


print(Student_data)
Student_data.to_csv('Student.csv',index=False)    