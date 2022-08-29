import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')
df.index = pd.to_datetime(df.index.str.strip())

# Clean data
'''Limpiar los datos filtrando los días en que las vistas de la página se encuentran en el 2,5% 
superior del conjunto de datos o en el 2,5% inferior del conjunto de datos.'''
df = df[(df.value >= df.value.quantile(q=0.025)) & (df.value <= df.value.quantile(q=0.975))]

'''Crea una función llamada draw_line_plot que utilice Matplotlib para dibujar un gráfico de 
línea similar a "examples/Figure_1.png". El título debe ser "Daily freeCodeCamp Forum Page Views
5/2016-12/2019". 
La etiqueta en el eje x debe ser "Date" y la etiqueta en el eje y debe ser "Page Views".'''
def draw_line_plot():
     # Draw line plot
    fig, ax = plt.subplots()
    ax.plot(df.value, color = 'r')
    ax.set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
           xlabel= 'Date',
           ylabel='Page Views')
    plt.show()
   





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
'''
Crea una función llamada draw_bar_plot que dibuje un gráfico de barras similar a "examples/Figure_2.png".
Debe mostrar el número promedio de vistas diarias de cada mes, agrupadas por año. 
La leyenda debe mostrar etiquetas mensuales y tener un título de "Months". En el gráfico, 
la etiqueta en el eje x debe ser "Years" y la etiqueta en el eje y debe ser "Average Page Views".
'''
def draw_bar_plot():
    global df
    # Prepare data for box plots (this part is done!)
    df_bar = df.copy()
    # Copy and modify data for monthly bar plot
 
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    k = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar = k.unstack()


    # Draw bar plot
    fig = df_bar.plot.bar(legend=True, xlabel='Years', ylabel='Average Page Views').figure
    plt.legend(['January', 'February', 'March', 'April','May', 'June', 'July', 'August','September', 'October',
              'November', 'December'], fontsize='x-small')
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=6)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    
    # Draw box plots (using Seaborn)
    fig = plt.figure(figsize=(40,20))
    
    # chart 1
    plt.subplot(1,2,1)
    sns.boxplot(x='year', y='value',data=df_box, linewidth=1)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel("Page Views")
    
    # chart 2 
    plt.subplot(1,2,2)
    sns.boxplot(data=df_box, x='month', y='value', linewidth=1)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.ylabel("Page Views")
    plt.xlabel('Month')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
