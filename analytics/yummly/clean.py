"""
Prepare each line to be consumed as a dict object
"""
import json
import pandas as pd


def parse_json_to_df(fi_name):
    '''
    parse the json file into a list of 
    dict objects
    '''
    a = []
    raw_file = open(fi_name).readlines()
    for l in raw_file:
        a.append(json.loads(l))

    return pd.DataFrame(a)



if __name__ == '__main__':
    df = parse_json_to_df('data/raw-test.json')
    import pdb; pdb.set_trace()
