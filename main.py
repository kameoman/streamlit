from os import write
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit入門')
st.write('DataFrame')
st.write('Interactive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここが右カラムです')

option = st.text_input('あなたの趣味は？')
condition = st.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味は', option,'です。'
'コンディション:', condition

expander = st.expander('お問い合わせ1')
expander.write('お問い合わせ内容を書く')
expander2 = st.expander('お問い合わせ2')
expander2.write('お問い合わせ内容を書く')
expander3 = st.expander('お問い合わせ3')
expander3.write('お問い合わせ内容を書く')

# bt = st.button('成功')
# bt

# rd = st.radio('ラジオボタン',('Comedy', 'Drama', 'Documentary'))
# rd

# option = st.selectbox(
#   'あなたの好きな数字を入力してください',
#   list(range(1, 11))
# )

# 'あなたの好きな数字は', option, 'です。'

# if st.checkbox('Show Image'):
#     img = Image.open('top.png')
#     st.image(img, caption='agris top', use_column_width=True)


















# df = pd.DataFrame(
#   np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#   columns=['lat', 'lon']
#     # '1列目': [1, 2, 3, 4],
#     # '2列目': [10, 20, 30, 40]
# )

# df

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)
# st.map(df)




# st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)
# st.table(df.style.highlight_max(axis=0))

# マジックコマンド
# """
# ## 章

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """

