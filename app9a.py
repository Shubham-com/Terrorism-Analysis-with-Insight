# Creating Tabs in UI

#importing the libraries
import pandas as pd
import webbrowser
import dash
import dash_html_components as html
import dash_core_components as dcc 

# Global variables
app = dash.Dash()


def load_data():
  dataset_name = "global_terror.csv"
  global df
  df = pd.read_csv(dataset_name)
  

def open_browser():
  # Open the default web browser
  webbrowser.open_new('http://127.0.0.1:8050/')

def create_app_ui():
  # Create the UI of the Webpage here
  main_layout = html.Div([

  html.H1('Terrorism Analysis with Insights', id='Main_title'),
  
  dcc.Tabs(id="Tabs", value="tab-1",children=[
      dcc.Tab(label="Map tool" ,id="Map tool",value="tab-1", children=[
      dcc.Tabs(id = "subtabs", value = "tab-1",children = [
              dcc.Tab(label="World Map tool", id="World", value="tab-1", children = [html.Div()]),
              dcc.Tab(label="India Map tool", id="India", value="tab-2", children =[html.Div()])
              ]
              )]),
      
      dcc.Tab(label = "Chart Tool", id="chart tool", value="Chart", children=[
      dcc.Tabs(id = "subtabs2", value = "tab-2",children = [
              dcc.Tab(label="World Chart tool", id="WorldC", value="tab-3"),
              dcc.Tab(label="India Chart tool", id="IndiaC", value="tab-4")]),
              html.Div()
              ])
      ])
  ])
  return main_layout


def main():
  load_data()
  open_browser()

  global app
  app.layout = create_app_ui()
  app.run_server() # debug=True

  print("This would be executed only after the script is closed")
  df = None
  app = None
  
if __name__ == '__main__':
    main()