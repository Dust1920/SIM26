import geopandas as gpd
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from auxiliar import arrow,text_block


def mexico_map(colors: ListedColormap, col_data: str, mexico_df: gpd.GeoDataFrame, **kwargs):
    title = kwargs.get('title', None)
    if title == None:
        title = ""
    data2 = kwargs.get('ad_data',None)
    data_text = kwargs.get('ad_text', None)
    saving = kwargs.get('path',None)
    arrow_positions = [(0.490, 0.400), (0.450, 0.260), (0.587, 0.270), 
                    (0.530, 0.340), (0.585, 0.330), (0.560, 0.260), 
                    (0.587, 0.240), (0.420, 0.370), (0.620, 0.250),
                    (0.555, 0.330), (0.780, 0.220), (0.620, 0.270)]
    texti_positions = [(0.350, 0.420), (0.400, 0.200), (0.480, 0.140),
                    (0.700, 0.550), (0.700, 0.450), (0.700, 0.400),
                    (0.600, 0.090), (0.320, 0.360), (0.738, 0.249),
                    (0.700, 0.500), (0.780, 0.280), (0.700, 0.350)]
    ax = mexico_df.plot(col_data, figsize=(20,20), cmap = colors,
                    legend=True, categorical = True, legend_kwds = {
                        'fontsize': 20,
                        'markerscale':2,
                    })

    mexico_df.boundary.plot(lw=0.5, color='black', ax=ax)
    ax.set_axis_off()
    ax.set_title(title, fontsize = 30)

    ax.text(x = 0, y = 1.6e6, s = data_text, fontsize = 18, weight = 'bold')
 
    area_limit = mexico_df.geometry.area['Yucatán']
    mini = 0
    if data2 != None:
        col_data = data2
    ax.text(x = 3.2e6,
            y = 1.9e6,
            fontsize = 18,
            weight = 'bold',
            s = f'Estados Unidos Mexicanos {mexico_df.loc[mexico_df.index[0], col_data] } %')
    for estado in mexico_df.index:
        if estado == 'Estados Unidos Mexicanos':
            continue
        if mexico_df.geometry.area[estado] >= area_limit:
            text_block(mexico_df.loc[estado,'Abreviatura'] + f"\n {mexico_df.loc[estado, col_data]}",
                    mexico_df.loc[estado,:].geometry.centroid.coords[0], ax)
        else:
            _ = arrow(mexico_df.loc[estado,'Abreviatura'] + f"\n {mexico_df.loc[estado, col_data]}",
                    arrow_positions[mini], texti_positions[mini], ax)
            mini +=1
    
    if saving !=None:
        plt.savefig(saving)