# 顧客データ分析ダッシュボード

このプロジェクトは、顧客データを分析し、インタラクティブなダッシュボードを提供するStreamlitアプリケーションです。

## 機能

- データの概要表示（総顧客数、平均年齢、都道府県数）
- 年齢分布のヒストグラム
- 都道府県別の顧客数
- 性別比率
- 登録日別の顧客数推移
- 顧客データ一覧表示

## セットアップ

1. 必要なパッケージのインストール:
```bash
pip install -r requirements.txt
```

2. アプリケーションの実行:
```bash
streamlit run customer_analysis.py
```

## 使用技術

- Python 3.11
- Streamlit
- Pandas
- Plotly 