from flask import Flask, render_template, make_response, jsonify, request, redirect, url_for

import numpy as np
import pandas as pd

# import matplotlib.pyplot as plt
# import seaborn as sns

import folium
from folium.plugins import MarkerCluster

import geopandas as gpd

app = Flask(__name__)

@app.route('/')
def index():
    state_geo = gpd.read_file('./data/seoul_geo_sigugun.json')
    df = pd.read_csv('./data/집계구별 일별소비지역별 카드소비패턴.csv', encoding='cp949')
    df = df.dropna()

    state_list = state_geo['name'].values.tolist()
    gdf = df[df['가맹점주소시군구(SGG)'].isin(state_list)].groupby('가맹점주소시군구(SGG)')['카드이용금액계(AMT_CORR)'].mean()
    gdf = gdf.reset_index()

    map = folium.Map(location=[37.562225, 126.978555], tiles="OpenStreetMap", zoom_start=11)

    map.choropleth(
        geo_data=state_geo,
        name='인구밀도',
        data=gdf,
        columns=['가맹점주소시군구(SGG)', '카드이용금액계(AMT_CORR)'],
        key_on='feature.properties.name',
        fill_color='Reds',  # if state_geo["code"].str == '11250' else 'Reds',      # 'Blues',
        fill_opacity=0.7,
        line_opacity=0.3,
        color='gray',
        legend_name='income'
    )

    folium.plugins.MousePosition().add_to(map)

    map.get_root().width = "800px"
    map.get_root().height = "600px"
    html_str = map.get_root()._repr_html_()

    # # Save to html
    # # m.save('kr_incode.html')
    # # webbrowser.open_new("folium_kr.html")

    return render_template('maptest.html', KEY_MAP=html_str)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)