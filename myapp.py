import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Baca dataset
data = pd.read_csv('netflix_titles.csv')

# Tampilkan judul halaman
st.title('Visualisasi Data Netflix')

# Tampilkan dataset
st.subheader('Data Netflix')
st.dataframe(data)

# Tampilkan beberapa visualisasi
st.subheader('Visualisasi Data')

# Pilih tipe konten untuk ditampilkan
content_type = st.selectbox('Tampilkan Berdasarkan Genre', ['TV Shows', 'International TV Shows', 'Anime Series', 'Crime TV Shows', 'TV Dramas',
                                                            'Romantic TV Shows', 'Docuseries', 'International Movies', 'Sci-Fi & Fantasy', 'Thrillers',
                                                            'Action & Adventure', 'Dramas', 'Horror Movies', 'Stand-Up Comedy', 'Children & Family Movies',
                                                            'Movies', 'Romantic Movies', 'Comedies', 'Music & Musicals', 'Classic Movies', 'Sports Movies',
                                                            'Reality TV', 'LGBTQ Movies', 'Cult Movies', 'Independent Movies', 'Teen TV Shows',
                                                            'British TV Shows', "Kids' TV", 'Spanish-Language TV Shows',
                                                            'Korean TV Shows', 'Faith & Spirituality', 'Stand-Up Comedy & Talk Shows',
                                                            'TV Action & Adventure', 'TV Comedies', 'TV Mysteries', 'TV Sci-Fi & Fantasy',
                                                            'TV Thrillers', 'Romantic International Movies', 'Classic & Cult TV', 'Science & Nature TV',
                                                            'TV Horror', 'TV Shows based on Comics', 'TV Shows based on Books', 'Movies based on Books',
                                                            'Children & Family Movies, Dramas', 'Romantic Movies, Sci-Fi & Fantasy',
                                                            'TV Dramas, TV Sci-Fi & Fantasy', 'Action & Adventure, Thrillers', 'Anime Features', 'Anime Fantasies',
                                                            'TV Comedies, TV Dramas', 'Movies, Thrillers', 'Sci-Fi & Fantasy, Thrillers',
                                                            'Children & Family Movies, Comedies', 'Children & Family Movies, Music & Musicals',
                                                            'Anime Series, International TV Shows', 'Movies, Sci-Fi & Fantasy',
                                                            'TV Action & Adventure, TV Sci-Fi & Fantasy', 'Comedies, Dramas', 'TV Comedies, TV Thrillers',
                                                            'Dramas, Independent Movies', 'Romantic Movies, Stand-Up Comedy',
                                                            'Action & Adventure, Children & Family Movies', 'Action & Adventure, Independent Movies',
                                                            'Comedies, Music & Musicals', 'Dramas, International Movies', 'Comedies, Romantic Movies',
                                                            'Dramas, Faith & Spirituality', 'Action & Adventure, Comedies', 'Classic & Cult TV, Crime TV Shows',
                                                            'Romantic TV Shows, TV Dramas', 'TV Dramas, Teen TV Shows', 'Action & Adventure, Sci-Fi & Fantasy',
                                                            'Dramas, Romantic Movies', 'TV Action & Adventure, TV Comedies', 'TV Mysteries, TV Thrillers',
                                                            'Children & Family Movies, Classic Movies', 'Dramas, Independent Movies, Romantic Movies',
                                                            'Horror Movies, International Movies', 'Dramas, LGBTQ Movies', 'Horror Movies, Thrillers',
                                                            'Action & Adventure, International Movies', 'Children & Family Movies, International Movies',
                                                            'Classic Movies, Cult Movies', 'Comedies, International Movies', 'Comedies, Independent Movies',
                                                            'Documentaries, International Movies', 'Dramas, Horror Movies', 'Dramas, International Movies, Thrillers',
                                                            'Dramas, Music & Musicals', 'Dramas, Music & Musicals, Romantic Movies',
                                                            'Dramas, Music & Musicals, Sports Movies', 'Dramas, Romantic Movies, Sports Movies',
                                                            'Dramas, Sci-Fi & Fantasy', 'Dramas, Sci-Fi & Fantasy, Thrillers', 'Dramas, Sports Movies',
                                                            'Horror Movies, Independent Movies', 'Horror Movies, Sci-Fi & Fantasy',
                                                            'Independent Movies, Romantic Movies', 'International Movies, Romantic Movies',
                                                            'Music & Musicals, Romantic Movies', 'Romantic International Movies, Thrillers',
                                                            'Sci-Fi & Fantasy, Sports Movies', 'Sports Movies, Thrillers'])

# Filter dataset berdasarkan tipe konten yang dipilih
filtered_data = data[data['listed_in'] == content_type]

# Visualisasi jumlah film dan acara TV berdasarkan tipe konten
st.markdown('### Jumlah Film dan Acara TV')
content_type_counts = filtered_data['listed_in'].value_counts()
plt.figure(figsize=(8, 6))
sns.set(style="darkgrid")
sns.barplot(x=content_type_counts.index, y=content_type_counts.values)
plt.xlabel('Genre')
plt.ylabel('Jumlah')
plt.title('Jumlah Film dan Acara TV')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Tampilkan slider untuk memilih jumlah negara yang ditampilkan
num_countries = st.slider('Jumlah Negara yang Ditampilkan', min_value=5, max_value=20, value=10)

# Visualisasi jumlah konten berdasarkan negara
st.markdown(f'### Jumlah Konten per Negara (Top {num_countries})')
country_counts = filtered_data['country'].value_counts().head(num_countries)
plt.figure(figsize=(12, 6))
sns.set(style="darkgrid")
sns.barplot(x=country_counts.values, y=country_counts.index)
plt.xlabel('Jumlah Konten')
plt.ylabel('Negara')
plt.title(f'Jumlah Konten per Negara (Top {num_countries})')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Visualisasi jumlah konten berdasarkan tahun rilis
st.markdown('### Jumlah Konten per Tahun Rilis')
release_year_counts = filtered_data['release_year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
sns.set(style="darkgrid")
sns.lineplot(x=release_year_counts.index, y=release_year_counts.values)
plt.xlabel('Tahun Rilis')
plt.ylabel('Jumlah Konten')
plt.title('Jumlah Konten per Tahun Rilis')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()