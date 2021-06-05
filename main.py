import csv
import pandas as pd
import plotly.graph_objects as go
# to find out the average of the performance in each level by students
df = pd.read_csv("data.csv")
#print(df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(x=df.groupby("level")["attempt"].mean(),
                       y=['Level 1', 'Level 2', 'Level 3', 'Level 4'],
                       orientation = 'h'))
#fig.show()


# to find the performance analysis of TRL_987
student_df = df.loc[df['student_id'] == "TRL_987"]
print(student_df)
print(student_df.groupby("level")["attempt"].mean())

fig1=go.Figure(go.Bar(x=student_df.groupby("level")["attempt"].mean(),y=['Level 1','Level 2', 'Level 3','Level 4'],orientation="h"))
fig1.show()