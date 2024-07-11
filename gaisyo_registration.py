import streamlit as st
import pandas as pd
import os

# データを保存するためのCSVファイルのパス
data_file = "data.csv"

def app():  # この関数名を`main`から`app`に変更
    st.title("外商販促集計アプリ ver.1.8")
    st.subheader("集計情報登録")

    # フォームの作成
    with st.form(key='registration_form'):
        company = st.text_input("会社名")
        name = st.text_input("氏名")
        date = st.date_input("日付")
        product_name = st.text_input("商品名")
        isbn = st.text_input("ISBN or 商品コード")
        sales_destination = st.text_input("営業先")
        target = st.text_input("対象")
        sales_talk = st.text_input("営業トーク")
        reaction = st.text_input("反応")
        remarks = st.text_input("備考")

        # フォーム内に送信ボタンを配置
        submitted = st.form_submit_button("送信")

    if submitted:
        # ファイルが存在する場合は読み込み、存在しない場合は新たに作成
        if os.path.isfile(data_file):
            data = pd.read_csv(data_file)
            print(data)  # ここでデータを出力
        else:
            data = pd.DataFrame(columns=["会社名", "氏名", "日付", "商品名", "ISBN or 商品コード", "営業先", "対象", "営業トーク", "反応", "備考"])

        if company and name and date and product_name and isbn and sales_destination and target and sales_talk and reaction:
            try:
                new_data = pd.DataFrame({"会社名": [company], "氏名": [name], "日付": [date], "商品名": [product_name], "ISBN or 商品コード": [isbn], "営業先": [sales_destination], "対象": [target], "営業トーク": [sales_talk], "反応": [reaction], "備考": [remarks]})
                print(new_data)  # ここで新しいデータを出力
                data = pd.concat([data, new_data], ignore_index=True)
                data.to_csv(data_file, index=False)
                st.success("アンケートを集計しました。登録が完了しました。")
                print("集計情報登録に成功しました。")
            except Exception as e:
                st.error(f"エラーが発生しました：{e}")
                print(f"エラーが発生しました：{e}")
        else:
            st.error("すべての必須フィールドを入力してください。")

    if st.button('戻る'):
        st.experimental_rerun()
