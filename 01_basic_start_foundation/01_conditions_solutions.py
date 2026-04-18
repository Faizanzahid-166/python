# condition_1
age = 71

if age < 13:
    print('Child')
elif age < 20:
    print('Teenagers')
elif age < 60:
    print('Adult')
else:
    print('Seniors')

# condition_2
age_year = 8
day = 'wednesday'

price = 12 if age_year  >= 18 else 8

if day == 'wednesday':
    price = price - 2

print("ticket price is $ ", price) 

# condition_3
score = 85

if score >= 101:
    print('verify grade again')
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "fail"

print("Grade:" , grade)

# condition_4



