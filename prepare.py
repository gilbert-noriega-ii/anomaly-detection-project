import pandas as pd

def wrangle_curriculum():
    '''
    This function reads the anonymized curriculum access text 
    file and prepares it for exploration.
    '''
    #read csv
    df = pd.read_csv('anonymized-curriculum-access.txt', sep=" ", header=None)
    #names the columns
    df.columns = ['date', 'time', 'page_viewed', 'user_id', 'cohort_id', 'ip']
    #adds date and time together
    df["datetime"] = df["date"] + ' '+ df["time"]
    #changes datetime column to datetime type
    df['datetime'] = pd.to_datetime(df.datetime)
    #adding year
    df['year'] = df.datetime.dt.year
    #adding month
    df['month'] = df.datetime.dt.month
    #adding day 
    df['day'] = df.datetime.dt.day
    #adding hour
    df['hour'] = df.datetime.dt.hour
    #adding weekday
    df['weekday'] = df.datetime.dt.day_name()
    #changing data type
    df = df.astype(object)
    #setting index
    #df = df.set_index('datetime')
    #dropping duplicate columns
    df.drop(columns=['date', 'time'], inplace = True)
    return df