import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import ssl
import urllib.request

url = 'https://raw.githubusercontent.com/4GeeksAcademy/k-means-project-tutorial/main/housing.csv'

ssl_context = urllib.request.urlopen(url, context=ssl._create_unverified_context())

df = pd.read_csv(ssl_context, index_col=None)

df.to_csv('/Users/andreawendezflores/Documents/GitHub/Clustering/data/raw/california_housing_data', index=False)

