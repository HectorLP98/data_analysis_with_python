import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    '''
    Utiliza Pandas para importar los datos de epa-sea-level.csv.
Usa matplotlib para crear un diagrama de dispersión usando la columna 
"Year" como el eje x y la columna "CSIRO Adjusted Sea Level" como el eje y.
    '''
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    #print(df.head())

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df.Year, df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    '''
    Usa la función linregress de scipy.stats para obtener la pendiente e intersección con el 
    eje y de la línea de mejor encaje. Dibuja la línea de mejor encaje sobre el diagrama de dispersión.
    Haz que la línea pase por el año 2050 para predecir el aumento del nivel del mar en ese año.
    '''
    x = df.Year
    y = df['CSIRO Adjusted Sea Level']
    res = linregress(x,y)
    pos = x.index[-1]
    x[pos +1 ]= 2050
    ax.plot(x, res.intercept + res.slope*x, 'r', label='fitted line')

    # Create second line of best fit
    '''
    Traza una nueva línea de mejor encaje utilizando datos del año 2000 hasta el año más reciente del 
    conjunto de datos. Haz que la línea pase también por el año 2050 para predecir la subida del nivel 
    del mar en 2050 si el ritmo de subida continúa como desde el año 2000.
    '''
    df_2000 = df[df.Year >= 2000]
    df_2000.reset_index(drop=True, inplace=True)
    x_2000 = df_2000.Year
    y_2000 = df_2000['CSIRO Adjusted Sea Level']
    #print(len(y_2000), len(x_2000))
    res_2000 = linregress(x_2000,y_2000)
    pos_2000 = x_2000.index[-1]
    #print(pos_2000)
    x_2000[pos_2000 +1 ]= 2050
    ax.plot(x_2000, res_2000.intercept + res_2000.slope*x_2000, 'r', label='fitted line 2000')

    # Add labels and title
    '''
    La etiqueta del eje x debe ser "Year", la etiqueta del eje y debe ser "Sea Level (inches)",
    y el título debe ser "Rise in Sea Level"
    '''
    ax.set(title='Rise in Sea Level', xlabel='Year', ylabel='Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    #plt.savefig('sea_level_plot.png')
    return plt.gca()