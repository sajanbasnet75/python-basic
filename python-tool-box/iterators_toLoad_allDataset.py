import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('dark_background')
wbi=pd.read_csv('c:/Users/Sajan PC/Desktop/python-basic/wbi.csv',chunksize=1000)
def plot_pop(filename, country_code):
    new_dataframe=pd.DataFrame()
    for chunk in wbi:
        coun_code_ceb=chunk[chunk['CountryCode']==country_code]
        zip_col=zip(coun_code_ceb['Total Population'],coun_code_ceb['Urban population (% of total)'])   
        plot_list=list(zip_col)
    
        coun_code_ceb['Total Urban Population']=[int(i[0]*i[1]*0.01) for i in plot_list]
        new_dataframe=new_dataframe.append(coun_code_ceb)

    new_dataframe.plot(x='Year',y='Total Urban Population',kind='scatter')
    plt.show()
#print(plt.style.available)
plot_pop(wbi,'ARB')

'''
# Define plot_pop()
def plot_pop(filename, country_code):

    # Initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    # Initialize empty DataFrame: data
    data = pd.DataFrame()
    
    # Iterate over each DataFrame chunk
    for df_urb_pop in urb_pop_reader:
        # Check out specific country: df_pop_ceb
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

        # Zip DataFrame columns of interest: pops
        pops = zip(df_pop_ceb['Total Population'],
                    df_pop_ceb['Urban population (% of total)'])

        # Turn zip object into list: pops_list
        pops_list = list(pops)

        # Use list comprehension to create new DataFrame column 'Total Urban Population'
        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1]) for tup in pops_list]
    
        # Append DataFrame chunk to data: data
        data = data.append(df_pop_ceb)

    # Plot urban population data
    data.plot(kind='scatter', x='Year', y='Total Urban Population')
    plt.show()

# Set the filename: fn
fn = 'ind_pop_data.csv'

# Call plot_pop for country code 'CEB'
plot_pop(fn,'CEB')

# Call plot_pop for country code 'ARB'
plot_pop(fn,'CEB')

'''
