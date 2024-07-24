elif b is True:
print("b is True")
elif a == 0 and b is True:
    print("a is negative and b is True")
else:
     print("None of the conditions above hold")

work_hour=input('what is your input hours?')
f=int (work_hour)
normal_rate=51.45
extre_rate=88.9
if f <= 35:
           weekly_pay=f*normal_rate
           print(f'your weekly pay is {weekly_pay}')
else:
     weekly_pay=(f-35)*extre_rate+35*normal_rate
     print(f'your weekly pay is {weekly_pay}')

name = input('Who are you?') 
print('Welcome to the class,', name)

hours = int(input('Enter number of hours you worked this week: '))

normal_rate = 51.45
extre_rate= 88.9
hours_entered = 35

if hours > hours_entered:
pay = (hours_entered * normal_rate) + ((hours - hours_entered) * overload_rate)
else:
pay = hours * normal_rate
print(f'This weekly payment of Yingfan Xu is: {pay}')


# exercise 2

numbers= [-2, 3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15, 10]
temp_largest=numbers[0]

for number in numbers:
    if number>temp_largest:
             temp_largest=number
print(f'The largest value is: {temp_largest}')


# exercise 3

for i in range(1, 4):
  for j in range(1, 4):
      if i <= j:
        print(i, j)