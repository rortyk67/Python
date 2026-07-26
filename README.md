# Python

Python の学習用リポジトリです。文法や標準ライブラリの練習コードを、テーマごとにフォルダを分けて置いています。

作品リポジトリではなく、あくまで練習・実験用です。

## ディレクトリ構成

```
Python/
├── README.md
├── .gitignore
└── basics/         # 基本文法の練習
    └── basic.py
```

学習テーマが増えたら、`basics/` と同じようにフォルダを追加していきます。

## 環境

- Ubuntu 24.04
- pyenv でバージョン管理（`basics/` は Python 3.14.3）
- フォルダごとに `.venv`（仮想環境）を作成

`.venv/` と `.python-version` は `.gitignore` で除外しているため、リポジトリには含まれていません。

## 動かし方

各フォルダで仮想環境を用意してから実行します。

```bash
cd basics
pyenv local 3.14.3        # Python のバージョンを固定
python -m venv .venv      # 仮想環境を作成
source .venv/bin/activate # 仮想環境を有効化
python basic.py
```
