from flask import Flask, session, render_template, make_response, jsonify, request, redirect, url_for
import cx_Oracle
import random

app = Flask(__name__)
app.secret_key = "1111122222"


@app.route('/')
def index():
    return render_template('index01.html')

@app.route('/form_get', methods = ['GET'])
def form_get():
    id = request.args.get("userid")
    pw = request.args.get("userpw")
    print("id: ",id)
    print("pw: ",pw)
    return render_template('result01.html', KEY_MYDATA=[id,pw])

@app.route('/form_post', methods = ['POST'])
def form_post():
    id = request.form.get("userid")
    pw = request.form.get("userpw")
    var_list = [id,pw]
    var_list_dict = [{"KID": id, "KPW": pw},
                     {"KID": "kim", "KPW": 111},
                     {"KID": "park", "KPW": 222}]
    return render_template('result01.html', KEY_MYDATA=var_list_dict)

@app.route('/form_rest_text_text', methods=['POST'])
def form_rest_text_text():
    id=request.form.get("userid")
    return "나 서버 내가 줌"

@app.route('/form_rest_json_text', methods=['POST'])
def form_rest_json_text():
    dic = request.get_json()
    return "나 서버 내가 줌2"

@app.route('/form_rest_json_json', methods=['POST'])
def form_rest_json_json():
    dic = request.get_json()
    print(dic)
    return jsonify( {"msg" : "나 서버야 내가 줄께3"} )

@app.route('/form_rest_uri/<prm1>/<prm2>', methods=['POST'])
def form_rest_uri(prm1, prm2):
    print(prm1, prm2)
    return "나 서버야 내가 줄께"

import pandas as pd
import numpy as np
import folium
from folium import plugins
import re
import googlemaps
import pprint


@app.route("/map")
def map():
    dataset = pd.read_csv("./datasets/제주관광공사_여행장소_20220322.csv", encoding="cp949")
    df = dataset[dataset['장소상세설명']=='숙소']
    geo_list = []
    name_list = []
    for i in range(len(df))[:100]:
        lat = df.iloc[i]['위도']
        lng = df.iloc[i]['경도']
        sname = df.iloc[i]['장소명']
        geo_list.append((lat, lng))
        name_list.append(sname)
    map = folium.Map(location=[33.41041350000001, 126.4913534], zoom_start=10,
                     tiles='OpenStreetMap')
    plugins.MarkerCluster(geo_list, popups=name_list).add_to(map)

    map.get_root().width = "800px"
    map.get_root().height = "600px"
    html_str = map.get_root()._repr_html_()

    return render_template('result_map01.html', KEY_MYDATA=html_str)
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=7878)