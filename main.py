import pandas as pd
import plotly_express as p_ex

df = pd.read_csv('Copy+of+data+-+data.csv')
print(df)

graph = p_ex.scatter(df, x="date", y="cases", size_max=60,
                     color="country", title="Covid Cases")

graph.show()
