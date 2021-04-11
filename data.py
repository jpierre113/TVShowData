import matplotlib.pyplot as pyplot
import pandas as pd

#reads the CSV file using Pandas
df_viewers = pd.read_csv('Software Engineering Programming Exercise.csv')

#sets variable to a dataframe
viewer_frame = pd.DataFrame(df_viewers)

isPB = viewer_frame['Viewer Hometown'] == 'Pittsburgh'
isCL = viewer_frame['Viewer Hometown'] == 'Cleveland'


# plt.bar(x = df_viewers['Program Genre'])