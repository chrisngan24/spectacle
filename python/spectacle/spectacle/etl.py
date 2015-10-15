import pandas as pd

def encode_categorical_features(df, col):
    '''
    df - the dataframe to manipulate
    col - the categorical column that will be encoded
    '''
    categ_mat = pd.get_dummies(df[col])
    categ_mat.columns = ['encoded_%s_%s' %(col, c) for c in categ_mat.columns.values]

    return df.join(categ_mat)
