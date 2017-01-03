def get_gender(gender='unknown'):
    if gender is 'm':
        gender = 'male'
    elif gender is 'f':
        gender = 'female'
    print(gender)

get_gender()
get_gender('m')
get_gender('f')
