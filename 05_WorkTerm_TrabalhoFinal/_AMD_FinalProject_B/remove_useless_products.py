from ast import For
import pandas as pd

ignoreProducts = ['home', 'open', '/customer/', 'display.category*homepage']

if __name__ == '__main__':
    df = pd.read_csv('z_dataset_JAN_updated.csv')
    out = pd.DataFrame(columns=df.columns)
    for row in df.values:
        if not str(row[4]) in ignoreProducts:
            out = out.append([row], ignore_index=True)

    # print(out)
    out.to_csv('z_dataset_JAN_updated_filtered.csv', index=False)
