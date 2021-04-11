import matplotlib.pyplot as plt
import pandas as pd

#reads the CSV file using Pandas
df_viewers = pd.read_csv('Software Engineering Programming Exercise.csv')

#sets variable to a dataframe
viewer_frame = pd.DataFrame(df_viewers)


#filters based on City
isCity = viewer_frame[(viewer_frame['Viewer Hometown'] == 'Pittsburgh') | (viewer_frame['Viewer Hometown'] == 'Cleveland')]


#gives the sum of viewers based on genre
total = isCity.groupby(['Program Genre']).sum()

total.plot.bar(figsize=(10,12))

plt.xlabel('Genres')
plt.ylabel('Viewers')

plt.show()