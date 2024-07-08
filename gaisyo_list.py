import streamlit as st
import pandas as pd
import os

# データを保存するためのCSVファイルのパス
data_file = "data.csv"

# ファイルが存在する場合は読み込み、存在しない場合は新たに作成
if os.path.isfile(data_file):
    data = pd.read_csv(data_file)
else:
    data = pd.DataFrame(columns=["会社名", "氏名", "日付", "商品名", "ISBN or 商品コード", "営業先", "対象", "営業トーク", "反応", "備考"])

def app():  # この関数名を`main`から`app`に変更
    global data
    st.title("外商販売集計アプリ ver.1.5")
    st.subheader("集計状況一覧")
    isbn_to_search = st.text_input("ISBN or 商品コードで絞り込む")
    product_name_to_search = st.text_input("商品名で絞り込む")
    sort_by_date = st.checkbox("日付順に並び替える")

    filtered_data = data
    if isbn_to_search:
        filtered_data = filtered_data[filtered_data["ISBN or 商品コード"] == isbn_to_search]
    if product_name_to_search:
        filtered_data = filtered_data[filtered_data["商品名"] == product_name_to_search]
    if sort_by_date:
        filtered_data = filtered_data.sort_values("日付")

    st.write(filtered_data)

    if st.button('戻る'):
        st.experimental_rerun()
