import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 

df = pd.read_csv('spotify .csv', index_col=0) 
df.sort_values('song_popularity', ascending=False, inplace=True) #Songs in order of popularity


print(df.head(15))
print(df.head())
print(df.info()) 
print(df.describe())

duplicados = df[df.duplicated(keep='first')]
print(duplicados)
df.drop_duplicates(keep='first', inplace=True) 

# inconsistencies
def remove_units (DataFrame, columns, what):
    for col in columns:
        DataFrame[col] = DataFrame[col].str.strip(what)
 
remove_units(df, ['acousticness', 'danceability'], 'mol/L')
remove_units(df, ['song_duration_ms', 'acousticness'], 'kg')
print (type(np.nan))

df = df.replace(['nao_sei'], np.nan)
df['key'] = df['key'].replace([0.177], np.nan)
df['audio_mode'] = df['audio_mode'].replace(['0.105'], np.nan)
df['speechiness'] = df['speechiness'].replace(['0.nao_sei'], np.nan)
#df['time_signature' = df['time_signature'].replace(['0.7'], '2800000000'], np.nan)
print(df.info()) 

numerical_cols = ['song_duration_ms', 'acousticness', 'danceability',
                  'energy', 'instrumentalness', 'liveness', 'loudness',
                  'speechiness', 'tempo', 'audio_valence']
 
categorical_cols = ['song_popularity', 'key', 'audio_mode', 'time_signature']
 
def to_type(DataFrame, columns, type):
    for col in columns:
        DataFrame[col] = DataFrame[col].astype(type)
 
to_type(df, numerical_cols, 'float')
to_type(df, categorical_cols, 'category')

print(df.info())

def exclui_outliers(DataFrame, col_name):
  intervalo = 2.7*DataFrame[col_name].std()
  media = DataFrame[col_name].mean()
  DataFrame.loc[df[col_name] < (media - intervalo), col_name] = np.nan
  DataFrame.loc[df[col_name] > (media + intervalo), col_name] = np.nan

  numerical_cols = ['song_duration_ms', 'acousticness', 'danceability',
                  'energy', 'instrumentalness', 'liveness', 
                  'loudness', 'speechiness', 'tempo','audio_valence']
for col in numerical_cols:
  exclui_outliers(df, col)
  
# null data
  numerical_cols = ['song_duration_ms', 'acousticness', 'danceability',
                  'energy', 'instrumentalness', 'liveness', 
                  'loudness', 'speechiness', 'tempo','audio_valence']


df.dropna(inplace=True)