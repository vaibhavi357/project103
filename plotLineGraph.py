#pip install pandas
#pip install plotly_express
import pandas as pd
import plotly.express as px
#read line_chart.csv using pandas ans store it in df
df = pd.read_csv("line_chart.csv")
#create a line graph using plotly express and store it in fig
fig = px.line(df, x = "Year", y = "Per capita income", color="Country", title="Per Capita Income for a Country")
#display the graph
fig.show()