import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# ページ設定
st.set_page_config(
    page_title="顧客データ分析",
    page_icon="📊",
    layout="wide"
)

# タイトル
st.title("顧客データ分析ダッシュボード")

# データの読み込み
@st.cache_data
def load_data():
    df = pd.read_csv('customer_master.csv')
    df['registration_date'] = pd.to_datetime(df['registration_date'])
    return df

df = load_data()

# データの概要
st.header("1. データの概要")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("総顧客数", f"{len(df):,}人")
with col2:
    st.metric("平均年齢", f"{df['age'].mean():.1f}歳")
with col3:
    st.metric("都道府県数", f"{df['pref'].nunique()}都道府県")

# 年齢分布
st.header("2. 年齢分布")
fig_age = px.histogram(df, x='age', nbins=30,
                      title='顧客の年齢分布',
                      labels={'age': '年齢', 'count': '顧客数'})
st.plotly_chart(fig_age, use_container_width=True)

# 都道府県別の顧客数
st.header("3. 都道府県別の顧客数")
pref_counts = df['pref'].value_counts()
fig_pref = px.bar(pref_counts, 
                  title='都道府県別の顧客数',
                  labels={'value': '顧客数', 'index': '都道府県'})
st.plotly_chart(fig_pref, use_container_width=True)

# 性別比率
st.header("4. 性別比率")
gender_counts = df['gender'].value_counts()
fig_gender = px.pie(values=gender_counts.values, 
                    names=gender_counts.index,
                    title='性別比率')
st.plotly_chart(fig_gender, use_container_width=True)

# 登録日別の顧客数推移
st.header("5. 登録日別の顧客数推移")
daily_counts = df.groupby(df['registration_date'].dt.date).size().reset_index()
daily_counts.columns = ['date', 'count']
fig_daily = px.line(daily_counts, x='date', y='count',
                    title='登録日別の顧客数推移',
                    labels={'date': '登録日', 'count': '顧客数'})
st.plotly_chart(fig_daily, use_container_width=True)

# データテーブル
st.header("6. 顧客データ一覧")
st.dataframe(df, use_container_width=True) 