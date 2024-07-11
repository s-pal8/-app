# 2024.07.10時点で不要なモジュール

import streamlit as st  

"""複数のアプリケーションを管理するためのユーティリティ"""

class MultiApp:
    def __init__(self):
        # アプリケーションを格納するためのリストを初期化
        self.apps = []

    def add_app(self, title, func):
        """新しいアプリケーションを追加"""
        # アプリケーションのタイトルと関数をリストに追加
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # ドロップダウンメニューから実行するアプリを選択
        app = st.selectbox(
            'ナビゲーション',
            self.apps,
            format_func=lambda app: app['title'])

        # 選択されたアプリを実行
        app['function']
