name = input('enter the name: ')
profession = input('enter the profession: ')
birth_year = int(input('enter birth year: '))
country = input('enter the country: ')
gender = input('enter m/f')
age = 2022-int(birth_year)
if gender == 'm':
    pronoun= 'He'
else:
    pronoun= 'She'

text = f'{name} is a {profession} of {country}. {pronoun} is {age} years old.'
print(text)