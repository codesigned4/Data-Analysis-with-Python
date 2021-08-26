import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()


def quantile(df):
    df = df.sort_values("value")
    lenght = len(df.index) - 1
    removeBottom = int(lenght * 2.5 / 100)
    removeTop = int(lenght * 97.5 / 100)
    df.drop(df.index[removeTop:], inplace=True)
    df.drop(df.index[:removeBottom], inplace=True)
    df = df.sort_index()
    return df


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"])
df.set_index('date', inplace=True)

# Clean data
newDf = quantile(df)


# print(newDf)


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(newDf.index, newDf['value'], color='red', linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


draw_line_plot()


def draw_bar_plot():
    df_bar = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"])

    df_bar = quantile(df_bar)

    df_bar['year'] = pd.DatetimeIndex(df_bar['date']).year
    df_bar['month'] = pd.DatetimeIndex(df_bar['date']).month
    df_bar.drop('date', axis='columns', inplace=True)
    # print(df)
    # print(df.pivot_table(index="year",columns="month",values="value"))
    pivotTable = df_bar.pivot_table(index="year", columns="month", values="value")
    # Plot a bar chart using the DF
    ax = pivotTable.plot(kind="bar", figsize=(7, 7))
    # Get a Matplotlib figure from the axes object for formatting purposes
    fig = ax.get_figure()
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(
        ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
         "December"], title="Months")
    # plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


draw_bar_plot()


def draw_box_plot():
    df_box = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"])

    # Clean data
    df_box = quantile(df_box)

    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    df_box["month_num"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_num")

    # Draw box plots (using Seaborn)

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_figwidth(20)
    fig.set_figheight(10)

    ax1 = sns.boxplot(x=df_box["year"], y=df_box["value"], ax=ax1)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    ax2 = sns.boxplot(x=df_box["month"], y=df_box["value"], ax=ax2)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig


draw_box_plot()
