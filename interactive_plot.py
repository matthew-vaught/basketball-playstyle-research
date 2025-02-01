import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import SpectralEmbedding
from mpl_toolkits.mplot3d import Axes3D
from sklearn.manifold import TSNE
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import pairwise_distances
from sklearn.metrics import pairwise_distances_argmin_min
from scipy.cluster.hierarchy import ward, fcluster
from scipy.cluster.hierarchy import dendrogram, linkage
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.io import output_notebook
from bokeh.models import ColorBar
from bokeh.transform import linear_cmap
from bokeh.palettes import Viridis256
from bokeh.plotting import figure, show
from bokeh.models import Slider
from bokeh.layouts import column
from bokeh.io import show
from bokeh.io import curdoc

# Read in the basketball-reference dataframe
df = pd.read_csv(r"C:\Users\vaugh\Desktop\basketball-pf-research\Basketball-reference data\df_with_all_positions(2001-2024).csv")
df.set_index(['Season', 'Player'], inplace=True)

# Cleaning up the dataframe
df.rename(columns = {'PF': 'Personal Fouls Committed'}, inplace=True)
df.rename(columns = {'Fouls Drawn - Shoot': 'Shooting Fouls Drawn'}, inplace=True)
df.drop(columns = ['% of FGA by Distance - 2P', 'FG'], inplace=True)

# Removing any players named "Player"
df.reset_index(inplace=True)
df = df[df['Player'] != 'Player']
df.set_index(['Season', 'Player'], inplace=True)

positions = ['PG', 'SG', 'SF', 'PF', 'C']
dfs_by_position = {}
for position in positions:
    dfs_by_position[position] = df[df['Pos'] == position]
    dfs_by_position[position] = dfs_by_position[position].drop(columns=['Pos'])

for df in dfs_by_position:
    # Changing all the values in the df to be floats so that I can apply PCA
    dfs_by_position[df].fillna(0, inplace=True)  # Filling NaNs with 0
    dfs_by_position[df] = dfs_by_position[df].astype(float)

    # Replacing any infinite values with 0
    dfs_by_position[df].replace([np.inf, -np.inf], 0, inplace=True)

    per_48_stats = ['FGA', 'Personal Fouls Committed', 'BLK', 'STL', 'DRB', 'ORB', 'TOV', 'AST']

    for stat in per_48_stats:
        dfs_by_position[df][stat] = dfs_by_position[df][stat] / (dfs_by_position[df]['MP'] / dfs_by_position[df]['G']) * 48

    ordered_cols = ['G', 'MP', 'USG%', 'FGA', 'Personal Fouls Committed', 'BLK', 'STL', 'DRB', 'ORB', 'TOV', 'AST', "% of FG Ast'd - 3P", "% of FG Ast'd - 2P", 'FTr', 'Shooting Fouls Drawn', 'Corner 3s - %3PA', '% of FGA by Distance - 3P', '% of FGA by Distance - 16-3P', '% of FGA by Distance - 10-16', '% of FGA by Distance - 3-10', '% of FGA by Distance - 0-3', 'Dunks - %FGA', ]
    dfs_by_position[df] = dfs_by_position[df].reindex(columns = ordered_cols)

for df in dfs_by_position:
    # Filter out players who played less than 20 games or 10 min/game in a season
    dfs_by_position[df] = dfs_by_position[df][(dfs_by_position[df]['G'] >= 20) & ((dfs_by_position[df]['MP'] / dfs_by_position[df]['G']) >= 10)]

    # Drop the G and MP columns as well as the Shooting Fouls column
    dfs_by_position[df] = dfs_by_position[df].drop(columns = ['G', 'MP', 'Shooting Fouls Drawn'])

pg_df = dfs_by_position['PG']
sg_df = dfs_by_position['SG']
sf_df = dfs_by_position['SF']
pf_df = dfs_by_position['PF']
c_df = dfs_by_position['C']

pf_df = pf_df.drop(columns = ['Dunks - %FGA', 'Personal Fouls Committed'])
pf_df['TRB'] = pf_df['ORB'] + pf_df['DRB']

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(pf_df)
scaled_df = pd.DataFrame(scaled_data, columns=pf_df.columns, index=pf_df.index)

# Drop the two REB columns in favor of TRB
condensed_scaled_df = scaled_df.drop(columns = ['ORB', 'DRB'])

embedding = SpectralEmbedding(n_components=2, affinity='rbf')
transformed_data = embedding.fit_transform(condensed_scaled_df)

le_plotted_df = condensed_scaled_df.reset_index()
le_plotted_df['LE1'] = transformed_data[:, 0]
le_plotted_df['LE2'] = transformed_data[:, 1]
le_plotted_df['color'] = 'NA'

# Initialize the ColumnDataSource
source = ColumnDataSource(le_plotted_df)

# Define a color map for the default color (gray)
gray_color = '#D3D3D3'

# Create the figure with the updated points
p = figure(
    title='LE Projection of Basketball Data - Power Forwards (Season Highlight)',
    x_axis_label='Component 1',
    y_axis_label='Component 2',
    width=800,
    height=600,
    tools='pan, wheel_zoom, box_zoom, reset, save'
)

# Scatter plot where points are colored based on the season selection
p.scatter(
    x='LE1',
    y='LE2',
    source=source,
    size=10,
    alpha=0.7,
    color='color',
    legend_label='Power Forwards'
)

# Create a slider for season selection
season_slider = Slider(start=2001, end=2024, value=2001, step=1, title="Season")

# Define a function to update the plot based on the selected season
def update_season(attr, old, new):
    season = season_slider.value
    # Highlight points from the selected season in blue, and set others to gray
    le_plotted_df['color'] = [
        gray_color if season != row['Season'] else 'blue' 
        for _, row in le_plotted_df.iterrows()
    ]
    # Update the data source with the new colors
    source.data = {
        'LE1': le_plotted_df['LE1'],
        'LE2': le_plotted_df['LE2'],
        'Season': le_plotted_df['Season'],
        'color': le_plotted_df['color']
    }

# Attach the callback function to the slider's value change
season_slider.on_change('value', update_season)

# Layout the plot with the season slider
layout = column(p, season_slider)

# Attach layout to the document
curdoc().add_root(layout)