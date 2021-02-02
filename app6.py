
'''
1. Prepare the data for the UI - Country Dropdown, year slider
2. Create the new UI components 
3. Create callbacks
'''


import pandas as pd
import dash   # !pip install dash
import dash_html_components as html
from dash.dependencies import Input, State, Output
import dash_core_components as dcc

import plotly.graph_objects as go
import plotly.express as px


import webbrowser

# Global Variables
app = dash.Dash()  # Creating your object 


def load_data():
    dataset_name =(r"D:\Terrorism Analysis Forsk Coding School\global_terror.csv")
    
    global df
    df = pd.read_csv(dataset_name)
    
    #print(df.sample(5))
    temp_list = sorted(df['country_txt'].unique().tolist())
    #print(temp_list)

    global country_list
    # List comprehension
    country_list = [{"label": str(i), "value": str(i)}  for i in temp_list ]
    #print(country_list)

    global year_list
    year_list = sorted(df['iyear'].unique().tolist())
    #print(year_list)

    global year_dict
    # my slider needs data in dictionary format 
    year_dict = {str(year): str(year) for year in year_list}
    print(year_dict)


    
def open_browser():
    # Opening the Browser
    webbrowser.open_new('http://127.0.0.1:8050/')

def create_app_ui():
    # Heading and a Button 
    main_layout = html.Div(
    [
    html.H1(id='Main_title', children='Terrorism Analysis with Insights'),

    dcc.Dropdown(id='country-dropdown', 
        options = country_list,
        value = 'India'
        ),

    dcc.Graph(id='graph-object'),

    dcc.Slider(
        id='year-slider',
        min=min(year_list),
        max=max(year_list),
        value=min(year_list), # default value of the slider
        marks=year_dict  # this is the interval for slider  
        )
    ]
    ) 
    
    return main_layout


@app.callback(
    dash.dependencies.Output ('graph-object', 'figure'),
    [
    dash.dependencies.Input('country-dropdown', 'value'),
    dash.dependencies.Input('year-slider', 'value')
    ]   
    )
def update_app_ui(country_value,year_value):

    #Industry Best Practice 

    print("Data Type of country value = " , str(type(country_value)))
    print("Data of country value = " , str(country_value))

    print("Data Type of year value = " , str(type(year_value)))
    print("Data of year value = " , str(year_value))
    

    figure = go.Figure()

    return figure


    
def main():
    print("Welcome to the Project Season 3 ")   
    
    load_data()
    open_browser()
    
    global app
    
    app.layout = create_app_ui()  # blank Container Page
    # change the title
    app.title = "Terrorism Analysis with Insights"

    # Change the favicon 
    # https://www.favicon.cc/  upload your icon for your project  download your favicon
    # create a directory assests  and copy your favicon.ico there


    app.run_server()
    
    print("Thanks for using my Project ")
    # Industry Best Practices 
    app = None 
    df = None 

# pl do  not type your code here 

if __name__ == '__main__' :
    main()


'''
style={'background-image': 'url(assets/military.jpeg)'}
'''






