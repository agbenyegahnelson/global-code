name = input('what is your name?')
age = input('what is your age?')
y = 'years' if int(age) > 1 else 'year'
print('Heello ' + ' ' + ' ' + name + ' ' + '! You are ' + age + ' ' + y + ' old.')
# Message to nelson
if int(age) < 12:
    print('Hello' + ' '+ name + '! You are child' + ' of ' + age )
elif 12 < int(age) < 18 :
    print('Hello' + ' '+ name + '! You are a teenager' + ' ' + 'of' + ' ' + age + ' dont play with men')
else:
    print('Hello' + ' '+ name +'! You are an adult' + ' ' + 'of' + ' ' + age + ' ' + 'behave well')


