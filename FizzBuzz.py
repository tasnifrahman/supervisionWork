num = int(input('enter your number : '))
for i in range(num+1):
    if(i%3==0 and i%5==0):
        print('FizzBuzz')
        continue
    elif(i%3==0):
        print('Fizz')
        continue
    elif(i%5==0):
        print('Buzz')
        continue
    else:
        print(i)
