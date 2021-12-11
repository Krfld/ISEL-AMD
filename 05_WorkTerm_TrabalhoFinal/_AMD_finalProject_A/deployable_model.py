'''
Using the file a01_dataset_analysis.py,
the 1R result says that the feature to be considered is 'isAstigmatic'
'''


def model1R(age, tearRate, isMyope, isAstigmatic, isHypermetrope):
    lenses = 'none' if isAstigmatic == 'false' else 'hard'
    if lenses == 'none':
        print('The patient doesn\'t need to wear lenses')
    else:
        print(f'The patient needs to wear {lenses} lenses')


if __name__ == '__main__':
    validInput = False
    while not validInput:
        age = input('Patient age (young | presbyopic | pre-presbyopic):')
        if age != 'young' and age != 'presbyopic' and age != 'pre-presbyopic':
            print('Invalid age')
            validInput = False
        else:
            validInput = True

    validInput = False
    while not validInput:
        tearRate = input('Patient tear-rate (normal | reduced):')
        if tearRate != 'normal' and tearRate != 'reduced':
            print('Invalid tearRate')
            validInput = False
        else:
            validInput = True

    validInput = False
    while not validInput:
        isMyope = input('Patient isMyope (true | false):')
        if isMyope != 'true' and isMyope != 'false':
            print('Invalid isMyope')
            validInput = False
        else:
            validInput = True

    validInput = False
    while not validInput:
        isAstigmatic = input('Patient isAstigmatic (true | false):')
        if isAstigmatic != 'true' and isAstigmatic != 'false':
            print('Invalid isAstigmatic')
            validInput = False
        else:
            validInput = True

    validInput = False
    while not validInput:
        isHypermetrope = input('Patient isHypermetrope (true | false):')
        if isHypermetrope != 'true' and isHypermetrope != 'false':
            print('Invalid isHypermetrope')
            validInput = False
        else:
            validInput = True

    print()
    model1R(age, tearRate, isMyope, isAstigmatic, isHypermetrope)
