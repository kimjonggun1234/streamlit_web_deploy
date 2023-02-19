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
st.subheader("도큐먼트")

if st.button("app.py 코드 보기"):
    code='''import streamlit as st
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

    '''
    st.code(code, language="python")


if st.button("Chart_Demo.py 코드 보기"):
    code='''# pages/2_Chart_Demo.py
    import streamlit as st
    import pandas as pd
    import pydeck as pdk
    from urllib.error import URLError


    # 페이지 기본 설정
    st.set_page_config(
        page_icon="🐶",
        page_title="빅공잼의 스트림릿 배포하기",
        layout="wide",
    )

    st.markdown("# Mapping Demo")
    st.sidebar.header("Mapping Demo")
    st.write(
        """This demo shows how to use
    [`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
    to display geospatial data."""
    )


    @st.experimental_memo
    def from_data_file(filename):
        url = (
            "http://raw.githubusercontent.com/streamlit/"
            "example-data/master/hello/v1/%s" % filename
        )
        return pd.read_json(url)


    try:
        ALL_LAYERS = {
            "Bike Rentals": pdk.Layer(
                "HexagonLayer",
                data=from_data_file("bike_rental_stats.json"),
                get_position=["lon", "lat"],
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                extruded=True,
            ),
            "Bart Stop Exits": pdk.Layer(
                "ScatterplotLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_color=[200, 30, 0, 160],
                get_radius="[exits]",
                radius_scale=0.05,
            ),
            "Bart Stop Names": pdk.Layer(
                "TextLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_text="name",
                get_color=[0, 0, 0, 200],
                get_size=15,
                get_alignment_baseline="'bottom'",
            ),
            "Outbound Flow": pdk.Layer(
                "ArcLayer",
                data=from_data_file("bart_path_stats.json"),
                get_source_position=["lon", "lat"],
                get_target_position=["lon2", "lat2"],
                get_source_color=[200, 30, 0, 160],
                get_target_color=[200, 30, 0, 160],
                auto_highlight=True,
                width_scale=0.0001,
                get_width="outbound",
                width_min_pixels=3,
                width_max_pixels=30,
            ),
        }
        st.sidebar.markdown("### Map Layers")
        selected_layers = [
            layer
            for layer_name, layer in ALL_LAYERS.items()
            if st.sidebar.checkbox(layer_name, True)
        ]
        if selected_layers:
            st.pydeck_chart(
                pdk.Deck(
                    map_style="mapbox://styles/mapbox/light-v9",
                    initial_view_state={
                        "latitude": 37.76,
                        "longitude": -122.4,
                        "zoom": 11,
                        "pitch": 50,
                    },
                    layers=selected_layers,
                )
            )
        else:
            st.error("Please choose at least one layer above.")
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )'''
    st.code(code, language="python")
if st.button("Graph.py 보기"):
    code='''import streamlit as st
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


    # 페이지 컬럼 분할(예: 부트스트랩 컬럼, 그리드)
    cols = st.columns((1, 1, 2))
    cols[0].metric("10/11", "15 °C", "2")
    cols[0].metric("10/12", "17 °C", "2 °F")
    cols[0].metric("10/13", "15 °C", "2")
    cols[1].metric("10/14", "17 °C", "2 °F")
    cols[1].metric("10/15", "14 °C", "-3 °F")
    cols[1].metric("10/16", "13 °C", "-1 °F")

    #라인 그래프 데이터 생성(with. Pandas)
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    # 컬럼 나머지 부분에 라인차트 생성
    cols[2].line_chart(chart_data)'''
    st.code(code, language="python")