import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit入門')
st.write('DataFrame')
st.write('Display Image')

img = Image.open('top.png')

st.image(img, caption='agris top', use_column_width=True)


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

