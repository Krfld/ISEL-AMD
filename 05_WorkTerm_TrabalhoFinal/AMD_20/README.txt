To execute the deployed model, open 'deployable_model.py'.

When executing, you'll be prompt to input the method to use ('1r' or 'id3' or 'nb') and the patient information.

When executing the 1R method, you'll be shown the score metrics of the algorithm.

When executing the ID3 or NB method, you can opt to generate the model, see the score metrics and save the model and the encoder (that will be used to predict the new patient information), or to load the model and encoder generated.

To save the model, in the 'main' function, uncomment the line that calls the 'fitClassifier' function (line 229).
To load only, comment this line.

The model is loaded in the line 232.