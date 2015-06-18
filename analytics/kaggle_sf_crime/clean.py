import pandas as pd
import datetime

def get_date_from_str(x):
    return datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')

def get_day_from_date(x):
    return str(x.date())

def get_year_from_date(x):
    return str(x.date())



def get_hour_from_date(x):
    return x.time().hour

def apply_date(col):
    return col.apply(lambda row: get_day_from_date(
                                get_date_from_str(
                                    row
                                    )))
def apply_hour(col):
    return col.apply(lambda row: get_hour_from_date(
                                get_date_from_str(
                                    row
                                    )))


if __name__ == '__main__':
    sf = pd.read_csv('data/train.csv') 
    

