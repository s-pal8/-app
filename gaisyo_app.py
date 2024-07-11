import streamlit as st
import gaisyo_registration, gaisyo_list  # ここでアプリモジュールを直接インポート

class _SessionState:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

def get_session_state(**kwargs):
    session_id = get_report_ctx().session_id
    session = Server.get_current()._get_session_info(session_id).session
    if not hasattr(session, '_session_state'):
        session._session_state = _SessionState(**kwargs)
    return session._session_state

# メインアプリ
def main():
    st.title('外商販促集計アプリver.1.0')
    st.subheader("メニュー")
    if st.button("集計情報登録"):
        gaisyo_registration.app()
    elif st.button("集計情報一覧"):
        gaisyo_list.app()
    elif st.button("商品一覧"):
        st.write("準備中")
    elif st.button("施策案内"):
        st.write("準備中")
    elif st.button("会員登録"):
        st.write("準備中")

if __name__ == "__main__":
    main()

# 実行するときはターミナルに「streamlit run gaisyo_app.py」を入力する
