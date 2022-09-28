Basic Python
1. Split this string
s = "Hi there Sathiyamoorthy!"
s="hi there Sathiyamoorthy!"
a=s.split()
print(a);
['hi', 'there', 'sathiyamoorthy']
2. Use .format() to print the following string.
Output should be: The diameter of Earth is 12742 kilometers.
planet = "Earth"
diameter = 12742
planet = "Earth"
diameter = 12742
print( 'The diameter of {} is {} kilometers.' .format(planet,diameter));
The diameter of Earth is 12742 kilometers.
3. In this nest dictionary grab the word "hello"
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d={'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d={'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]["tricky"][3]['target'][3])
hello
Numpy
import numpy as np
4.1 Create an array of 10 zeros?
4.2 Create an array of 10 fives?
import numpy as np
array=np.zeros(10)*2
print("an array of 10 zero")
print(array)
an array of 10 zero
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
import numpy as np
array=np.ones(10)*5
print("an array of 10 five")
print(array)
an array of 10 five
[5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
5. Create an array of all the even integers from 20 to 35
import numpy as np
array=np.arange(20,35,2)
print("Array of all the even integers from 30 to 70")
print(array) 
Array of all the even integers from 30 to 70
[20 22 24 26 28 30 32 34]
6. Create a 3x3 matrix with values ranging from 0 to 8
import numpy as np
x=np.arange(0, 9).reshape(3,3)
print(x)
[[0 1 2]
 [3 4 5]
 [6 7 8]]
7. Concatinate a and b
a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
import numpy as np
a=np.array([1,2,3])
b=np.array ([4,5,6])
c=np.concatenate((a,b))
print(c)
[1 2 3 4 5 6]
Pandas
8. Create a dataframe with 3 rows and 2 columns
import pandas as pd
import pandas as pd   
data = {'Name': ['Balaji', 'Roshan', 'Suresh'], 'Age': [20, 21, 19]} 
df = pd.DataFrame(data)    
print(df)  
     Name  Age
0   Balaji   20
1   Roshan   21
2   Suresh   19
9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023
import pandas as pd
pd.date_range(start="2023-01-01",end="2023-02-10")
       
DatetimeIndex(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04',
               '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08',
               '2023-01-09', '2023-01-10', '2023-01-11', '2023-01-12',
               '2023-01-13', '2023-01-14', '2023-01-15', '2023-01-16',
               '2023-01-17', '2023-01-18', '2023-01-19', '2023-01-20',
               '2023-01-21', '2023-01-22', '2023-01-23', '2023-01-24',
               '2023-01-25', '2023-01-26', '2023-01-27', '2023-01-28',
               '2023-01-29', '2023-01-30', '2023-01-31', '2023-02-01',
               '2023-02-02', '2023-02-03', '2023-02-04', '2023-02-05',
               '2023-02-06', '2023-02-07', '2023-02-08', '2023-02-09',
               '2023-02-10'],
              dtype='datetime64[ns]', freq='D')
10. Create 2D list to DataFrame
lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]

lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
df = pd.DataFrame(lists, columns =['Fname', 'Lname', 'Age']) 
print(df) 
   Fname Lname     Age
0      1   Balaji   22
1      2   Roshan   25
2      3   Suresh   24
