import pandas as pd
import datetime
import dateutil.parser

def get_date_from_str(x):
    return dateutil.parser.parse(x)

def get_day_from_date(x):
    return str(x.date())

def get_year_from_date(x):
    return str(x.date())

def get_time_from_date(x):
    return x.time()

def get_month_from_date(x):
    return x.month


def get_hour_from_date(x):
    return x.time().hour

def get_seconds_int_from_date(x):
    a = str(x.time()).split(':') # split 12:00:00
    return int(a[0]) * 3600 + int(a[1]) * 60 + int(a[2])

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

def apply_month(col):
    return col.apply(lambda row: get_month_from_date(
                                get_date_from_str(
                                    row
                                    )))
def apply_time(col):
    return col.apply(lambda row: get_time_from_date(
                                get_date_from_str(
                                    row
                                    )))

def apply_time_int(col):
    return col.apply(lambda row: get_seconds_int_from_date(
                                get_date_from_str(
                                    row
                                    )))


def clean_sf_crime_data_set(df):
    '''
    Assumes data is from Kaggle 
    '''
    df['Date'] = apply_date(df['Dates'])
    df['Hour'] = apply_hour(df['Dates'])
    df['Month'] = apply_hour(df['Dates'])
    df['Time'] = apply_time(df['Dates'])
    df['Time_int'] = apply_time_int(df['Dates'])

    return df

def read_and_clean_sf_crim_data_set(path):
    return clean_sf_crime_data_set(pd.read_csv(path))


if __name__ == '__main__':
    sf = pd.read_csv('data/train.csv') 
    

