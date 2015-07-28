'''
call this script to munge all data sets
'''
import pandas as pd
import numpy as np
TUBE_ID = 'tube_assembly_id'

def merge_file_name(path, file_name):
    return '%s/%s' % (path , file_name)

def etl(path_to_data):
    '''
    Assumes that the data is from the kaggle competition
    https://www.kaggle.com/c/caterpillar-tube-pricing/data
    and follows this schema
    '''
    df = None

    ######
    # Load up init df
    ######
    df_train = pd.read_csv(
            merge_file_name(path_to_data, 'train_set.csv')
            )
    df_test = pd.read_csv(
            merge_file_name(path_to_data, 'test_set.csv')
            )
    df_tubes = pd.read_csv(
            merge_file_name(path_to_data, 'tube.csv')
            )
    df_components = pd.read_csv(
            merge_file_name(path_to_data, 'components.csv')
            )
    df_tube_end = pd.read_csv(
            merge_file_name(path_to_data, 'tube_end_form.csv')
            )
    df_bom = pd.read_csv(
            merge_file_name(path_to_data, 'bill_of_materials.csv')
            )
    df_specs = pd.read_csv(
            merge_file_name(path_to_data, 'specs.csv')
            )
    df_type_component = pd.read_csv(
            merge_file_name(path_to_data, 'type_component.csv')
            )
    df = pd.merge(
            pd.merge(df_tubes, df_specs, on=TUBE_ID),
            df_bom,
            on=TUBE_ID
            )
    # Join and clean the tube ends
    df = pd.merge(
            df, 
            df_tube_end, 
            left_on='end_a', 
            right_on='end_form_id',
            how='left', # sometimes end_a is null
            )
    df.rename(columns={'forming': 'end_a_forming'}, inplace=True)
    df.drop('end_form_id', axis=1, inplace=True)
    df = pd.merge(
            df, 
            df_tube_end, 
            left_on='end_x', 
            right_on='end_form_id',
            how='left', # sometimes end_x is null
            )
    df.rename(columns={'forming': 'end_x_forming'}, inplace=True)
    df.drop('end_form_id', axis=1, inplace=True)

    # Drop the component lists and spec list so that it's 
    # a column of arrays


    # Join all to train set
    df_train = pd.merge(df, df_train, on=TUBE_ID)
    df_test = pd.merge(df, df_test, on=TUBE_ID)

    feature_extend(df_train)
    feature_extend(df_test)
    return [df_train, df_test]

def get_cols_matching_regex(col_arr, regex):
    m_cols = []
    for col in col_arr:
        if col.find(regex) != -1:
            m_cols.append(col)
    return np.array(m_cols) 

###
# Transformations on the full set
###
def feature_list_count(df, regex, new_col_count):
    cols = df.columns.values

    m_cols = get_cols_matching_regex(cols, regex)
    df[new_col_count] = 0
    for col_name in m_cols:
        if col_name != new_col_count:
            df[new_col_count] += df.apply(\
                    lambda row: 1 if str(row[col_name]) != 'nan' else 0,
                    axis=1
                )
    #return df

def feature_extend(df):
    feature_list_count(df, 'component_', 'component_count')
    feature_list_count(df, 'spec', 'spec_count')
    #return df

if __name__ == '__main__':
    df = etl('competition_data')
    df_ext = feature_extend(df)
    import pdb; pdb.set_trace()
