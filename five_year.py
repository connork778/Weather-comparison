import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

temps = pd.read_csv("boston_min_max_1981_2021.csv")

#Shortening column names
temps = temps.rename(columns={"tmin (degrees F)": "tmin", "tmax (degrees F)": "tmax"})


#Converts strings to datetime objects so we can run datetime operations on them
temps["Date"] = pd.to_datetime(temps["Date"])


#Copies rows from desired years
years_first = temps[temps.Date.dt.year.isin([1982, 1983, 1984, 1985, 1986])].copy()

years_last = temps[temps.Date.dt.year.isin([2016, 2017, 2018, 2019, 2020])].copy()




#Adds year column
years_first["Year"] = years_first["Date"].dt.year
years_last["Year"] = years_last["Date"].dt.year


#Create series that find mean and sorts temps by month and year
tmin_mean_first = years_first.groupby([years_first["Date"].dt.month, "Year"])["tmin"].mean()
tmin_mean_last = years_last.groupby([years_last["Date"].dt.month, "Year"])["tmin"].mean()

#Convert series to df then pivot into wide-form
tmin_mean_first = tmin_mean_first.to_frame()
tmin_mean_last = tmin_mean_last.to_frame()
wide_tmin_mean_first = tmin_mean_first.loc[:,:].reset_index().pivot(index="Date", columns="Year", values="tmin")
wide_tmin_mean_last = tmin_mean_last.loc[:,:].reset_index().pivot(index="Date", columns="Year", values="tmin")

#Create graphs
sns.heatmap(wide_tmin_mean_first, annot=True)
plt.show()


sns.heatmap(wide_tmin_mean_last, annot=True)
plt.show()




'''
CSV Information:
PRISM Time Series Data
Location:  Lat: 42.3707   Lon: -71.0868   Elev: 20ft
"Climate variables: tmin,tmax"
Spatial resolution: 4km
Period: 1981-01-01 - 2021-01-01
Dataset: AN81d
PRISM day definition: 24 hours ending at 1200 UTC on the day shown
Grid Cell Interpolation: Off
Time series generated: 2021-Nov-12
Details: http://www.prism.oregonstate.edu/documents/PRISM_datasets.pdf

To learn how to pivot the df I used:
https://stackabuse.com/ultimate-guide-to-heatmaps-in-seaborn-with-python/
'''