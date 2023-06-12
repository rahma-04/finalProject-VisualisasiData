import pandas as pd
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.models import CategoricalColorMapper
from bokeh.palettes import Spectral6
from bokeh.layouts import widgetbox, row
from bokeh.models import Slider, Select

# Membaca dataset Netflix Movies and TV Shows
data = pd.read_csv("netflix_titles.csv")

# Membuat list dari nilai unik dalam kolom "type"
type_list = data.type.unique().tolist()

# Membuat color mapper
color_mapper = CategoricalColorMapper(factors=type_list, palette=Spectral6)

# Membuat ColumnDataSource
source = ColumnDataSource(data={
    'x': data.release_year,
    'y': data.duration,
    'title': data.title,
    'type': data.type
})

# Membuat plot
plot = figure(title='Netflix Movies and TV Shows', x_axis_label='Release Year', y_axis_label='Duration',
              plot_height=400, plot_width=700, tools=[HoverTool(tooltips='@title')])

# Menambahkan lingkaran ke plot
plot.circle(x='x', y='y', source=source, fill_alpha=0.8,
            color=dict(field='type', transform=color_mapper), legend='type')

# Menentukan posisi legenda
plot.legend.location = 'top_left'

# Fungsi callback untuk memperbarui plot
def update_plot(attr, old, new):
    selected_type = type_select.value
    min_duration = duration_slider.value[0]
    max_duration = duration_slider.value[1]
    new_data = {
        'x': data[(data.type == selected_type) & (data.duration >= min_duration) & (data.duration <= max_duration)].release_year,
        'y': data[(data.type == selected_type) & (data.duration >= min_duration) & (data.duration <= max_duration)].duration,
        'title': data[(data.type == selected_type) & (data.duration >= min_duration) & (data.duration <= max_duration)].title,
        'type': data[(data.type == selected_type) & (data.duration >= min_duration) & (data.duration <= max_duration)].type
    }
    source.data = new_data

# Membuat dropdown menu untuk memilih jenis konten (type)
type_select = Select(title='Type', options=type_list, value=type_list[0])
type_select.on_change('value', update_plot)

# Membuat slider untuk memilih rentang durasi
duration_slider = Slider(title='Duration Range', start=data.duration.min(), end=data.duration.max(),
                         value=(data.duration.min(), data.duration.max()), step=1)

duration_slider.on_change('value', update_plot)

# Membuat layout
layout = row(widgetbox(type_select, duration_slider), plot)

# Menambahkan layout ke curdoc
curdoc().add_root(layout)
