"""
> 80    A+
> 70    A
> 60    A-
> 50    B
> 40    C
> 33    D
0-32    F
"""
number = int(input('enter number: '))
if number > 80:
    print('Grage is A+')
elif number > 70:
    print('Grage is A')
elif number > 60:
    print('Grage is A-')
elif number > 50:
    print('Grage is B')
elif number > 40:
    print('Grage is C')
elif number > 33:
    print('Grage is D')
else:
    print('Fail')