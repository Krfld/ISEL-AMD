import numpy as np
import pandas as pd

ignoreProducts = ['home', 'open', '/customer', 'display.category*homepage']

# Removes the rows where product_gui starts with any of the ignoreProducts
if __name__ == '__main__':
    df = pd.read_csv('z_dataset_JAN_updated.csv')
    df = df[df['product_gui'] != '']
    for productToIgnore in ignoreProducts:
        df = df[df['product_gui'].str.startswith(productToIgnore) == False]
    df.to_csv('z_dataset_JAN_updated_filtered.csv', index=False)
