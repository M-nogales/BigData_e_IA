import pandas as pd
import numpy as np
# create a series
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dw = pd.Series(weekdays,dtype='string')
# print('dw: ', dw)



abc= ['a','b','c','d','e','f','g','h']
nums = pd.Series([0,1,2,3,4,5,6,7], index=abc)
# print('nums: ', nums)

print('nums[a]: ', nums['a'])

print('nums[a,b]: ', nums[['a', 'b']])

print('nums[1:4]: ', nums[1:4])

print('nums[0:7]: ', nums[0:7])

abc1= ['a','b','c','d','e','f','g','h',np.nan]
nums1 = pd.Series([0,1,2,3,4,5,6,7,8], index=abc1)
print('nums1: ', nums1)
print(nums1.dropna())

# tail(), head()
print('nums1.head(3): ', nums1.head(3))
print('nums1.tail(3): ', nums1.tail(3))

# describe()
print('nums1.describe()', nums1.describe())

# sort_values()
print('nums1.sort_values()', nums1.sort_values())
print('nums1.sort_values()', nums1.sort_values(ascending=False))

# Atributos
print('Total de elementos: ', nums1.size)
print('Total de elementos: ', nums1.count())
print('Valores concatenacion/suma: ', nums1.sum())
print('valores maximos', nums1.max())
print('valores minimos', nums1.min())
print('Valores media: ', nums1.mean())
print('Valores mediana: ', nums1.median())

# apply()
print('nums1.apply(lambda x: x*10): ', nums1.apply(lambda x: x*10))


abc2= ['a','b','c','d','e','f','g','h','i','j']
test= [0,1,2,3,4,5,6,7,8, np.nan]
nums2 = pd.Series(test, index=abc2)
# notnull()
print('nums1: ', nums2)
print('nums1.isnull(): ', nums2.isnull())
print('nums1.notnull(): ', nums2.notnull())
# cambiar valores nulos por 0
print(nums2.fillna(0))
# unique()
print('nums2.unique(): ', nums2.unique())

#----------------------------------
asignatures = ['Math', 'History', 'Geography', 'Physics', 'Chemistry']
notes = [8, 7, 6, 9, 10]

grades = pd.Series(notes, asignatures)
print('grades: ', grades)

print('grades.size: ', grades.size)
print('grades.index: ', grades.index)
print('grades["Math"]: ', grades["Math"])
print('grades["Math", "History"]: ', grades[["Math", "History"]])
print('grades[lambda x: x < 5]', grades[lambda x: x > 5])
print('grades[grades.between(5, 8)]', grades[grades.between(5, 8)])
print('grades[grades>5]', grades[grades>5])

#----------------------------------

dict_notes = {'Math': 8, 'History': 7, 'Geography': 6, 'Physics': 9, 'Chemistry': 10}
grades = pd.Series(dict_notes)
print('grades: ', grades)