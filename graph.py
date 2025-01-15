import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.widgets import Cursor
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import date
from dateutil.relativedelta import relativedelta
import yfinance as yf

sns.set()


def generate_year_graph(ticker):
    end_date = date.today()
    start_date = end_date - relativedelta(years=5)

    price_data = yf.download(ticker, start_date, end_date)
    date_range = (end_date - start_date).days

    price_data.reset_index(inplace=True)
    if isinstance(price_data.columns, pd.MultiIndex):
        price_data.columns = price_data.columns.get_level_values(0)

    # Sets up plot
    fig, ax = plt.subplots(figsize=(14, 10))
    sns.set_style("whitegrid")

    # Line plot
    line = ax.plot(price_data["Date"], price_data["Close"], color="firebrick")[0]

    # Add more ticks to x-axis
    ax = plt.gca()

    # Setup for cursor
    cursor = Cursor(ax, useblit=True, color='red', linewidth=1)

    # Add annotation for hover
    annotation = ax.annotate(
        "", xy=(0, 0), xytext=(-50, 20),
        textcoords="offset points",
        bbox=dict(boxstyle="round", fc="w"),
        arrowprops=dict(arrowstyle="->",)
    )
    annotation.set_visible(False)

    def on_hover(event):
        if event.inaxes == ax:
            xdata = mdates.date2num(line.get_xdata())
            ydata = line.get_ydata()

            if len(xdata) > 0:
                nearest_index = np.abs(xdata - event.xdata).argmin()
                nearest_x = xdata[nearest_index]
                nearest_y = ydata[nearest_index]

                annotation.xy = (nearest_x, nearest_y)
                annotation.set_text(f"Date: {mdates.num2date(nearest_x).strftime('%d-%m-%Y')}\nPrice: ${nearest_y:.2f}")
                annotation.set_visible(True)
                fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", on_hover)

    if date_range <= 31:
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    elif date_range <= 365:
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.xaxis.set_minor_locator(mdates.WeekdayLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    else:
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))

    # Add more ticks to y-axis
    ymin, ymax = price_data['Close'].min(), price_data['Close'].max()
    ytick_range = np.linspace(ymin, ymax, num=10)
    plt.yticks(ytick_range)

    # Labeling for the graph
    plt.title(f"The Stock Price of {ticker}", size='x-large', color='blue')
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Price", fontsize=12)

    # Rotate x-axis for readability
    plt.xticks(rotation=45, ha='right')

    plt.legend()
    plt.show()


