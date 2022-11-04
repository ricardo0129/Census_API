import requests
import pandas as pd

def saveFile(outfile,popdata,format):
    df = pd.DataFrame(popdata)
    if format=='csv':
        df.to_csv(outfile, sep=',', index=False, header=False)
    else:
        df.to_excel(outfile)


def query(year='2019',scope='state',scope_value='*',state=None,outfile=None,format='csv'):
    data_source='pep'
    cols='NAME,POP'
    dname='population'

    #keyfile='census_key.txt' key not needed unless you reach daily limit
    #with open(keyfile) as key:
    #    api_key=key.read().strip()

    base_url = f'https://api.census.gov/data/{year}/{data_source}/{dname}'


    data_url = f'{base_url}?get={cols}&for={scope}:{scope_value}'

    if state:
        data_url+=f'&in=state:{state}'

    #data_url+=f'&key={api_key}'

    response=requests.get(data_url)
    popdata=response.json()

    for records in popdata:
        print(records)

    if outfile:
        saveFile(outfile,popdata,format)
        
'''
scope can be 'region,state,county,or place' 
scope_value can be a specific value of that scope or wildcard *

if you want to search inside the scope you can modify the state value
eg. you want to see all the counties in Florida
'''
#query(scope='region',outfile="output_data.csv",format='csv')  #show region population and save results in csv format


query(scope='state') #  show population by state
#query(scope='state',scope_value='12')  only show population of one state



#query(scope='county') show all counties
#query(scope='county', state='12') show all counties in florida 

#query(scope='place',scope_value='00124', state='01')   show population of Abbevile city Alabama
#query(scope='place',scope_value='*',state='12') show all populations of cities in Florida
