from my_split_and_eval import *


# Get patient information
# _______________
def getPatient():
    validInput = False
    while not validInput:
        age = input('Patient age (young | presbyopic | pre-presbyopic): ')
        if age != 'young' and age != 'presbyopic' and age != 'pre-presbyopic':
            print('Invalid age')
            validInput = False
        else:
            validInput = True

    validInput = False
    while not validInput:
        tearRate = input('Patient tear-rate (normal | reduced): ')
        if tearRate != 'normal' and tearRate != 'reduced':
            print('Invalid tearRate')
            validInput = False
        else:
            validInput = True

    validInput = False
    while not validInput:
        isMyope = input('Patient isMyope (true | false): ')
        if isMyope != 'true' and isMyope != 'false':
            print('Invalid isMyope')
            validInput = False
        else:
            validInput = True

    validInput = False
    while not validInput:
        isAstigmatic = input('Patient isAstigmatic (true | false): ')
        if isAstigmatic != 'true' and isAstigmatic != 'false':
            print('Invalid isAstigmatic')
            validInput = False
        else:
            validInput = True

    validInput = False
    while not validInput:
        isHypermetrope = input('Patient isHypermetrope (true | false): ')
        if isHypermetrope != 'true' and isHypermetrope != 'false':
            print('Invalid isHypermetrope')
            validInput = False
        else:
            validInput = True

    return age, tearRate, isMyope, isAstigmatic, isHypermetrope


# Print result
# ___________________________
def printLenses(lenses=None):
    if lenses == 'none':
        print('The patient does not need to wear lenses')
    else:
        print(f'The patient needs to wear {lenses} lenses')

# _________
# ID3 or NB
# _________


# ___________________________
# lists to define the:
# - train|test split methods
# - classification techniques
# - score metrics
# ___________________________
seed = 5

# ________________________
# train|test split methods
list_func_tt_split = \
    [
        # (holdout, (1.0/3.0, seed)),
        (stratified_holdout, (1.0/3.0, seed)),
        # (repeated_holdout, (1.0/3.0, 2, seed)),
        # (repeated_stratified_holdout, (1.0/3.0, 10, seed)),
        # (fold_split, (3, seed)),
        # (stratified_fold_split, (3, seed)),
        # (repeated_fold_split, (3, 2, seed)),
        # (repeated_stratified_fold_split, (3, 2, seed)),
        # (leave_one_out, ()),
        # (leave_p_out, (2, )),
        # (bootstrap_split_once, (seed, )),
        # (bootstrap_split_repeated, (2, seed))
    ]

# _____________
# score metrics
list_score_metric = \
    [
        (accuracy_score, {}),
        # (precision_score, {"average": "weighted"}),  # macro #micro #weighted
        # (recall_score, {"average": "weighted"}),  # macro #micro #weighted
        # (f1_score, {"average": "weighted"}),  # macro #micro #weighted
        # (cohen_kappa_score, {}),
    ]


def fitClassifier(classifier=None):
    '''
    Fit the dataset return the classifier
    '''

    fileName = "./datasets/fpa_dataset.csv"
    featureName = ['age', 'tearRate', 'isMyope', 'isAstigmatic', 'isHypermetrope', 'prescribedLenses']
    func_datasetLoader = None

    D = load_dataset(fileName, featureName=featureName, func_datasetLoader=func_datasetLoader)
    show_data(D)  # TODO Transform data

    for (f_tt_split, args_tt_split) in list_func_tt_split:
        (X, y, tt_split_indexes) = train_test_split_recipe(D, f_tt_split, *args_tt_split)
        # show_function_name("train_test_split:", f_tt_split)
        # show_train_test_split(X, y, tt_split_indexes, numFirstRows=10)

        for (f_score, keyword_args_score) in list_score_metric:
            score_all = score_recipe(classifier, X, y, tt_split_indexes, f_score, **keyword_args_score)
            # show_function_name("score_method:", f_score)
            # show_score(score_all)

    return classifier


def classifier(age=None, tearRate=None, isMyope=None, isAstigmatic=None, isHypermetrope=None, fittedClassifier=None):
    '''
    Predict the lenses needed for the patient based on the fitted classifier
    '''

    lenses = fittedClassifier.predict([age, tearRate, isMyope, isAstigmatic, isHypermetrope])
    printLenses(lenses)


# 1R
# ________________________________________________________________
def model1R(age=None, tearRate=None, isMyope=None, isAstigmatic=None, isHypermetrope=None):
    '''
    Using the file a01_dataset_analysis.py,
    the 1R result says that the feature to be considered is 'isAstigmatic'
    '''

    lenses = 'none' if isAstigmatic == 'false' else 'hard'
    printLenses(lenses)


# _________
def main():
    classifier = DecisionTreeClassifier()  # GaussianNB() or DecisionTreeClassifier()
    fittedClassifier = fitClassifier(classifier)

    age, tearRate, isMyope, isAstigmatic, isHypermetrope = getPatient()

    print()
    model1R(age, tearRate, isMyope, isAstigmatic, isHypermetrope)
    classifier(age, tearRate, isMyope, isAstigmatic, isHypermetrope, fittedClassifier)


if __name__ == '__main__':
    main()
