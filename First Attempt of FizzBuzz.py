num = int(input('Type any number here: '))
'''
Виводить "Fizz", якщо число кратне якомусь певному числу (наприклад, 3);
Виводить "Buzz", якщо число кратне іншому певному числу (наприклад, 5);
Виводить "FizzBuzz", якщо число кратне обом цим числам;
В іншому випадку виводить саме число.'
'''

if num%3==0 and num%5==0:
    print('FizzBuzz')
elif num%3==0:
    print('Fizz')
elif num%5==0:
    print('Buzz')
else:
    print(num)