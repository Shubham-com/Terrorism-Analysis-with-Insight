#importing the libraries
import pandas as pd
import webbrowser

import dash
import dash_html_components as html
from dash.dependencies import Input, State, Output 



# Global variables
app = dash.Dash()


def load_data():
  dataset_name =(r"D:\Terrorism Analysis Forsk Coding School\global_terror.csv")

  #this line we use to hide some warnings which gives by pandas
  #pd.options.mode.chained_assignment = None
  
  global df
  df = pd.read_csv(dataset_name)
  
  print(df.sample(5))

def open_browser():
  # Open the default web browser
  webbrowser.open_new('http://127.0.0.1:8050/')

def create_app_ui():
  # Create the UI of the Webpage here
  main_layout = html.Div(
  [
  html.H1(id='Main_title',children='Terrorism Analysis with Insights' ),
  html.Button( id='button_close',children='Click to Test',n_clicks=0)
  ]
  )
  
  return main_layout

@app.callback(
    dash.dependencies.Output('Main_title', 'children'),
    [dash.dependencies.Input('button_close', 'n_clicks')]
    )
def update_app_ui(n_clicks):
  print("Value passed when clicked on button close = ", str(n_clicks))
  if (n_clicks > 0):
    return "I do not know : " + str(n_clicks)
  else:
    return "Click to Test"
  

def main():
  load_data()
  
  open_browser()
  
  global app
  app.layout = create_app_ui()
  app.title = "Terrorism Analysis with Insights"
  # go to https://www.favicon.cc/ and download the ico file and store in assets directory 
  app.run_server() # debug=True

  print("This would be executed only after the script is closed")
  df = None
  app = None
  

if __name__ == '__main__':
    main()




