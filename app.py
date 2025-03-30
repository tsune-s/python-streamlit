import streamlit as st

# ページの設定
st.set_page_config(
    page_title="はじめてのStreamlit",
    page_icon="👋",
    layout="wide"
)

# タイトル
st.title("はじめてのStreamlitアプリ")

# テキスト入力
user_input = st.text_input("あなたの名前を入力してください", "")

if user_input:
    st.write(f"こんにちは、{user_input}さん！")

# スライダー
age = st.slider("年齢を選択してください", 0, 100, 25)
st.write(f"選択された年齢: {age}歳")

# セレクトボックス
favorite_color = st.selectbox(
    "好きな色を選んでください",
    ["赤", "青", "緑", "黄", "紫"]
)
st.write(f"選択された色: {favorite_color}") 