import streamlit as st

# 设置页面标题
st.title("我的第一个 Streamlit 应用")

# 显示文本
st.write("这是一个简单的交互式应用，用纯 Python 编写！")

# 显示数据表格
import pandas as pd
data = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "年龄": [25, 30, 28],
    "城市": ["北京", "上海", "广州"]
})
st.dataframe(data)  # 交互式表格

# 绘制图表
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(data["姓名"], data["年龄"])
st.pyplot(fig)  # 显示 matplotlib 图表