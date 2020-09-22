import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

# set style 
plt.style.use('bmh')
# Load data
df = pd.read_excel('book_list.xlsx')

# How many books towards my goal have I finished?
start_date = dt.datetime(2020,1,1)
today_date = dt.date.today()
end_date = dt.datetime(2020,12,31)
dates = pd.DataFrame(index=pd.date_range(start_date,today_date))
books = df.groupby(by='Finish Date')['Title'].count()
books = dates.join(books)
books.fillna(0, inplace=True)
books['rolling_count'] = books.cumsum()
books = books[['rolling_count']]
dates = pd.DataFrame(index=pd.date_range(start_date, end_date))
books = dates.join(books)
books.fillna(0, inplace=True)
ax = books.plot(kind='area', figsize=(12,10))
ax.plot(dates, (200/365)*dates, 'g')
ax.set_yticks([0, 25, 50, 75, 100, 125, 150, 175, 200])
ax.set_xlabel('Date', labelpad=10, weight='bold', size=12)
ax.set_ylabel('Books Read', labelpad=10, weight='bold', size=12)
ax.set_title('Books Read Towards My Yearly Goal of 200 Books', pad=20, weight='bold', size=18)
ax.legend(labels=['Books Read'])
read = int(books['rolling_count'].max())
ax.text(today_date, read, 'As of Today: %s' % (read), weight='bold')
q1 = books['rolling_count'].loc['20200331']
ax.text(dt.datetime(2020,3,1), q1, 'Q1: %s' % (int(q1)))
q2 = books['rolling_count'].loc['20200630']
ax.text(dt.datetime(2020,6,1), q2-5, 'Q2: %s' % (int(q2)))
plt.savefig('goal_progress.png')
plt.close()


# What is my average rating?
ratings = df.groupby(by='Type').agg({'Title':'count','Rating':'mean'})

# Plot average ratings by format
spines_ = ['right', 'top', 'left', 'bottom']
colors=['#0B1441', '#10227C', '#1837D2']
ax = ratings['Rating'].plot(kind='barh', color=colors, figsize=(12,10))
for spine in spines_:
    ax.spines[spine].set_visible(False)
ax.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=True, left=False, right=False, labelleft=True)
ax.set_xticks([])
ax.set_xlabel('My Average Rating', labelpad=20, weight='bold', size=12)
ax.set_ylabel('Book Format', labelpad=20, weight='bold', size=12)
ax.set_title('My Average Book Rating by Format', weight='bold', size=18)
for i,v in enumerate(ratings['Rating']):
    ax.text(v+.1, i, str("{:.2f}".format(v)), weight='bold')
plt.savefig('rating_format.png')
plt.close()

