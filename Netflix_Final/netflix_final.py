
# coding: utf-8

#  

# # Introduction
# 
# In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the "Netflix Stock Profile" team visualize the Netflix stock data. In finance, _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. 
# 
# 
# For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:
# + The distribution of the stock prices for the past year
# + Netflix's earnings and revenue in the last four quarters
# + The actual vs. estimated earnings per share for the four quarters in 2017
# + A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017
# 
# During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.
# 
# After you complete your visualizations, you'll be creating a presentation to share the images with the rest of the Netflix Stock Profile team.
# 
# Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)
# 

# ## Step 1
# 
# Let's get our notebook ready for visualizing! Import the modules that you'll be using in this project:
# - `from matplotlib import pyplot as plt`
# - `import pandas as pd`
# - `import seaborn as sns`

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# ## Step 2

# Load the datasets and inspect them:

# Load **NFLX.csv** into a DataFrame called `netflix_stocks`. Then, quickly inspect the DataFrame using `.head()`.
# 
# (Hint: Use the `pd.read_csv()`function).
# 
# Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits.

# In[2]:


netflix_stocks = pd.read_csv('NFLX.csv')
print(netflix_stocks.head(5))


# Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `.head()`.
# 
# Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). 
# 

# In[3]:


dowjones_stocks = pd.read_csv('DJI.csv')
print(dowjones_stocks.head())


# ## Step 3

# Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.
#  - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly
#  - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.
#  - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). 
# 
# 
# Answer the following questions by inspecting the data in the **NFLX.csv** and **DJI.csv**

# What year is represented in the data?

# In[4]:


#2017


# Is the data represented by days, weeks, or months?

# In[5]:


#months


# In[6]:


print(netflix_stocks.head())


# ## Step 4
# 
# Great! Now that we have spent sometime looking at the data, let's look at the column names of the DataFrame `netflix_stocks` using `.head()`. 

# In[7]:


print(netflix_stocks.head())


# What do you notice? The first two column names are one word each, and the only one that is not is Adj Close! `Adj Close` is ambivalent, but as Yahoo adjusts the price, this will a very important metric for analyzing how Netflix performed.
# 
# Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work with the data. 
# 
# Do this for the Dow Jones pandas dataframe as well.
# 
# (Hint: Use `.rename()`. [You can read the documentation here.](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)).

# In[8]:


netflix_stocks.rename(columns = {'Adj Close' : 'Price'},inplace=True)
dowjones_stocks.rename(columns = {'Close' : 'Price'},inplace=True)
print(netflix_stocks.head())


# Run `netflix_stocks.head()` again to check your new column name worked.

# Call `.head()` on the DataFrame `dowjones_stocks`.

# In[9]:


print(dowjones_stocks.head())


# ## Step 5
# 
# We want to visualize the distribution of the Netflix stock prices to see the range of prices for 2017. We will do this using a violin plot.
# 
# 1. Plot the `Price` of the `netflix_stocks` DataFrame on a Seaborn `.violinplot()`
# Since the logo of Netflix is red, assign the color `"red"` as a Parameter when you visualize the plot.
# 
# 2. Start by setting the variable `ax` equal to `sns.violinplot()`. This will instantiate a figure and give us access to the axes through the variable name `ax`. 
# 3. Improve the readability of the chart by adding a title of the plot. Add `""Distribution of 2017 Netflix Stock Price"` by using `ax.set_title()`
# 4. Be sure to show your plot!
# 

# In[10]:


ax=sns.violinplot(data=netflix_stocks,y='Price',palette='hls')
ax.set_title("Distribution of 2017 Netflix Stock Price" )
plt.savefig("NFLX_Dist_vio.png")
plt.show()


# ## Graph Literacy
# - What are your first impressions looking at the visualized data?
# 
# - In what range(s) did most of the prices fall throughout the year?
# 
# - What were the highest and lowest prices? 

# In[11]:


#For 2017, Netflix stock prices ranged from a low of $120 to a high of $220.
#The median stock prices were around $170.
#The majority of prices cleared between $140 and $180. 


# ## Step 6
# 
# Next, we will chart the performance of the dividends per share by graphing the estimate Yahoo projected for the Quarter compared to the actual dividends for that quarters. We will accomplish this using a scatter chart. 
# 
# 1. Plot the actual dividends by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.
# 2. Plot the actual dividends by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color
# 
# 3. Often, estimates and actual dividendss are the same. To account for this, be sure to set your transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.
# 4. Add a legend by using `plt.legend()` and passing in a list with two strings `["Actual", "Estimate"]`
# 
# 5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`
# 6. Assing "`"Dividends per share in cents"` as the title of your plot.
# 

# In[12]:


x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]
plt.scatter(x_positions,earnings_actual,color='red',alpha=0.5)
plt.scatter(x_positions,earnings_estimate,color='blue',alpha=0.5)
plt.legend(["Actual","Estimate"])
plt.xticks(x_positions,chart_labels)
plt.title("Dividends per share in cents")
plt.savefig("NFLX_div_act_est.png")
plt.show()


# ## Graph Literacy
# 
# + What do the purple dots tell us about the actual and estimate dividends in this graph? (Hint: In color theory red and blue mix to make purple.)
# 

# In[13]:


#In 2Q2017 actual dividends were the same as estimated dividends (0.15) therefore the red (estimated) and blue (actual) plots overlap, creating a purple dot. 


#  

# ## Step 6

# Next, we will visualize Netflix company revenue and earnings by mapping two bars side-by-side. We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).
# 
# As you may recall, plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand. We have pasted the starter code for that exercise below. 
# 
# 1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars
# 2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data
# 3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars
# 4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data
# 5. Create a legend for your bar chart with the `labels` provided
# 6. Add a descriptive title for your chart with `plt.title()`
# 7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`
# 8. Be sure to show your plot!
# 

# In[14]:


# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

#earnings as percentage of revenue
#percentage_of_revenue =[(.0656/2.79)*100,(.12959/2.98)*100,(.18552/3.29)*100,(.29012/3.7)*100]
#print(percentage_of_revenue)

# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars1_x = [t*element + w*n for element
           in range(d)]

# Earnings
n = 2 #This is our second dataset (out of 2)
t = 2 #Number of dataset
d = 4 #Number of sets of bars
w = 0.8 #Width of each bar
bars2_x = [t*element + w*n for element
           in range(d)]

middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]

plt.bar(bars1_x,revenue_by_quarter, color ='blue')
plt.bar(bars2_x,earnings_by_quarter, color ='green')
plt.title('Netflix Revenue vs Earnings, Quarterly')
plt.legend(["Revenue","Earnings"], loc=2)
plt.xlabel("Quarter")
plt.ylabel("$ Billions")
plt.xticks(middle_x, quarter_labels)
plt.savefig("NFLX_rev_ear.png")
plt.show()


# ## Graph Literacy
# What are your first impressions looking at the visualized data?
# 
# - Does Revenue follow a trend?
# - Do Earnings follow a trend?
# - Roughly, what percentage of the revenue constitutes earnings?

# In[15]:


#Revenue and earnings both increase each quarter, at a similar magnitude. 
#Earnings are around 2% to 7% of earnings through all quarters.


# ## Step 7
# 
# In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. 
# 
# Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.
# - We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot
#     - `1`-- the number of rows for the subplots
#     - `2` -- the number of columns for the subplots
#     - `1` -- the subplot you are modifying
# 
# - Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`netflix_stocks['Date'], netflix_stocks['Price']`)
# - Assign "Netflix" as a title to this subplot. Hint: `plt.set_title()`
# - For each subplot, `set_xlabel` to `"Date"` and `set_ylabel` to `"Stock Price"`
# - Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`dowjones_stocks['Date'], dowjones_stocks['Price']`)
# - Assign "Dow Jones" as a title to this subplot. Hint: `plt.set_title()`
# - There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`
# - Be sure to `.show()` your plots.
# 

# In[29]:


# Left plot Netflix
# ax1 = plt.subplot(total rows, total columns, subplot to modify)
ax1 = plt.subplot(1, 2, 1)
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Price')
ax1.set_title("Netflix")
plt.xticks(rotation='vertical')
plt.plot(netflix_stocks['Date'], netflix_stocks['Price'], color="red")

# Right plot Dow Jones
# ax2 = plt.subplot(total rows, total columns, subplot to modify)
ax2 = plt.subplot(1, 2, 2)
ax2.set_xlabel('Date')
ax2.set_ylabel('Stock Price')
ax2.set_title("Dow Jones")
plt.xticks(rotation='vertical')
plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'], color="blue")

plt.subplots_adjust(wspace=.5)
plt.subplots_adjust(hspace=5)
plt.savefig("NFLX_DOW.png")
plt.show()


# - How did Netflix perform relative to Dow Jones Industrial Average in 2017?
# - Which was more volatile?
# - How do the prices of the stocks compare?

# In[17]:


#Overall, Netflix stock increased in value in line with the Dow Jones Industrial Average
#Netflix was more volatile compared with the Dow. 
#Netflix outperformed the DJIA, increasing 36.42% during 2017, compared to the DJIA increasing 24.44%.


#  

# # Step 9
# 
# It's time to make your presentation! Save each of your visualizations as a png file with `plt.savefig("filename.png")`.
# 
# As you prepare your slides, think about the answers to the graph literacy questions. Embed your observations in the narrative of your slideshow!
# 
# Remember that your slideshow must include:
# - A title slide
# - A list of your visualizations and your role in their creation for the "Stock Profile" team
# - A visualization of the distribution of the stock prices for Netflix in 2017
# - A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary
# - A visualization and a brief summary of their earned versus actual dividends
# - A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017
# 
