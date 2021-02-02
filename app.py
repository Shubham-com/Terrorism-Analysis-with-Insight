
'''
My AUDIO is MUTED
Will start at 9 PM

'''


import pandas as pd
import dash   # !pip install dash
import dash_html_components as html
from dash.dependencies import Input, State, Output
import dash_core_components as dcc

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
    # Bar and Line in the dropdown
    dcc.Dropdown(id='dropdown-1', options = [{'label':'Asia', 'value':'Asia'},{'label':'Line', 'value':'Line'}])

    # goto w3schools  learn HTML 
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
def update_app_ui(n_clicks):
    # Industry Best Practice 
    print("Value passed is = ", str(n_clicks))

    if (n_clicks > 0):
        return "I clicked = " + str(n_clicks)
    else:
        return 'Click to Test'




    
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








