

import ssl
import urllib.request
import streamlit as st
import pandas as pd
import gzip
import io
import numpy as np

st.title('Budget Analysis')
st.header('2023 Zambia Budget Analysis')
st.subheader('Conversational Approach')

#Load Data

context = ssl._create_unverified_context()

DATE_COLUMN = 'date/time'
DATA_URL = urllib.request.urlopen('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz', context = context)

#with gzip.open(DATA_URL, 'rt', encoding='utf-8') as file:
 #   content = file.read()

@st.cache_data
def load_data(nrows):

    with gzip.open(DATA_URL,'rt', encoding='utf-8') as file:
        data = pd.read_csv(file, nrows = nrows)

    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
deta = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')
