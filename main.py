# 基本ライブラリー
from PIL import Image
import io
import numpy as np
import pandas as pd
import cv2

# 他の自作ファイルの読み込み
import prediction
import gray
import mask
import model

# アプリ
import streamlit as st

## イチゴの方
# テキストの表示
st.write("""
    # Date's Web Application
    ## イチゴのヘタをとって食べれる状態にしよう!
""")

# ファイルのアップロード
uploaded_file = st.file_uploader('Choose a strawberry_image file')

if uploaded_file is not None:
    print(uploaded_file)
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    st.image(
        image, caption='upload images',
        use_column_width=True
    )
    strawberry = model.CutOut("./model/strawberry_model.pb", uploaded_file)

    if strawberry is not None:
        image = Image.open(strawberry)
        img_array = np.array(image)
        st.image(
            image, caption='download images',
            use_column_width=True
        )


## パイナップルの方
# テキストの表示
st.write("""
    ## パイナップルの冠芽をとって食べれる状態にしよう!
""")

# ファイルのアップロード
uploaded_file2 = st.file_uploader('Choose a pine_image file')

if uploaded_file2 is not None:
    print(uploaded_file2)
    image = Image.open(uploaded_file2)
    img_array = np.array(image)
    st.image(
        image, caption='upload images',
        use_column_width=True
    )
    pine = model.CutOut("./model/pine_model.pb", uploaded_file2)

    if pine is not None:
        image = Image.open(pine)
        img_array = np.array(image)
        st.image(
            image, caption='download images',
            use_column_width=True
        )