import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from time import sleep

#페이지 기본 설정
st.set_page_config(
    page_title="종건이의 웹사이트",
    layout="wide"
)
# 로딩바 구현하기
with st.spinner(text="페이지 로딩중..."):
    sleep(2)

#페이지 헤더, 서브헤더 제목 설정
st.header("# 겨울방학 프로젝트")
st.write("## streamlit이란 무엇인가?")
st.write("###### 2019년 하반기에 탄생한, 파이썬 기반 웹 어플리케이션 툴입니다. 데이터사이언스/머신러닝 프로젝트를 웹 어플리케이션에 배포하는 목적으로 아주 편리하고 강력한 기능을 제공하고 있습니다")

