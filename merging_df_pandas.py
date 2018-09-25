# EXERCISE
# Merging on a specific column
# This exercise follows on the last one with the DataFrames revenue and managers for your company. You expect your company to grow and, eventually, to operate in cities with the same name on different states. As such, you decide that every branch should have a numerical branch identifier. Thus, you add a branch_id column to both DataFrames. Moreover, new cities have been added to both the revenue and managers DataFrames as well. pandas has been imported as pd and both DataFrames are available in your namespace.
#
# At present, there should be a 1-to-1 relationship between the city and branch_id fields. In that case, the result of a merge on the city columns ought to give you the same output as a merge on the branch_id columns. Do they? Can you spot an ambiguity in one of the DataFrames?
#
# INSTRUCTIONS
# 100 XP
# Using pd.merge(), merge the DataFrames revenue and managers on the 'city' column of each. Store the result as merge_by_city.
# Print the DataFrame merge_by_city. This has been done for you.
# Merge the DataFrames revenue and managers on the 'branch_id' column of each. Store the result as merge_by_id.
# Print the DataFrame merge_by_id. This has been done for you, so hit 'Submit Answer' to see the result!

# Merge revenue with managers on 'city': merge_by_city
merge_by_city = pd.merge(revenue, managers, on='city')

# Print merge_by_city
print(merge_by_city)

# Merge revenue with managers on 'branch_id': merge_by_id
merge_by_id = pd.merge(revenue, managers, on='branch_id')

# Print merge_by_id
print(merge_by_id)

# EXERCISE
# Merging on columns with non-matching labels
# You continue working with the revenue & managers DataFrames from before. This time, someone has changed the field name 'city' to 'branch' in the managers table. Now, when you attempt to merge DataFrames, an exception is thrown:
#
# >>> pd.merge(revenue, managers, on='city')
# Traceback (most recent call last):
#     ... <text deleted> ...
#     pd.merge(revenue, managers, on='city')
#     ... <text deleted> ...
# KeyError: 'city'
# Given this, it will take a bit more work for you to join or merge on the city/branch name. You have to specify the left_on and right_on parameters in the call to pd.merge().
#
# As before, pandas has been pre-imported as pd and the revenue and managers DataFrames are in your namespace. They have been printed in the IPython Shell so you can examine the columns prior to merging.
#
# Are you able to merge better than in the last exercise? How should the rows with Springfield be handled?
#
# INSTRUCTIONS
# 100 XP
# Merge the DataFrames revenue and managers into a single DataFrame called combined using the 'city' and 'branch' columns from the appropriate DataFrames.
# In your call to pd.merge(), you will have to specify the parameters left_on and right_on appropriately.
# Print the new DataFrame combined.

# Merge revenue & managers on 'city' & 'branch': combined
combined = pd.merge(revenue, managers, left_on='city', right_on='branch')

# Print combined
print(combined)

# EXERCISE
# Merging on multiple columns
# Another strategy to disambiguate cities with identical names is to add information on the states in which the cities are located. To this end, you add a column called state to both DataFrames from the preceding exercises. Again, pandas has been pre-imported as pd and the revenue and managers DataFrames are in your namespace.
#
# Your goal in this exercise is to use pd.merge() to merge DataFrames using multiple columns (using 'branch_id', 'city', and 'state' in this case).
#
# Are you able to match all your company's branches correctly?
#
# INSTRUCTIONS
# 100 XP
# Create a column called 'state' in the DataFrame revenue, consisting of the list ['TX','CO','IL','CA'].
# Create a column called 'state' in the DataFrame managers, consisting of the list ['TX','CO','CA','MO'].
# Merge the DataFrames revenue and managers using three columns :'branch_id', 'city', and 'state'. Pass them in as a list to the on paramater of pd.merge().

# Add 'state' column to revenue: revenue['state']
revenue['state'] = ['TX','CO','IL','CA']

# Add 'state' column to managers: managers['state']
managers['state'] = ['TX','CO','CA','MO']

# Merge revenue & managers on 'branch_id', 'city', & 'state': combined
combined = pd.merge(revenue, managers, on=['branch_id', 'city', 'state'])

# Print combined
print(combined)

# EXERCISE
# Left & right merging on multiple columns
# You now have, in addition to the revenue and managers DataFrames from prior exercises, a DataFrame sales that summarizes units sold from specific branches (identified by city and state but not branch_id).
#
# Once again, the managers DataFrame uses the label branch in place of city as in the other two DataFrames. Your task here is to employ left and right merges to preserve data and identify where data is missing.
#
# By merging revenue and sales with a right merge, you can identify the missing revenue values. Here, you don't need to specify left_on or right_on because the columns to merge on have matching labels.
#
# By merging sales and managers with a left merge, you can identify the missing manager. Here, the columns to merge on have conflicting labels, so you must specify left_on and right_on. In both cases, you're looking to figure out how to connect the fields in rows containing Springfield.
#
# pandas has been imported as pd and the three DataFrames revenue, managers, and sales have been pre-loaded. They have been printed for you to explore in the IPython Shell.
#
# INSTRUCTIONS
# 100 XP
# Execute a right merge using pd.merge() with revenue and sales to yield a new DataFrame revenue_and_sales.
# Use how='right' and on=['city', 'state'].
# Print the new DataFrame revenue_and_sales. This has been done for you.
# Execute a left merge with sales and managers to yield a new DataFrame sales_and_managers.
# Use how='left', left_on=['city', 'state'], and right_on=['branch', 'state'].
# Print the new DataFrame sales_and_managers. This has been done for you, so hit 'Submit Answer' to see the result!

# Merge revenue and sales: revenue_and_sales
revenue_and_sales = pd.merge(revenue, sales, how='right', on=['city', 'state'])

# Print revenue_and_sales
print(revenue_and_sales)

# Merge sales and managers: sales_and_managers
sales_and_managers = pd.merge(sales, managers, how='left', left_on=['city', 'state'], right_on=['branch', 'state'])

# Print sales_and_managers
print(sales_and_managers)

# EXERCISE
# Merging DataFrames with outer join
# This exercise picks up where the previous one left off. The DataFrames revenue, managers, and sales are pre-loaded into your namespace (and, of course, pandas is imported as pd). Moreover, the merged DataFrames revenue_and_sales and sales_and_managers have been pre-computed exactly as you did in the previous exercise.
#
# The merged DataFrames contain enough information to construct a DataFrame with 5 rows with all known information correctly aligned and each branch listed only once. You will try to merge the merged DataFrames on all matching keys (which computes an inner join by default). You can compare the result to an outer join and also to an outer join with restricted subset of columns as keys.
#
# INSTRUCTIONS
# 100 XP
# Merge sales_and_managers with revenue_and_sales. Store the result as merge_default.
# Print merge_default. This has been done for you.
# Merge sales_and_managers with revenue_and_sales using how='outer'. Store the result as merge_outer.
# Print merge_outer. This has been done for you.
# Merge sales_and_managers with revenue_and_sales only on ['city','state'] using an outer join. Store the result as merge_outer_on and hit 'Submit Answer' to see what the merged DataFrames look like!

# Perform the first merge: merge_default
merge_default = pd.merge(sales_and_managers, revenue_and_sales)

# Print merge_default
print(merge_default)

# Perform the second merge: merge_outer
merge_outer = pd.merge(sales_and_managers, revenue_and_sales, how='outer')

# Print merge_outer
print(merge_outer)

# Perform the third merge: merge_outer_on
merge_outer_on = pd.merge(sales_and_managers, revenue_and_sales, on=['city', 'state'], how='outer')

# Print merge_outer_on
print(merge_outer_on)

# EXERCISE
# Using merge_ordered()
# This exercise uses pre-loaded DataFrames austin and houston that contain weather data from the cities Austin and Houston respectively. They have been printed in the IPython Shell for you to examine.
#
# Weather conditions were recorded on separate days and you need to merge these two DataFrames together such that the dates are ordered. To do this, you'll use pd.merge_ordered(). After you're done, note the order of the rows before and after merging.
#
# INSTRUCTIONS
# 100 XP
# Perform an ordered merge on austin and houston using pd.merge_ordered(). Store the result as tx_weather.
# Print tx_weather. You should notice that the rows are sorted by the date but it is not possible to tell which observation came from which city.
# Perform another ordered merge on austin and houston.
# This time, specify the keyword arguments on='date' and suffixes=['_aus','_hus'] so that the rows can be distinguished. Store the result as tx_weather_suff.
# Print tx_weather_suff to examine its contents. This has been done for you.
# Perform a third ordered merge on austin and houston.
# This time, in addition to the on and suffixes parameters, specify the keyword argument fill_method='ffill' to use forward-filling to replace NaN entries with the most recent non-null entry, and hit 'Submit Answer' to examine the contents of the merged DataFrames!

# Perform the first ordered merge: tx_weather
tx_weather = pd.merge_ordered(austin, houston)

# Print tx_weather
print(tx_weather)

# Perform the second ordered merge: tx_weather_suff
tx_weather_suff = pd.merge_ordered(austin, houston, on='date', suffixes=['_aus', '_hus'])

# Print tx_weather_suff
print(tx_weather_suff)

# Perform the third ordered merge: tx_weather_ffill
tx_weather_ffill = pd.merge_ordered(austin, houston, on='date', suffixes=['_aus', '_hus'], fill_method='ffill')

# Print tx_weather_ffill
print(tx_weather_ffill)

# EXERCISE
# Using merge_asof()
# Similar to pd.merge_ordered(), the pd.merge_asof() function will also merge values in order using the on column, but for each row in the left DataFrame, only rows from the right DataFrame whose 'on' column values are less than the left value will be kept.
#
# This function can be used to align disparate datetime frequencies without having to first resample.
#
# Here, you'll merge monthly oil prices (US dollars) into a full automobile fuel efficiency dataset. The oil and automobile DataFrames have been pre-loaded as oil and auto. The first 5 rows of each have been printed in the IPython Shell for you to explore.
#
# These datasets will align such that the first price of the year will be broadcast into the rows of the automobiles DataFrame. This is considered correct since by the start of any given year, most automobiles for that year will have already been manufactured.
#
# You'll then inspect the merged DataFrame, resample by year and compute the mean 'Price' and 'mpg'. You should be able to see a trend in these two columns, that you can confirm by computing the Pearson correlation between resampled 'Price' and 'mpg'.
#
# INSTRUCTIONS
# 100 XP
# Merge auto and oil using pd.merge_asof() with left_on='yr' and right_on='Date'. Store the result as merged.
# Print the tail of merged. This has been done for you.
# Resample merged using 'A' (annual frequency), and on='Date'. Select [['mpg','Price']] and aggregate the mean. Store the result as yearly.
# Hit Submit Answer to examine the contents of yearly and yearly.corr(), which shows the Pearson correlation between the resampled 'Price' and 'mpg'.

# Merge auto and oil: merged
merged = pd.merge_asof(auto, oil, left_on='yr', right_on='Date')

# Print the tail of merged
print(merged.tail())

# Resample merged: yearly
yearly = merged.resample('A', on='Date')[['mpg', 'Price']].mean()

# Print yearly
print(yearly)

# print yearly.corr()
print(yearly.corr())

# EXERCISE
# Loading Olympic edition DataFrame
# In this chapter, you'll be using The Guardian's Olympic medal dataset.
#
# Your first task here is to prepare a DataFrame editions from a tab-separated values (TSV) file.
#
# Initially, editions has 26 rows (one for each Olympic edition, i.e., a year in which the Olympics was held) and 7 columns: 'Edition', 'Bronze', 'Gold', 'Silver', 'Grand Total', 'City', and 'Country'.
#
# For the analysis that follows, you won't need the overall medal counts, so you want to keep only the useful columns from editions: 'Edition', 'Grand Total', City, and Country.
#
# INSTRUCTIONS
# 100 XP
# INSTRUCTIONS
# 100 XP
# Read file_path into a DataFrame called editions. The identifier file_path has been pre-defined with the filename 'Summer Olympic medallists 1896 to 2008 - EDITIONS.tsv'. You'll have to use the option sep='\t' because the file uses tabs to delimit fields (pd.read_csv() expects commas by default).
# Select only the columns 'Edition', 'Grand Total', 'City', and 'Country' from editions.
# Print the final DataFrame editions in entirety (there are only 26 rows). This has been done for you, so hit 'Submit Answer' to see the result!

#Import pandas
import pandas as pd

# Create file path: file_path
file_path = 'Summer Olympic medallists 1896 to 2008 - EDITIONS.tsv'

# Load DataFrame from file_path: editions
editions = pd.read_csv(file_path, sep='\t')

# Extract the relevant columns: editions
editions = editions[['Edition', 'Grand Total', 'City', 'Country']]

# Print editions DataFrame
print(editions)

# EXERCISE
# Loading IOC codes DataFrame
# Your task here is to prepare a DataFrame ioc_codes from a comma-separated values (CSV) file.
#
# Initially, ioc_codes has 200 rows (one for each country) and 3 columns: 'Country', 'NOC', & 'ISO code'.
#
# For the analysis that follows, you want to keep only the useful columns from ioc_codes: 'Country' and 'NOC' (the column 'NOC' contains three-letter codes representing each country).
#
# INSTRUCTIONS
# 100 XP
# Read file_path into a DataFrame called ioc_codes. The identifier file_path has been pre-defined with the filename 'Summer Olympic medallists 1896 to 2008 - IOC COUNTRY CODES.csv'.
# Select only the columns 'Country' and 'NOC' from ioc_codes.
# Print the leading 5 and trailing 5 rows of the DataFrame ioc_codes (there are 200 rows in total). This has been done for you, so hit 'Submit Answer' to see the result!

# Import pandas
import pandas as pd

# Create the file path: file_path
file_path = 'Summer Olympic medallists 1896 to 2008 - IOC COUNTRY CODES.csv'

# Load DataFrame from file_path: ioc_codes
ioc_codes = pd.read_csv(file_path)

# Extract the relevant columns: ioc_codes
ioc_codes = ioc_codes[['Country', 'NOC']]

# Print first and last 5 rows of ioc_codes
print(ioc_codes.head())
print(ioc_codes.tail())

# EXERCISE
# Building medals DataFrame
# Here, you'll start with the DataFrame editions from the previous exercise.
#
# You have a sequence of files summer_1896.csv, summer_1900.csv, ..., summer_2008.csv, one for each Olympic edition (year).
#
# You will build up a dictionary medals_dict with the Olympic editions (years) as keys and DataFrames as values.
#
# The dictionary is built up inside a loop over the year of each Olympic edition (from the Index of editions).
#
# Once the dictionary of DataFrames is built up, you will combine the DataFrames using pd.concat().
#
# INSTRUCTIONS
# 100 XP
# Within the for loop:
# Create the file path. This has been done for you.
# Read file_path into a DataFrame. Assign the result to the year key of medals_dict.
# Select only the columns 'Athlete', 'NOC', and 'Medal' from medals_dict[year].
# Create a new column called 'Edition' in the DataFrame medals_dict[year] whose entries are all year.
# Concatenate the dictionary of DataFrames medals_dict into a DataFame called medals. Specify the keyword argument ignore_index=True to prevent repeated integer indices.
# Print the first and last 5 rows of medals. This has been done for you, so hit 'Submit Answer' to see the result!

# Import pandas
import pandas as pd

# Create empty dictionary: medals_dict
medals_dict = {}

for year in editions['Edition']:

    # Create the file path: file_path
    file_path = 'summer_{:d}.csv'.format(year)

    # Load file_path into a DataFrame: medals_dict[year]
    medals_dict[year] = pd.read_csv(file_path)

    # Extract relevant columns: medals_dict[year]
    medals_dict[year] = medals_dict[year][['Athlete', 'NOC', 'Medal']]

    # Assign year to column 'Edition' of medals_dict
    medals_dict[year]['Edition'] = year

# Concatenate medals_dict: medals
medals = pd.concat(medals_dict, ignore_index=True)
# Print first and last 5 rows of medals
print(medals.head())
print(medals.tail())

# EXERCISE
# Counting medals by country/edition in a pivot table
# Here, you'll start with the concatenated DataFrame medals from the previous exercise.
#
# You can construct a pivot table to see the number of medals each country won in each year. The result is a new DataFrame with the Olympic edition on the Index and with 138 country NOC codes as columns. If you want a refresher on pivot tables, it may be useful to refer back to the relevant exercises in Manipulating DataFrames with pandas.
#
# INSTRUCTIONS
# 100 XP
# Construct a pivot table from the DataFrame medals, aggregating by count (by specifying the aggfunc parameter). Use 'Edition' as the index, 'Athlete' for the values, and 'NOC' for the columns.
# Print the first & last 5 rows of medal_counts. This has been done for you, so hit 'Submit Answer' to see the results!


# Construct the pivot_table: medal_counts
medal_counts = medals.pivot_table(values='Athlete', columns='NOC', index='Edition', aggfunc='count')

# Print the first & last 5 rows of medal_counts
print(medal_counts.head())
print(medal_counts.tail())

# EXERCISE
# Computing fraction of medals per Olympic edition
# In this exercise, you'll start with the DataFrames editions, medals, & medal_counts from prior exercises.
#
# You can extract a Series with the total number of medals awarded in each Olympic edition.
#
# The DataFrame medal_counts can be divided row-wise by the total number of medals awarded each edition; the method .divide() performs the broadcast as you require.
#
# This gives you a normalized indication of each country's performance in each edition.
#
# INSTRUCTIONS
# 100 XP
# Set the index of the DataFrame editions to be 'Edition' (using the method .set_index()). Save the result as totals.
# Extract the 'Grand Total' column from totals and assign the result back to totals.
# Divide the DataFrame medal_counts by totals along each row. You will have to use the .divide() method with the option axis='rows'. Assign the result to fractions.
# Print first & last 5 rows of the DataFrame fractions. This has been done for you, so hit 'Submit Answer' to see the results!

# Set Index of editions: totals
totals = editions.set_index('Edition')

# Reassign totals['Grand Total']: totals
totals = totals['Grand Total']

# Divide medal_counts by totals: fractions
fractions = medal_counts.divide(totals, axis='rows')

# Print first & last 5 rows of fractions
print(fractions.head())
print(fractions.tail())

# EXERCISE
# Computing percentage change in fraction of medals won
# Here, you'll start with the DataFrames editions, medals, medal_counts, & fractions from prior exercises.
#
# To see if there is a host country advantage, you first want to see how the fraction of medals won changes from edition to edition.
#
# The expanding mean provides a way to see this down each column. It is the value of the mean with all the data available up to that point in time. If you are interested in learning more about pandas' expanding transformations, this section of the pandas documentation has additional information.
#
# INSTRUCTIONS
# 100 XP
# Create mean_fractions by chaining the methods .expanding().mean() to fractions.
# Compute the percentage change in mean_fractions down each column by applying .pct_change() and multiplying by 100. Assign the result to fractions_change.
# Reset the index of fractions_change using the .reset_index() method. This will make 'Edition' an ordinary column.
# Print the first and last 5 rows of the DataFrame fractions_change. This has been done for you, so hit 'Submit Answer' to see the results!

# Apply the expanding mean: mean_fractions
mean_fractions = fractions.expanding().mean()

# Compute the percentage change: fractions_change
fractions_change = mean_fractions.pct_change()*100

# Reset the index of fractions_change: fractions_change
fractions_change = fractions_change.reset_index()

# Print first & last 5 rows of fractions_change
print(fractions_change.head())
print(fractions_change.tail())

# EXERCISE
# Building hosts DataFrame
# Your task here is to prepare a DataFrame hosts by left joining editions and ioc_codes.
#
# Once created, you will subset the Edition and NOC columns and set Edition as the Index.
#
# There are some missing NOC values; you will set those explicitly.
#
# Finally, you'll reset the Index & print the final DataFrame.
#
# INSTRUCTIONS
# 100 XP
# INSTRUCTIONS
# 100 XP
# Create the DataFrame hosts by doing a left join on DataFrames editions and ioc_codes (using pd.merge()).
# Clean up hosts by subsetting and setting the Index.
# Extract the columns 'Edition' and 'NOC'.
# Set 'Edition' column as the Index.
# Use the .loc[] accessor to find and assign the missing values to the 'NOC' column in hosts. This has been done for you.
# Reset the index of hosts using .reset_index(), and then hit 'Submit Answer' to see what hosts looks like!

# Import pandas
import pandas as pd

# Left join editions and ioc_codes: hosts
hosts = pd.merge(editions, ioc_codes, how='left')

# Extract relevant columns and set index: hosts
hosts = hosts[['Edition', 'NOC']].set_index('Edition')

# Fix missing 'NOC' values of hosts
print(hosts.loc[hosts.NOC.isnull()])
hosts.loc[1972, 'NOC'] = 'FRG'
hosts.loc[1980, 'NOC'] = 'URS'
hosts.loc[1988, 'NOC'] = 'KOR'

# Reset Index of hosts: hosts
hosts = hosts.reset_index()

# Print hosts
print(hosts)

# EXERCISE
# Reshaping for analysis
# This exercise starts off with fractions_change and hosts already loaded.
#
# Your task here is to reshape the fractions_change DataFrame for later analysis.
#
# Initially, fractions_change is a wide DataFrame of 26 rows (one for each Olympic edition) and 139 columns (one for the edition and 138 for the competing countries).
#
# On reshaping with pd.melt(), as you will see, the result is a tall DataFrame with 3588 rows and 3 columns that summarizes the fractional change in the expanding mean of the percentage of medals won for each country in blocks.
#
# INSTRUCTIONS
# 100 XP
# Create a DataFrame reshaped by reshaping the DataFrame fractions_change with pd.melt().
# You'll need to use the keyword argument id_vars='Edition' to set the identifier variable.
# You'll also need to use the keyword argument value_name='Change' to set the measured variables.
# Print the shape of the DataFrames reshaped and fractions_change. This has been done for you.
# Create a DataFrame chn by extracting all the rows from reshaped in which the three letter code for each country ('NOC') is 'CHN'.
# Print the last 5 rows of the DataFrame chn using the .tail() method. This has been done for you, so hit 'Submit Answer' to see the results!

# Import pandas
import pandas as pd

# Reshape fractions_change: reshaped
reshaped = pd.melt(fractions_change, id_vars='Edition', value_name='Change')

# Print reshaped.shape and fractions_change.shape
print(reshaped.shape, fractions_change.shape)

# Extract rows from reshaped where 'NOC' == 'CHN': chn
chn = reshaped.loc[reshaped.NOC == 'CHN']

# Print last 5 rows of chn with .tail()
print(chn.tail())

# EXERCISE
# Merging to compute influence
# This exercise starts off with the DataFrames reshaped and hosts in the namespace.
#
# Your task is to merge the two DataFrames and tidy the result.
#
# The end result is a DataFrame summarizing the fractional change in the expanding mean of the percentage of medals won for the host country in each Olympic edition.
#
# INSTRUCTIONS
# 100 XP
# Merge reshaped and hosts using an inner join. Remember, how='inner' is the default behavior for pd.merge().
# Print the first 5 rows of the DataFrame merged. This has been done for you. You should see that the rows are jumbled chronologically.
# Set the index of merged to be 'Edition' and sort the index.
# Print the first 5 rows of the DataFrame influence. This has been done for you, so hit 'Submit Answer' to see the results!

# Import pandas
import pandas as pd

# Merge reshaped and hosts: merged
merged = pd.merge(reshaped, hosts, how='inner')

# Print first 5 rows of merged
print(merged.head())

# Set Index of merged and sort it: influence
influence = merged.set_index('Edition').sort_index()

# Print first 5 rows of influence
print(influence.head())

# EXERCISE
# Plotting influence of host country
# This final exercise starts off with the DataFrames influence and editions in the namespace. Your job is to plot the influence of being a host country.
#
# INSTRUCTIONS
# 100 XP
# Create a Series called change by extracting the 'Change' column from influence.
# Create a bar plot of change using the .plot() method with kind='bar'. Save the result as ax to permit further customization.
# Customize the bar plot of change to improve readability:
# Apply the method .set_ylabel("% Change of Host Country Medal Count") toax.
# Apply the method .set_title("Is there a Host Country Advantage?") to ax.
# Apply the method .set_xticklabels(editions['City']) to ax.
# Reveal the final plot using plt.show().

# Import pyplot
import matplotlib.pyplot as plt

# Extract influence['Change']: change
change = influence['Change']

# Make bar plot of change: ax
ax = change.plot(kind='bar')

# Customize the plot to improve readability
ax.set_ylabel("% Change of Host Country Medal Count")
ax.set_title("Is there a Host Country Advantage?")
ax.set_xticklabels(editions['City'])

# Display the plot
plt.show()
