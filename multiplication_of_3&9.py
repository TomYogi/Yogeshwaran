# -*- coding: utf-8 -*-
"""multiplication of 3&9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zmhwjswONNJQ3BNJpaQegaqHtTcw7wTj
"""

n=int(input("Enter your range here: "))
m=int(input("Enter the number to divide: "))
print("Numbers in a range of ",n)
for i in range(n): 
  if i%m==0:
    print(i)

"""Program to calculate Electric bill..

"""

def choice():
    # ch=int(input("Enter your choice: "))
    print("1.Commercial Use")
    print("2.Domestic Use")
    # ch=int(input("Enter your choice: "))
choice()

def invalid():
  print("You have Selected the Invalid option")
  print("Select correct option")
  # choice()
  choice()

ch=int(input("Enter your choice: "))

def commercial():
  print("You have Selected the Commercial Use")
  unit=int(input("Number of units:"))
  bill=unit*8.5
  print("Your amount to pay : Rs.", bill)

def domestic():
  print("You have selected the Domestic use")
  unit=int(input("Number of units:"))
  if unit<=100:
    bill=unit*3.46
    print("Your amount to pay : Rs.", bill)
  elif unit>=101 and unit<=300:
    bill=346+((unit-100)*7.43)
    print("Your amount to pay : Rs.", bill)
  elif unit>=301 and unit<=500:
    bill=346+1486+((unit-300)*10.32)
    print("Your amount to pay : Rs.", bill)
  else:
    bill=346+1486+2064((unit-500)*11.71)
    print("Your amount to pay : Rs.", bill)

while ch>=3:
    invalid()
    ch=int(input("Enter your choice: "))

if ch==2:
  domestic()
elif ch==1:
  commercial()

"""Program to Calculate Annual Salary"""

hr_salary=250
extratime_salary=100

hr_work=int(input("Number of hours work per day: "))
extratime_work=int(input("Number of Extra hours worked per month: "))
leave=int(input("Average number of days leaves taken in month: "))

salary_extratime=extratime_work*extratime_salary
salary_perday=hr_work*hr_salary
salary_leave=salary_perday*leave
salary_permonth=salary_perday*30+salary_extratime-salary_leave
salary_annual=salary_permonth*12 

print("\nSalary per day: ",salary_perday)
print("Salary per month: ",salary_permonth)
print("Annual salary: ",salary_annual)

"""Program to calculate the students marksheet"""

n=int(input("Enter the number of students: "))
# print("\nEnter the marks of",student_1)
m=int(input("Enter the number of subject: "))
# exec(f'mark_{p}=0')

for k in range(n):
    print("\n")
    exec(f'cat_{k} = input("Enter the Student Name: ")')
    exec(f'cat_{k} = print(cat_{k}, "marks")')
    for o in range(m):
        exec(f'mark_{o}= int(input("Enter subject Marks: "))')
        # for l in range(f'int(mark_{o})'):
        # d=f'mark_{o}'
    # for d in range(m):
        # d=f'mark_{m--1}'
        # print(d)
    avg=int(d/m)
    count=0
    while(count<m):
      d=f'mark_{m-1}'
      count=count+1
      print(d)

    
        # avg = int(sum(f'mark_{o}.values()')/len(f'mark_{o}')) 

    # totalf'mark_{o}' = 0
    # totalitem=0
    # for m, value in f'mark_{o}'.items():
    #     totalitem += value
    #     totalf'mark_{o}' += value
    #     average = totalf'mark_{o}'/totalitem
    
    # print("Average:",f'mark_{o}')
    
    print("Average: ",avg)
      # exec(f'avg=mark_{o}/m')
      # exec(f'print(avg)')
    # for av in range(m):
    #   sum=num+av
    #   avg=sum/m

# print("\n",name,"\n",fname,"\n",doy,"\n",sts)

import pandas as pd

df=pd.DataFrame({
                  'name':['s','u','d','a','n'],
                  'fname':['su','ud','da','an','ns'],
                  'doy':[1991,2003,2004,2005,2006],
                  'sts':['s','d','s','d','s']})
df['age']=2022-df['doy']
df['fage']=2*df['age']

df['fsts']=df['fage'].map(lambda x:"retired" if x>58 else "rpd")
df['gender']=df['sts'].map(lambda y:"Male" if y=='s' else "Female")
# print(df)
print(df)

from google.colab import drive

# Mount your Drive to the Colab VM.
drive.mount('/drive')

# Write the DataFrame to CSV file.
with open('/drive/My Drive/fo1.csv', 'w') as f:
  df.to_csv(f)
  df = pd.read_csv('data.csv')
  print(df.to_string())

"""1-find the age of student and assign 
2-double the age of child and assign in father's age
3-find the father's age above 58 and assign it as retired if not-rpd
4-convert to csv
"""