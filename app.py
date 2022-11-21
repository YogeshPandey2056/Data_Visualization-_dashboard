from dash import dash_table,dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import seaborn as sns

import pandas as pd

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


df = pd.read_csv('boston_corrected.csv')
#print(df.head())
data = df.head(20)
app = dash.Dash(__name__)


df["RAD"]= df["RAD"].astype(str)
fig1 = px.scatter(df, x = df['RAD'], y = df['TAX'], color = df['RAD'],
  #size = "duration", color = "deposit", hover_name = "job",
  log_x = True, size_max = 60)


vals = df['RAD'].value_counts().tolist()
labels = ['24','8','7','6','5','4','3','2','1']

fig2 = px.bar(x = labels, y = vals)

fig3 = px.pie(df, df['CHAS'], color = "CHAS")

fig4 = px.imshow(df.corr())
# fig5 = px.line(df, x=data['LSTAT'], y=data['MEDV'], title='Price of housing with respect to lower status population')

app.layout =html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    children="BOSTON HOUSING PRICE PREDICTION", className="header-title"
                ),
                html.P(
                    children="Welcome to the Boston House Price Prediction"
                             " Dashboard for data vizualization",
                    className="header-description",
                ),
                ],
            className="header",
            
        ),
         dash_table.DataTable(
          id = 'table',
          columns = [{
              "name": i,
              "id": i
            }
            for i in df.columns],
          data = df.head(20)
          .to_dict('records'),
        ),
        html.Div(
          children=[
            html.P(
                    children="This is the Scatter plot showing x-axis=RAD(index of accessibility to radial highways) & y-axis=VAL(count of individual RAD value) ",
                  ),
          dcc.Graph(
            id = 'bubble',
            figure = fig1,
            
          )
        ],className="wrapper"),
        html.Div(
            children=[
              html.P(
                    children="This is the bar graph showing x-axis=RAD(index of accessibility to radial highways) & y-axis=TAX(full-value property-tax rate per $10,000)",
                  ),
              dcc.Graph(
              id = 'bar',
              figure = fig2
            ), 
            ],className="wrapper"
          ),
        html.Div(
          children=[
            html.P(
                    children="This is the pie chart showing percantage of Charles River dummy variable (1 if tract bounds river; 0 otherwise)) ",
                  ),
            dcc.Graph(
            id = 'pie',
            figure = fig3
          ),
          ],className="wrapper"
        ), 
        html.Div(
          children=[
            html.P(
                    children="This is the correlation matrix showing  the correlation coefficients for different variables. "
                    "A correlation coefficient of -1 describes a perfect negative, or inverse, correlation, with values in one series rising as those in the other decline, and vice versa. A coefficient of 1 shows a perfect positive correlation, or a direct relationship. A correlation coefficient of 0 means there is no linear relationship.",
                  ),
             dcc.Graph(
            id = 'correlation_matrix',
            figure = fig4
          )
          ],className="wrapper"
        ),
        #  html.Div(
        #   children=[
        #     html.P(
        #             children="This is the line chart showing the change in price of housing with respect to lower status population",
        #           ),
        #      dcc.Graph(
        #     id = 'Line_graph',
        #     figure = fig5
        #   )
        #   ],className="wrapper"
        # ),
    ])

if __name__ == '__main__':
  app.run_server(debug=True)


