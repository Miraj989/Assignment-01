

ch = 'y'
sum = 0
while ch.lower() == "y":
    num = float(input('enter any number'))
    ch = input("do you want to continue: (y/n)")
    sum+=num
print('sum of all number', sum)