import pandas as pd
import numpy as np

def lesson1(): 
    df_data = {
        'col1' : np.random.rand(5),
        'col2' : np.random.rand(5),
        'col3' : np.random.rand(5),
        'col4' : np.random.rand(5)
    }
    
    df = pd.DataFrame(df_data)
    #print(df)
    #print(df['col1'])
    print(df[['col1', 'col2']][:2])
    
def lesson2():
    tracks = pd.read_excel('Tracks.xls', sheet_name=0)
    #print(tracks)
    #print(tracks.columns)
    print(tracks['Milliseconds'][:5])
    flights = pd.read_csv('flights.csv', index_col=False)
    print(flights)

def lesson3():
    flights = pd.read_csv('flights.csv', index_col=False)
    print(flights.columns)
    #print(flights['DAY_OF_WEEK'])
    #print(flights['ORIGIN'])
    print(flights.iloc[0,0])
    print(flights.iloc[2,1])
    print(flights.iloc[2, flights.columns.get_loc('DAY_OF_MONTH')])
    print(flights.iloc[:3, flights.columns.get_loc('DAY_OF_MONTH')])
    print(flights.iloc[0, [flights.columns.get_loc('ORIGIN'),flights.columns.get_loc('DEST')]])
    
def lesson4():
    flights = pd.read_csv('flights.csv', index_col=False)
    print(flights.sort_values(by=['DISTANCE']))
    print(flights.sort_values(by=['DISTANCE', 'AIR_TIME'], ascending=False))
    
def challenge1():
    flights = pd.read_csv('flights.csv', index_col=False)
    #sort by AIR_TIME and descending order
    print(flights.sort_values(by=['AIR_TIME'], ascending=False))

def lesson5():
    flights = pd.read_csv('flights.csv', index_col=False)
    print(flights[flights['DAY_OF_MONTH'] == 1])
    print(flights[flights['ORIGIN_STATE_NM'] == 'New York'])
    long_flights = flights[flights['DISTANCE'] < 4000]
    print(long_flights['ORIGIN_STATE_NM'] == 'Hawaii')
    
def lesson6():
    #grouping data
    flights = pd.read_csv('flights.csv', index_col=False)
    grouped_data = flights.groupby('DAY_OF_WEEK')
    print(grouped_data['DISTANCE'].mean())

    
def main():
    lesson5()

if __name__ == "__main__":
    main()
    