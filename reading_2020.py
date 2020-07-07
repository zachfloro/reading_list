import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel('book_list.xlsx')

# What is my average rating?
ratings = df.groupby(by='Type').agg({'Title':'count','Rating':'mean'})

# Plot average ratings as bar with number of titles annotated
spines_ = ['right', 'top', 'left', 'bottom']
ax = ratings['Rating'].plot(kind='barh', color='#1837D2')
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
