import streamlit as st
import pandas as pd
import os
import hashlib

# ユーザー情報を保存するためのCSVファイルのパス
users_file = "users.csv"

# ファイルが存在する場合は読み込み、存在しない場合は新たに作成
if os.path.isfile(users_file):
    users = pd.read_csv(users_file, index_col='username').to_dict('index')
else:
    users = {}

# パスワードをハッシュ化する関数
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    menu = ["ログイン", "登録"]
    choice = st.sidebar.selectbox("メニュー", menu)

    if choice == "ログイン":
        st.subheader("ログイン")

        username = st.text_input("ユーザー名")
        password = st.text_input("パスワード", type='password')

        if st.button("ログイン"):
            if username in users and users[username]['password'] == hash_password(password):
                st.success("ログインしました：{}".format(username))
            else:
                st.error("ユーザー名またはパスワードが間違っています")

    elif choice == "登録":
        st.subheader("登録")

        new_username = st.text_input("ユーザー名")
        new_password = st.text_input("パスワード", type='password')

        if st.button("登録"):
            if new_username in users:
                st.error("このユーザー名は既に存在します")
            else:
                users[new_username] = {'password': hash_password(new_password)}
                pd.DataFrame(users).T.to_csv(users_file)
                st.success("登録が完了しました")

if __name__ == "__main__":
    main()
