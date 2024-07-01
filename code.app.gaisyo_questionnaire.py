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

def main():
    global data  # この行を追加
    st.title("外商販売集計アプリ ver.1.5")  # アプリケーション名を変更

    menu = ["アンケートの集計", "集計状況一覧"]
    choice = st.sidebar.selectbox("メニュー", menu)

    if choice == "アンケートの集計":
        st.subheader("アンケートの集計")
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

        if st.button("送信"):
            if company and name and date and product_name and isbn and sales_destination and target and sales_talk and reaction:
                try:
                    new_data = pd.DataFrame({"会社名": [company], "氏名": [name], "日付": [date], "商品名": [product_name], "ISBN or 商品コード": [isbn], "営業先": [sales_destination], "対象": [target], "営業トーク": [sales_talk], "反応": [reaction], "備考": [remarks]})
                    data = pd.concat([data, new_data], ignore_index=True)
                    data.to_csv(data_file, index=False)
                    st.success("アンケートを集計しました。")
                    print("アンケートの集計に成功しました。")
                except Exception as e:
                    st.error(f"エラーが発生しました：{e}")
                    print(f"エラーが発生しました：{e}")
            else:
                st.error("すべての必須フィールドを入力してください。")

    elif choice == "集計状況一覧":
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

if __name__ == "__main__":
    main()

# 実行するときはターミナルに「streamlit run code.app.gaisyo_questionnaire.py」を入力する


