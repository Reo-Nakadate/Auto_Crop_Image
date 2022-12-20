# Auto_Crop_Image

オリジナルのデータセットとラベルをもとにTensorFlowで学習したモデルを利用し

DeepLab v3+を用いたセマンティックセグメンテーションを行うことで

イチゴやパイナップルの実だけを抽出するアプリケーション

# DEMO

<img width="1440" alt="top_page" src="https://user-images.githubusercontent.com/74957723/208628692-5cc67baa-4985-47d7-a2ef-678f2e1291b5.png">
<img width="1440" alt="demo" src="https://user-images.githubusercontent.com/74957723/208628716-08803846-691c-4ebb-a299-d0e186718b82.png">

# Requirement

python 3.9

# Installation

$ pipenv install

# Usage

$ streamlit run main.py

# Future

オリジナルのモデルを作成し、自動で切り抜ける画像の種類を増やすことができる

例えば景色の画像から人や車、動物を切り抜くことも可能になる

# Author

* 作成者:Reo Nakadate
* 所属:Musashino University
* E-mail:s2022061@stu.musashino-u.ac.jp
