#pip install pandas
#pip install plotly_express
import pandas as pd
import plotly.express as px
#read line_chart.csv using pandas ans store it in df
df = pd.read_csv("data.csv")
#create a line graph using plotly express and store it in fig
fig = px.scatter(df, x = "Population", y = "Per capita", size = "Percentage", color="Country", size_max = 60)
#display the graph
fig.show()