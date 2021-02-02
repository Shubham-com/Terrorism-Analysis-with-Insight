
'''
My AUDIO is MUTED
Will start at 9 PM

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
    
    print(df.sample(5))
    
def open_browser():
    # Opening the Browser
    webbrowser.open_new('http://127.0.0.1:8050/')

def create_app_ui():
    # Heading and a Button 
    main_layout = html.Div(
    [
    html.H1(id='Main_title', children='Terrorism Analysis with Insights'),
    html.Button(id='button_close', children = 'Click to Test', n_clicks=0),
    html.Hr(),
    dcc.Dropdown(id='dropdown-1', 
        options = [{'label':'Bar', 'value':'Bar'},{'label':'Line', 'value':'Line'}],
        value = 'Line'
        ),
    dcc.Graph(id='graph-object')

     
    ]
    ) 
    
    return main_layout

# Event handling Concept
# Decorator
@app.callback(
    dash.dependencies.Output ('button_close', 'children'),
    [
    dash.dependencies.Input('button_close', 'n_clicks')
    ]   
    )
# This is called everytime the application is loaded the first time 
# And each time you click the button
def update_app_ui(n_clicks):
    # Industry Best Practice 
    print("Data Type of n_clicks = ", str(type(n_clicks)))
    print("Value passed is = ", str(n_clicks))

    if (n_clicks > 0):
        return "I clicked = " + str(n_clicks)
    else:
        return 'Click to Test'


# Graph is made out of figure object 
@app.callback(
    dash.dependencies.Output ('graph-object', 'figure'),
    [
    dash.dependencies.Input('dropdown-1', 'value')
    ]   
    )
def update_app_ui(dd_value):
    # Best Practice 
    print("Data type of dd_value  =", str(type(dd_value)))
    print("Value of dd_value  =", str(dd_value)  ) 

    figure = go.Figure()  # way to create a blank figure object 


    if (dd_value == 'Bar'):
        print("I will create a Bar Graph here")
        # what logic i will write here to create Bar Figure
        data = [
        ['mohan', 10], ['ramesh', 15], ['ganesh', 14],['divya', 20], ['rohan',25], ['sita', 18]
        ]

        figure = px.bar(pd.DataFrame(
                        data, 
                        columns = ['Name', 'Age']), 
                        y ='Age',
                        x = 'Name',
                        text='Age',
                        hover_data=['Age','Name'],
                        height=500
                        )


    elif (dd_value == 'Line'):
        print("I will create a Line Graph here")
        # what logic i will write here , create the Line Figure
        data = [
        ['mohan', 10], ['ramesh', 15], ['ganesh', 14],['divya', 20], ['rohan',25], ['sita', 18]
        ]
        figure = go.Figure(data=go.Scatter(
            x=pd.DataFrame(data, columns = ['Name', 'Age'])['Name'], 
            y=pd.DataFrame(data, columns = ['Name', 'Age'])['Age'])
        )


    else:
        print("Nothing is selected from Drop Down")



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






