import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML, Image

df = pd.read_csv('test.csv',usecols=['name','group','year','value'])
colors = dict(zip(['Taiwan','Canada','America'],['#adb0ff','#ffb3ff','#90d595']))
group_lk = df.set_index('name')['group'].to_dict()
fig, ax = plt.subplots(figsize=(15, 8))

def draw_barchart(year):
    dff = df[df['year'].eq(year)].sort_values(by='value', ascending=True).tail(10)
    ax.clear()
    ax.barh(dff['name'], dff['value'], color = [colors[group_lk[x]] for x in dff['name']])
    dx = dff['value'].max() / 200
    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        ax.text(value-dx, i, name,           size=14, weight=600, ha='right', va='bottom')
        ax.text(value-dx, i-.25 , group_lk[name], size=10, color='#444444', ha='right', va='baseline')
        ax.text(value+dx, i, f'{value:,.0f}', size=14, ha='left', va='center')
    ax.text(1, 0.4, year, transform = ax.transAxes, size = 46, ha='right', weight=800)
    ax.text(0, 1.06, 'Population', transform = ax.transAxes, size = 12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 0.12, 'TestTestTest', transform = ax.transAxes, size = 24, ha='left', weight=600)
    plt.box(False)

# draw_barchart(2018)

animator = animation.FuncAnimation(fig, draw_barchart, frames=range(1980,2021))
# <-------- 轉換成HTML -------->
# target = HTML(animator.to_jshtml()
# html = target.data
# with open('html_file.html', 'w') as f:
#     f.write(html)

# <-------- 轉換成GIF -------->
# animator.save('animation.gif', writer='Pillow', fps=120)

# <-------- 轉換成MP4 -------->
FFwriter = animation.FFMpegWriter()
animator.save('animation.mp4', fps=8)
