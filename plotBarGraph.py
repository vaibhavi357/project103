#pip install pandas
#pip install plotly_express
import pandas as pd
import plotly.express as px
#read line_chart.csv using pandas ans store it in df
df = pd.read_csv("data.csv")
#create a line graph using plotly express and store it in fig
fig = px.bar(df, x = "Country", y = "InternetUsers")
#display the graph
fig.show()