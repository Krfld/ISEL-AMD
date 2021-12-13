from pandas import read_csv, DataFrame, Series


def datasetTransform():
    fileName = './dataset_long_name_ORIGINAL.csv'
    df = read_csv(fileName, dtype=str)
    df = DataFrame(df)
    df = df[:-1]  # Remove last row

    discreteHeader = Series(['discrete' for i in range(len(df.columns))], index=df.columns)
    classHeader = Series(['class'] + [''for i in range(len(df.columns)-1)], index=df.columns)
    header = DataFrame([discreteHeader, classHeader])

    df = header.append(df, ignore_index=True)

    df.to_csv('dataset_long_name_PTS_INPUT.tab', sep='\t', index=False)


if __name__ == '__main__':
    datasetTransform()
