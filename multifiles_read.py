# EXERCISE
# Reading DataFrames from multiple files
# When data is spread among several files, you usually invoke pandas' read_csv() (or a similar data import function) multiple times to load the data into several DataFrames.
#
# The data files for this example have been derived from a list of Olympic medals awarded between 1896 & 2008 compiled by the Guardian.
#
# The column labels of each DataFrame are NOC, Country, & Total where NOC is a three-letter code for the name of the country and Total is the number of medals of that type won (bronze, silver, or gold).
#
# INSTRUCTIONS
# 100 XP
# Import pandas as pd.
# Read the file 'Bronze.csv' into a DataFrame called bronze.
# Read the file 'Silver.csv' into a DataFrame called silver.
# Read the file 'Gold.csv' into a DataFrame called gold.
# Print the first 5 rows of the DataFrame gold. This has been done for you, so hit 'Submit Answer' to see the results.

# Import pandas
import pandas as pd

# Read 'Bronze.csv' into a DataFrame: bronze
bronze = pd.read_csv('Bronze.csv')

# Read 'Silver.csv' into a DataFrame: silver
silver = pd.read_csv('Silver.csv')

# Read 'Gold.csv' into a DataFrame: gold
gold = pd.read_csv('Gold.csv')

# Print the first five rows of gold
print(gold.head())

# EXERCISE
# Reading DataFrames from multiple files in a loop
# As you saw in the video, loading data from multiple files into DataFrames is more efficient in a loop or a list comprehension.
#
# Notice that this approach is not restricted to working with CSV files. That is, even if your data comes in other formats, as long as pandas has a suitable data import function, you can apply a loop or comprehension to generate a list of DataFrames imported from the source files.
#
# Here, you'll continue working with The Guardian's Olympic medal dataset.
#
# INSTRUCTIONS
# 100 XP
# Create a list of file names called filenames with three strings 'Gold.csv', 'Silver.csv', & 'Bronze.csv'. This has been done for you.
# Use a for loop to create another list called dataframes containing the three DataFrames loaded from filenames:
# Iterate over filenames.
# Read each CSV file in filenames into a DataFrame and append it to dataframes by using pd.read_csv() inside a call to .append().
# Print the first 5 rows of the first DataFrame of the list dataframes. This has been done for you, so hit 'Submit Answer' to see the results.

# Import pandas
import pandas as pd

# Create the list of file names: filenames
filenames = ['Gold.csv', 'Silver.csv', 'Bronze.csv']

# Create the list of three DataFrames: dataframes
dataframes = []
for filename in filenames:

    dataframes.append(pd.read_csv(filename))

# Print top 5 rows of 1st DataFrame in dataframes
print(dataframes[0].head())

# EXERCISE
# Combining DataFrames from multiple data files
# In this exercise, you'll combine the three DataFrames from earlier exercises - gold, silver, & bronze - into a single DataFrame called medals. The approach you'll use here is clumsy. Later on in the course, you'll see various powerful methods that are frequently used in practice for concatenating or merging DataFrames.
#
# Remember, the column labels of each DataFrame are NOC, Country, and Total, where NOC is a three-letter code for the name of the country and Total is the number of medals of that type won.
#
# INSTRUCTIONS
# 100 XP
# Construct a copy of the DataFrame gold called medals using the .copy() method.
# Create a list called new_labels with entries 'NOC', 'Country', & 'Gold'. This is the same as the column labels from gold with the column label 'Total' replaced by 'Gold'.
# Rename the columns of medals by assigning new_labels to medals.columns.
# Create new columns 'Silver' and 'Bronze' in medals using silver['Total'] & bronze['Total'].
# Print the top 5 rows of the final DataFrame medals. This has been done for you, so hit 'Submit Answer' to see the result!

# Import pandas
import pandas as pd

# Make a copy of gold: medals
medals = gold.copy()

# Create list of new column labels: new_labels
new_labels = ['NOC', 'Country', 'Gold']

# Rename the columns of medals using new_labels
medals.columns = new_labels

# Add columns 'Silver' & 'Bronze' to medals
medals['Silver'] = silver['Total']
medals['Bronze'] = br['Total']

# Print the head of medals
print(medals.head())

# EXERCISE
# Sorting DataFrame with the Index & columns
# It is often useful to rearrange the sequence of the rows of a DataFrame by sorting. You don't have to implement these yourself; the principal methods for doing this are .sort_index() and .sort_values().
#
# In this exercise, you'll use these methods with a DataFrame of temperature values indexed by month names. You'll sort the rows alphabetically using the Index and numerically using a column. Notice, for this data, the original ordering is probably most useful and intuitive: the purpose here is for you to understand what the sorting methods do.
#
# INSTRUCTIONS
# 100 XP
# INSTRUCTIONS
# 100 XP
# Read 'monthly_max_temp.csv' into a DataFrame called weather1 with 'Month' as the index.
# Sort the index of weather1 in alphabetical order using the .sort_index() method and store the result in weather2.
# Sort the index of weather1 in reverse alphabetical order by specifying the additional keyword argument ascending=False inside .sort_index().
# Use the .sort_values() method to sort weather1 in increasing numerical order according to the values of the column 'Max TemperatureF'.

# Import pandas
import pandas as pd

# Read 'monthly_max_temp.csv' into a DataFrame: weather1
weather1 = pd.read_csv('monthly_max_temp.csv', index_col='Month')

# Print the head of weather1
print(weather1.head())

# Sort the index of weather1 in alphabetical order: weather2
weather2 = weather1.sort_index()

# Print the head of weather2
print(weather2.head())

# Sort the index of weather1 in reverse alphabetical order: weather3
weather3 = weather1.sort_index(ascending=False)

# Print the head of weather3
print(weather3.head())

# Sort weather1 numerically using the values of 'Max TemperatureF': weather4
weather4 = weather3.sort_values('Max TemperatureF')

# Print the head of weather4
print(weather4.head())

# EXERCISE
# Reindexing DataFrame from a list
# Sorting methods are not the only way to change DataFrame Indexes. There is also the .reindex() method.
#
# In this exercise, you'll reindex a DataFrame of quarterly-sampled mean temperature values to contain monthly samples (this is an example of upsampling or increasing the rate of samples, which you may recall from the pandas Foundations course).
#
# The original data has the first month's abbreviation of the quarter (three-month interval) on the Index, namely Apr, Jan, Jul, and Oct. This data has been loaded into a DataFrame called weather1 and has been printed in its entirety in the IPython Shell. Notice it has only four rows (corresponding to the first month of each quarter) and that the rows are not sorted chronologically.
#
# You'll initially use a list of all twelve month abbreviations and subsequently apply the .ffill() method to forward-fill the null entries when upsampling. This list of month abbreviations has been pre-loaded as year.
#
# INSTRUCTIONS
# 100 XP
# Reorder the rows of weather1 using the .reindex() method with the list year as the argument, which contains the abbreviations for each month.
# Reorder the rows of weather1 just as you did above, this time chaining the .ffill() method to replace the null values with the last preceding non-null value.

# Import pandas
import pandas as pd

# Reindex weather1 using the list year: weather2
weather2 = weather1.reindex(year)

# Print weather2
print(weather2)

# Reindex weather1 using the list year with forward-fill: weather3
weather3 = weather1.reindex(year).ffill()

# Print weather3
print(weather3)

# EXERCISE
# Reindexing using another DataFrame Index
# Another common technique is to reindex a DataFrame using the Index of another DataFrame. The DataFrame .reindex() method can accept the Index of a DataFrame or Series as input. You can access the Index of a DataFrame with its .index attribute.
#
# The Baby Names Dataset from data.gov summarizes counts of names (with genders) from births registered in the US since 1881. In this exercise, you will start with two baby-names DataFrames names_1981 and names_1881 loaded for you.
#
# The DataFrames names_1981 and names_1881 both have a MultiIndex with levels name and gender giving unique labels to counts in each row. If you're interested in seeing how the MultiIndexes were set up, names_1981 and names_1881 were read in using the following commands:
#
# names_1981 = pd.read_csv('names1981.csv', header=None, names=['name','gender','count'], index_col=(0,1))
# names_1881 = pd.read_csv('names1881.csv', header=None, names=['name','gender','count'], index_col=(0,1))
# As you can see by looking at their shapes, which have been printed in the IPython Shell, the DataFrame corresponding to 1981 births is much larger, reflecting the greater diversity of names in 1981 as compared to 1881.
#
# Your job here is to use the DataFrame .reindex() and .dropna() methods to make a DataFrame common_names counting names from 1881 that were still popular in 1981.
#
# INSTRUCTIONS
# 100 XP
# Create a new DataFrame common_names by reindexing names_1981 using the Index of the DataFrame names_1881 of older names.
# Print the shape of the new common_names DataFrame. This has been done for you. It should be the same as that of names_1881.
# Drop the rows of common_names that have null counts using the .dropna() method. These rows correspond to names that fell out of fashion between 1881 & 1981.
# Print the shape of the reassigned common_names DataFrame. This has been done for you, so hit 'Submit Answer' to see the result!

# Import pandas
import pandas as pd

# Reindex names_1981 with index of names_1881: common_names
common_names = names_1981.reindex(names_1881.index.get_values())

# Print shape of common_names
print(common_names.shape)

# Drop rows with null counts: common_names
common_names = common_names.dropna()

# Print shape of new common_names
print(common_names.shape)

# EXERCISE
# Broadcasting in arithmetic formulas
# In this exercise, you'll work with weather data pulled from wunderground.com. The DataFrame weather has been pre-loaded along with pandas as pd. It has 365 rows (observed each day of the year 2013 in Pittsburgh, PA) and 22 columns reflecting different weather measurements each day.
#
# You'll subset a collection of columns related to temperature measurements in degrees Fahrenheit, convert them to degrees Celsius, and relabel the columns of the new DataFrame to reflect the change of units.
#
# Remember, ordinary arithmetic operators (like +, -, *, and /) broadcast scalar values to conforming DataFrames when combining scalars & DataFrames in arithmetic expressions. Broadcasting also works with pandas Series and NumPy arrays.
#
# INSTRUCTIONS
# 100 XP
# Create a new DataFrame temps_f by extracting the columns 'Min TemperatureF', 'Mean TemperatureF', & 'Max TemperatureF' from weather as a new DataFrame temps_f. To do this, pass the relevant columns as a list to weather[].
# Create a new DataFrame temps_c from temps_f using the formula (temps_f - 32) * 5/9.
# Rename the columns of temps_c to replace 'F' with 'C' using the .str.replace('F', 'C') method on temps_c.columns.
# Print the first 5 rows of DataFrame temps_c. This has been done for you, so hit 'Submit Answer' to see the result!

# Extract selected columns from weather as new DataFrame: temps_f
temps_f = weather[['Min TemperatureF', 'Mean TemperatureF', 'Max TemperatureF']]

# Convert temps_f to celsius: temps_c
temps_c = (temps_f - 32) * 5/9

# Rename 'F' in column names with 'C': temps_c.columns
temps_c.columns = ['Min TemperatureC', 'Mean TemperatureC', 'Max TemperatureC']

# Print first 5 rows of temps_c
print(temps_c.head())

# EXERCISE
# Computing percentage growth of GDP
# Your job in this exercise is to compute the yearly percent-change of US GDP (Gross Domestic Product) since 2008.
#
# The data has been obtained from the Federal Reserve Bank of St. Louis and is available in the file GDP.csv, which contains quarterly data; you will resample it to annual sampling and then compute the annual growth of GDP. For a refresher on resampling, check out the relevant material from pandas Foundations.
#
# INSTRUCTIONS
# 100 XP
# Read the file 'GDP.csv' into a DataFrame called gdp.
# Use parse_dates=True and index_col='DATE'.
# Create a DataFrame post2008 by slicing gdp such that it comprises all rows from 2008 onward.
# Print the last 8 rows of the slice post2008. This has been done for you. This data has quarterly frequency so the indices are separated by three-month intervals.
# Create the DataFrame yearly by resampling the slice post2008 by year. Remember, you need to chain .resample() (using the alias 'A' for annual frequency) with some kind of aggregation; you will use the aggregation method .last() to select the last element when resampling.
# Compute the percentage growth of the resampled DataFrame yearly with .pct_change() * 100.

import pandas as pd

# Read 'GDP.csv' into a DataFrame: gdp
gdp = pd.read_csv('GDP.csv', parse_dates=True, index_col='DATE')
print(gdp.head())
# Slice all the gdp data from 2008 onward: post2008
post2008 = gdp.loc['2008' :]

# Print the last 8 rows of post2008
print(post2008.tail(8))

# Resample post2008 by year, keeping last(): yearly
yearly = post2008.resample('A').last()

# Print yearly
print(yearly)

# Compute percentage growth of yearly: yearly['growth']
yearly['growth'] = yearly.pct_change() * 100

# Print yearly again
print(yearly)

# EXERCISE
# Converting currency of stocks
# In this exercise, stock prices in US Dollars for the S&P 500 in 2015 have been obtained from Yahoo Finance. The files sp500.csv for sp500 and exchange.csv for the exchange rates are both provided to you.
#
# Using the daily exchange rate to Pounds Sterling, your task is to convert both the Open and Close column prices.
#
# INSTRUCTIONS
# 100 XP
# Read the DataFrames sp500 & exchange from the files 'sp500.csv' & 'exchange.csv' respectively..
# Use parse_dates=True and index_col='Date'.
# Extract the columns 'Open' & 'Close' from the DataFrame sp500 as a new DataFrame dollars and print the first 5 rows.
# Construct a new DataFrame pounds by converting US dollars to British pounds. You'll use the .multiply() method of dollars with exchange['GBP/USD'] and axis='rows'
# Print the first 5 rows of the new DataFrame pounds. This has been done for you, so hit 'Submit Answer' to see the results!.

# Import pandas
import pandas as pd

# Read 'sp500.csv' into a DataFrame: sp500
sp500 = pd.read_csv('sp500.csv', parse_dates=True, index_col='Date')
print(sp500.head())
# Read 'exchange.csv' into a DataFrame: exchange
exchange = pd.read_csv('exchange.csv', parse_dates=True, index_col='Date')

# Subset 'Open' & 'Close' columns from sp500: dollars
dollars = sp500[['Open', 'Close']]

# Print the head of dollars
print(dollars.head())

# Convert dollars to pounds: pounds
pounds = dollars.multiply(exchange['GBP/USD'], axis='rows')

# Print the head of pounds
print(pounds.head())

# EXERCISE
# Appending pandas Series
# In this exercise, you'll load sales data from the months January, February, and March into DataFrames. Then, you'll extract Series with the 'Units' column from each and append them together with method chaining using .append().
#
# To check that the stacking worked, you'll print slices from these Series, and finally, you'll add the result to figure out the total units sold in the first quarter.
#
# INSTRUCTIONS
# 100 XP
# INSTRUCTIONS
# 100 XP
# Read the files 'sales-jan-2015.csv', 'sales-feb-2015.csv' and 'sales-mar-2015.csv' into the DataFrames jan, feb, and mar respectively.
# Use parse_dates=True and index_col='Date'.
# Extract the 'Units' column of jan, feb, and mar to create the Series jan_units, feb_units, and mar_units respectively.
# Construct the Series quarter1 by appending feb_units to jan_units and then appending mar_units to the result. Use chained calls to the .append() method to do this.
# Verify that quarter1 has the individual Series stacked vertically. To do this:
# Print the slice containing rows from jan 27, 2015 to feb 2, 2015.
# Print the slice containing rows from feb 26, 2015 to mar 7, 2015.
# Compute and print the total number of units sold from the Series quarter1. This has been done for you, so hit 'Submit Answer' to see the result!

# Import pandas
import pandas as pd

# Load 'sales-jan-2015.csv' into a DataFrame: jan
jan = pd.read_csv('sales-jan-2015.csv', parse_dates=True, index_col='Date')

# Load 'sales-feb-2015.csv' into a DataFrame: feb
feb = pd.read_csv('sales-feb-2015.csv', parse_dates=True, index_col='Date')

# Load 'sales-mar-2015.csv' into a DataFrame: mar
mar = pd.read_csv('sales-mar-2015.csv', parse_dates=True, index_col='Date')

# Extract the 'Units' column from jan: jan_units
jan_units = jan['Units']

# Extract the 'Units' column from feb: feb_units
feb_units = feb['Units']

# Extract the 'Units' column from mar: mar_units
mar_units = mar['Units']

# Append feb_units and then mar_units to jan_units: quarter1
quarter1 = jan_units.append(feb_units).append(mar_units)

# Print the first slice from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])

# Print the second slice from quarter1
print(quarter1.loc['feb 26, 2015' : 'mar 7, 2015'])

# Compute & print total sales in quarter1
print(quarter1.sum())


# EXERCISE
# Concatenating pandas Series along row axis
# Having learned how to append Series, you'll now learn how to achieve the same result by concatenating Series instead. You'll continue to work with the sales data you've seen previously. This time, the DataFrames jan, feb, and mar have been pre-loaded.
#
# Your job is to use pd.concat() with a list of Series to achieve the same result that you would get by chaining calls to .append().
#
# You may be wondering about the difference between pd.concat() and pandas' .append() method. One way to think of the difference is that .append() is a specific case of a concatenation, while pd.concat() gives you more flexibility, as you'll see in later exercises.
#
# INSTRUCTIONS
# 100 XP
# INSTRUCTIONS
# 100 XP
# Create an empty list called units. This has been done for you.
# Use a for loop to iterate over [jan, feb, mar]:
# In each iteration of the loop, append the 'Units' column of each DataFrame to units.
# Concatenate the Series contained in the list units into a longer Series called quarter1 using pd.concat().
# Specify the keyword argument axis='rows' to stack the Series vertically.
# Verify that quarter1 has the individual Series stacked vertically by printing slices. This has been done for you, so hit 'Submit Answer' to see the result!

# Initialize empty list: units
units = []

# Build the list of Series
for month in [jan, feb, mar]:
    units.append(month['Units'])

# Concatenate the list: quarter1
quarter1 = pd.concat(units, axis='rows')
# Print slices from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])

# EXERCISE
# Appending DataFrames with ignore_index
# In this exercise, you'll use the Baby Names Dataset (from data.gov) again. This time, both DataFrames names_1981 and names_1881 are loaded without specifying an Index column (so the default Indexes for both are RangeIndexes).
#
# You'll use the DataFrame .append() method to make a DataFrame combined_names. To distinguish rows from the original two DataFrames, you'll add a 'year' column to each with the year (1881 or 1981 in this case). In addition, you'll specify ignore_index=True so that the index values are not used along the concatenation axis. The resulting axis will instead be labeled 0, 1, ..., n-1, which is useful if you are concatenating objects where the concatenation axis does not have meaningful indexing information.
#
# INSTRUCTIONS
# 100 XP
# Create a 'year' column in the DataFrames names_1881 and names_1981, with values of 1881 and 1981 respectively. Recall that assigning a scalar value to a DataFrame column broadcasts that value throughout.
# Create a new DataFrame called combined_names by appending the rows of names_1981 underneath the rows of names_1881. Specify the keyword argument ignore_index=True to make a new RangeIndex of unique integers for each row.
# Print the shapes of all three DataFrames. This has been done for you.
# Extract all rows from combined_names that have the name 'Morgan'. To do this, use the .loc[] accessor with an appropriate filter. The relevant column of combined_names here is 'name'.


# Add 'year' column to names_1881 and names_1981
names_1881['year'] = 1881
names_1981['year'] = 1981

# Append names_1981 after names_1881 with ignore_index=True: combined_names
combined_names = names_1881.append(names_1981, ignore_index=True)

# Print shapes of names_1981, names_1881, and combined_names
print(names_1981.shape)
print(names_1881.shape)
print(combined_names.shape)

# Print all rows that contain the name 'Morgan'
print(combined_names.loc[combined_names['name'] == 'Morgan'])

# EXERCISE
# Concatenating pandas DataFrames along column axis
# The function pd.concat() can concatenate DataFrames horizontally as well as vertically (vertical is the default). To make the DataFrames stack horizontally, you have to specify the keyword argument axis=1 or axis='columns'.
#
# In this exercise, you'll use weather data with maximum and mean daily temperatures sampled at different rates (quarterly versus monthly). You'll concatenate the rows of both and see that, where rows are missing in the coarser DataFrame, null values are inserted in the concatenated DataFrame. This corresponds to an outer join (which you will explore in more detail in later exercises).
#
# The files 'quarterly_max_temp.csv' and 'monthly_mean_temp.csv' have been pre-loaded into the DataFrames weather_max and weather_mean respectively, and pandas has been imported as pd.
#
# INSTRUCTIONS
# 100 XP
# Create a new DataFrame called weather by concatenating the DataFrames weather_max and weather_mean horizontally.
# Pass the DataFrames to pd.concat() as a list and specify the keyword argument axis=1 to stack them horizontally.
# Print the new DataFrame weather.

# Concatenate weather_max and weather_mean horizontally: weather
weather = pd.concat([weather_max, weather_mean], axis=1)

# Print weather
print(weather)

# EXERCISE
# Reading multiple files to build a DataFrame
# It is often convenient to build a large DataFrame by parsing many files as DataFrames and concatenating them all at once. You'll do this here with three files, but, in principle, this approach can be used to combine data from dozens or hundreds of files.
#
# Here, you'll work with DataFrames compiled from The Guardian's Olympic medal dataset.
#
# pandas has been imported as pd and two lists have been pre-loaded: An empty list called medals, and medal_types, which contains the strings 'bronze', 'silver', and 'gold'.
#
# INSTRUCTIONS
# 100 XP
# Iterate over medal_types in the for loop.
# Inside the for loop:
# Create file_name using string interpolation with the loop variable medal. This has been done for you. The expression "%s_top5.csv" % medal evaluates as a string with the value of medal replacing %s in the format string.
# Create the list of column names called columns. This has been done for you.
# Read file_name into a DataFrame called medal_df. Specify the keyword arguments header=0, index_col='Country', and names=columns to get the correct row and column Indexes.
# Append medal_df to medals using the list .append() method.
# Concatenate the list of DataFrames medals horizontally (using axis='columns') to create a single DataFrame called medals. Print it in its entirety.


for medal in medal_types:

    # Create the file name: file_name
    file_name = "%s_top5.csv" % medal

    # Create list of column names: columns
    columns = ['Country', medal]

    # Read file_name into a DataFrame: df
    medal_df = pd.read_csv(file_name, header=0, index_col='Country', names=columns)

    # Append medal_df to medals
    medals.append(medal_df)

# Concatenate medals horizontally: medals
medals = pd.concat(medals, axis='columns')

# Print medals
print(medals)

# EXERCISE
# Concatenating vertically to get MultiIndexed rows
# When stacking a sequence of DataFrames vertically, it is sometimes desirable to construct a MultiIndex to indicate the DataFrame from which each row originated. This can be done by specifying the keys parameter in the call to pd.concat(), which generates a hierarchical index with the labels from keys as the outermost index label. So you don't have to rename the columns of each DataFrame as you load it. Instead, only the Index column needs to be specified.
#
# Here, you'll continue working with DataFrames compiled from The Guardian's Olympic medal dataset. Once again, pandas has been imported as pd and two lists have been pre-loaded: An empty list called medals, and medal_types, which contains the strings 'bronze', 'silver', and 'gold'.
#
# INSTRUCTIONS
# 100 XP
# Within the for loop:
# Read file_name into a DataFrame called medal_df. Specify the index to be 'Country'.
# Append medal_df to medals.
# Concatenate the list of DataFrames medals into a single DataFrame called medals. Be sure to use the keyword argument keys=['bronze', 'silver', 'gold'] to create a vertically stacked DataFrame with a MultiIndex.
# Print the new DataFrame medals. This has been done for you, so hit 'Submit Answer' to see the result!

for medal in medal_types:

    file_name = "%s_top5.csv" % medal

    # Read file_name into a DataFrame: medal_df
    medal_df = pd.read_csv(file_name, index_col='Country')

    # Append medal_df to medals
    medals.append(medal_df)

# Concatenate medals: medals
medals = pd.concat(medals, keys=['bronze', 'silver', 'gold'])

# Print medals in entirety
print(medals)

# EXERCISE
# Slicing MultiIndexed DataFrames
# This exercise picks up where the last ended (again using The Guardian's Olympic medal dataset).
#
# You are provided with the MultiIndexed DataFrame as produced at the end of the preceding exercise. Your task is to sort the DataFrame and to use the pd.IndexSlice to extract specific slices. Check out this exercise from Manipulating DataFrames with pandas to refresh your memory on how to deal with MultiIndexed DataFrames.
#
# pandas has been imported for you as pd and the DataFrame medals is already in your namespace.
#
# INSTRUCTIONS
# 100 XP
# Create a new DataFrame medals_sorted with the entries of medals sorted. Use .sort_index(level=0) to ensure the Index is sorted suitably.
# Print the number of bronze medals won by Germany and all of the silver medal data. This has been done for you.
# Create an alias for pd.IndexSlice called idx. A slicer pd.IndexSlice is required when slicing on the inner level of a MultiIndex.
# Slice all the data on medals won by the United Kingdom. To do this, use the .loc[] accessor with idx[:,'United Kingdom'], :.

# Sort the entries of medals: medals_sorted
medals_sorted = medals.sort_index(level=0)

# Print the number of Bronze medals won by Germany
print(medals_sorted.loc[('bronze','Germany')])

# Print data about silver medals
print(medals_sorted.loc['silver'])

# Create alias for pd.IndexSlice: idx
idx = pd.IndexSlice

# Print all the data on medals won by the United Kingdom
print(medals_sorted.loc[idx[:, 'United Kingdom'], : ])

# EXERCISE
# Concatenating horizontally to get MultiIndexed columns
# It is also possible to construct a DataFrame with hierarchically indexed columns. For this exercise, you'll start with pandas imported and a list of three DataFrames called dataframes. All three DataFrames contain 'Company', 'Product', and 'Units' columns with a 'Date' column as the index pertaining to sales transactions during the month of February, 2015. The first DataFrame describes Hardware transactions, the second describes Software transactions, and the third, Service transactions.
#
# Your task is to concatenate the DataFrames horizontally and to create a MultiIndex on the columns. From there, you can summarize the resulting DataFrame and slice some information from it.
#
# INSTRUCTIONS
# 100 XP
# Construct a new DataFrame february with MultiIndexed columns by concatenating the list dataframes.
# Use axis=1 to stack the DataFrames horizontally and the keyword argument keys=['Hardware', 'Software', 'Service'] to construct a hierarchical Index from each DataFrame.
# Print summary information from the new DataFrame february using the .info() method. This has been done for you.
# Create an alias called idx for pd.IndexSlice.
# Extract a slice called slice_2_8 from february (using .loc[] & idx) that comprises rows between Feb. 2, 2015 to Feb. 8, 2015 from columns under 'Company'.
# Print the slice_2_8. This has been done for you, so hit 'Submit Answer' to see the sliced data!

# Concatenate dataframes: february
february = pd.concat(dataframes, axis=1, keys=['Hardware', 'Software', 'Service'])

# Print february.info()
print(february.info())

# Assign pd.IndexSlice: idx
idx = pd.IndexSlice

# Create the slice: slice_2_8
slice_2_8 = february.loc['Feb. 2, 2015 ':'Feb. 8, 2015 ', idx[:, 'Company']]

# Print slice_2_8
print(slice_2_8)


# EXERCISE
# Concatenating DataFrames from a dict
# You're now going to revisit the sales data you worked with earlier in the chapter. Three DataFrames jan, feb, and mar have been pre-loaded for you. Your task is to aggregate the sum of all sales over the 'Company' column into a single DataFrame. You'll do this by constructing a dictionary of these DataFrames and then concatenating them.
#
# INSTRUCTIONS
# 100 XP
# INSTRUCTIONS
# 100 XP
# Create a list called month_list consisting of the tuples ('january', jan), ('february', feb), and ('march', mar).
# Create an empty dictionary called month_dict.
# Inside the for loop:
# Group month_data by 'Company' and use .sum() to aggregate.
# Construct a new DataFrame called sales by concatenating the DataFrames stored in month_dict.
# Create an alias for pd.IndexSlice and print all sales by 'Mediacore'. This has been done for you, so hit 'Submit Answer' to see the result!

# Make the list of tuples: month_list
month_list = [('january', jan), ('february', feb), ('march', mar)]

# Create an empty dictionary: month_dict
month_dict = {}

for month_name, month_data in month_list:

    # Group month_data: month_dict[month_name]
    month_dict[month_name] = month_data.groupby('Company').sum()

# Concatenate data in month_dict: sales
sales = pd.concat(month_dict)

# Print sales
print(sales)

# Print all sales by Mediacore
idx = pd.IndexSlice
print(sales.loc[idx[:, 'Mediacore'], :])


# EXERCISE
# Concatenating DataFrames with inner join
# Here, you'll continue working with DataFrames compiled from The Guardian's Olympic medal dataset.
#
# The DataFrames bronze, silver, and gold have been pre-loaded for you.
#
# Your task is to compute an inner join.
#
# INSTRUCTIONS
# 100 XP
# Construct a list of DataFrames called medal_list with entries bronze, silver, and gold.
# Concatenate medal_list horizontally with an inner join to create medals.
# Use the keyword argument keys=['bronze', 'silver', 'gold'] to yield suitable hierarchical indexing.
# Use axis=1 to get horizontal concatenation.
# Use join='inner' to keep only rows that share common index labels.
# Print the new DataFrame medals.

# Create the list of DataFrames: medal_list
medal_list = [bronze, silver, gold]

# Concatenate medal_list horizontally using an inner join: medals
medals = pd.concat(medal_list, keys= ['bronze', 'silver', 'gold'], axis=1, join= 'inner')

# Print medals
print(medals)


# EXERCISE
# Resampling & concatenating DataFrames with inner join
# In this exercise, you'll compare the historical 10-year GDP (Gross Domestic Product) growth in the US and in China. The data for the US starts in 1947 and is recorded quarterly; by contrast, the data for China starts in 1961 and is recorded annually.
#
# You'll need to use a combination of resampling and an inner join to align the index labels. You'll need an appropriate offset alias for resampling, and the method .resample() must be chained with some kind of aggregation method (.pct_change() and .last() in this case).
#
# pandas has been imported as pd, and the DataFrames china and us have been pre-loaded, with the output of china.head() and us.head() printed in the IPython Shell.
#
# INSTRUCTIONS
# 100 XP
# Make a new DataFrame china_annual by resampling the DataFrame china with .resample('A') (i.e., with annual frequency) and chaining two method calls:
# Chain .pct_change(10) as an aggregation method to compute the percentage change with an offset of ten years.
# Chain .dropna() to eliminate rows containing null values.
# Make a new DataFrame us_annual by resampling the DataFrame us exactly as you resampled china.
# Concatenate china_annual and us_annual to construct a DataFrame called gdp. Use join='inner' to perform an inner join and use axis=1 to concatenate horizontally.
# Print the result of resampling gdp every decade (i.e., using .resample('10A')) and aggregating with the method .last(). This has been done for you, so hit 'Submit Answer' to see the result!

# Resample and tidy china: china_annual
china_annual = china.resample('A').pct_change(10).dropna()

# Resample and tidy us: us_annual
us_annual = us.resample('A').pct_change(10).dropna()

# Concatenate china_annual and us_annual: gdp
gdp = pd.concat([china_annual, us_annual], join='inner', axis=1)

# Resample gdp and print
print(gdp.resample('10A').last())

# 
