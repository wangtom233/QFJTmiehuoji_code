import streamlit as st
from click import style

from calculator_service import (
    calculate_agent_mass_fluoroketone,
    calculate_agent_mass_hfc,
    calculate_required_volume,
)

# 设置页面配置
st.set_page_config(
    page_title="新能源电池消防系统灭火器容量计算器",
    page_icon="🧯",
    layout="wide"
)

# 自定义 CSS 样式
st.markdown("""
<style>
    /* 设置主标题样式 */
    .main-header {
        font-size: 2.2rem; /* 设置字体大小 */
        color: #0066cc;    /* 设置字体颜色 */
        text-align: center; /* 文字居中对齐 */
        margin-bottom: 1rem; /* 设置底部外边距 */
    }
    /* 设置副标题样式 */
    .sub-header {
        font-size: 1.2rem; /* 设置字体大小 */
        color: #333;    /* 设置字体颜色 */
        text-align: center; /* 文字居中对齐 */
        margin-bottom: 2rem; /* 设置底部外边距 */
    }
    /* 设置结果卡片样式 */
    .result-card {
        background-color: #f0f8ff; /* 设置背景颜色 */
        border-left: 5px solid #0066cc; /* 设置左边框样式 */
        padding: 1.5rem; /* 设置内边距 */
        border-radius: 8px; /* 设置圆角 */
        margin-top: 2rem; /* 设置顶部外边距 */
    }
    /* 设置警告框样式 */
    .warning-box {
        background-color: #fff8e6; /* 设置背景颜色 */
        border-left: 5px solid #ff9900; /* 设置左边框样式 */
        padding: 1rem; /* 设置内边距 */
        border-radius: 5px; /* 设置圆角 */
        margin-top: 1rem; /* 设置顶部外边距 */
    }
    /* 设置公式框样式 */
    .formula-box {
        background-color: #f8f9fa; /* 设置背景颜色 */
        border: 1px solid #dee2e6; /* 设置边框样式 */
        border-radius: 5px; /* 设置圆角 */
        padding: 1rem; /* 设置内边距 */
        margin: 1rem 0; /* 设置上下外边距 */
    }
    /* 设置参数表格样式 */
    .parameter-table {
        background-color: #e8f4fd; /* 设置背景颜色 */
        padding: 1rem; /* 设置内边距 */
        border-radius: 5px; /* 设置圆角 */
        margin: 1rem 0; /* 设置上下外边距 */
    }
    /* 调整 selectbox 的宽度 */
    .stSelectbox div[data-testid="stVerticalBlock"] > div {
        width: 300px !important; /* 设置所需宽度 */
    }
    /* 设置 selectbox 的样式，使其更加显眼 */
    .stSelectbox div[data-testid="stVerticalBlock"] > div {
        background-color: #e7f3fe !important; /* 设置背景颜色为浅蓝色 */
        border: 2px solid #007bff !important; /* 设置粗边框 */
        border-radius: 5px !important; /* 设置圆角 */
        padding: 10px !important; /* 设置内边距 */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important; /* 设置阴影效果 */
    }
    /* 调整 selectbox 内部文本样式 */
    .stSelectbox div[data-testid="stVerticalBlock"] > div > div:first-child div input {
        font-size: 16px !important; /* 设置字体大小 */
        color: #333 !important;      /* 设置字体颜色 */
        background: none !important; /* 移除默认的输入框背景 */
        border: none !important;    /* 移除默认的输入框边框 */
        outline: none !important;   /* 移除聚焦时的默认轮廓 */
        width: 100% !important;       /* 占据整个父容器的宽度 */
        height: 100% !important;      /* 占据整个父容器的高度 */
        text-align: left !important;  /* 文本左对齐 */
    }
    /* 设置 selectbox 占位符样式 */
    .stSelectbox div[data-testid="stVerticalBlock"] > div > div:first-child div input::placeholder {
        color: #999 !important; /* 设置占位符颜色 */
        opacity: 1 !important;    /* 确保占位符完全不透明 */
    }
    /* 调整 selectbox 的箭头样式 */
    .stSelectbox div[data-testid="stVerticalBlock"] > div svg {
        fill: #007bff !important; /* 设置箭头颜色 */
        width: 20px !important;   /* 设置箭头宽度 */
        height: 20px !important;  /* 设置箭头高度 */
    }
    /* 调整 selectbox 下拉菜单的样式 */
    .stSelectbox div[data-testid="stVerticalBlock"] + div[data-testid="stDropdown"] div[data-testid="stDropdownList"] {
        background-color: #ffffff !important; /* 设置背景颜色 */
        border: 1px solid #dddddd !important; /* 设置边框 */
        border-radius: 5px !important; /* 设置圆角 */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important; /* 设置阴影效果 */
        max-height: 200px !important; /* 设置最大高度 */
        overflow-y: auto !important; /* 启用垂直滚动条 */
    }
    /* 调整 selectbox 下拉菜单项的样式 */
    .stSelectbox div[data-testid="stVerticalBlock"] + div[data-testid="stDropdown"] div[data-testid="stDropdownList"] li {
        padding: 10px !important; /* 设置内边距 */
        border-bottom: 1px solid #eeeeee !important; /* 设置分隔线 */
        background-color: #ffffff !important; /* 设置背景颜色 */
        cursor: pointer !important; /* 设置鼠标悬停时的光标 */
    }
    /* 调整 selectbox 下拉菜单项悬停时的样式 */
    .stSelectbox div[data-testid="stVerticalBlock"] + div[data-testid="stDropdown"] div[data-testid="stDropdownList"] li:hover {
        background-color: #f0f8ff !important; /* 设置悬停背景颜色 */
    }
    /* 调整 selectbox 下拉菜单项选中时的样式 */
    .stSelectbox div[data-testid="stVerticalBlock"] + div[data-testid="stDropdown"] div[data-testid="stDropdownList"] li[selected="true"] {
        background-color: #e0f7fa !important; /* 设置选中背景颜色 */
    }
</style>
""", unsafe_allow_html=True)

# 主页标题与介绍
st.markdown('<h1 class="main-header">新能源电池消防系统灭火器容量计算器 - 精准计算灭火剂容积需求</h1>',
            unsafe_allow_html=True)
st.markdown(
    '<p class="sub-header">本工具专为新能源电池储能系统设计，帮助您快速准确计算出所需灭火剂容积，确保符合国际国内标准要求。</p>',
    unsafe_allow_html=True)

# 在侧边栏显示公式说明
with st.sidebar:
    st.header("📝 计算公式和参考标准")
    tab_fluoroketone, tab_hfc = st.tabs(["全氟己酮", "七氟丙烷"])

    with tab_fluoroketone:
        st.markdown("""<div class="formula-box">
            全氟己酮质量公式: ( m = K × c × v / (S_1 × (100 - c)) )<br>
            灭火剂容量公式: ( V = m / (p × d) )<br>
            比容公式: ( S_1 = 0.0664 + 0.000274 × T )<br>
            其中:<br>
            <ul>
                <li>( m ): 全氟己酮质量 (kg)</li>
                <li>( c ): 设计浓度 (%)</li>
                <li>( v ): 防护区体积 (m&sup3;)</li>
                <li>( S_1 ): 比容 (m&sup3;/kg)</li>
                <li>( T ): 环境最低温度 (°C)，默认20°C</li>
                <li>( p ): 全氟己酮密度 (4.2 MPa)：1420 kg/m&sup3;</li>
                <li>( d ): 充装率 (默认 0.85)</li>
            </ul>
        </div>""", unsafe_allow_html=True)

        st.header("📝 全氟己酮主要参数表（T/CECS 10171-2022）")
        st.image("listhfc.jpg")

    with tab_hfc:
        st.markdown("""<div class="formula-box">
            七氟丙烷质量公式: ( m = K × c × v / (S_2 × (100 - c)) )<br>
            灭火剂容量公式: ( V = m / (p × d) )<br>
            比容公式: S_2 = 0.1269 + 0.000513 × T )<br>
            其中:<br>
            <ul>
                <li>( m ): 七氟丙烷质量 (kg)</li>
                <li>( c ): 设计浓度 (%)</li>
                <li>( v ): 防护区体积 (m&sup3;)</li>
                <li>( S_2 ): 比容 (m&sup3;/kg)</li>
                <li>( T ): 环境最低温度 (°C)，默认20°C</li>
                <li>( p ): 七氟丙烷密度: 1120 kg/m&sup3; (4.2Mpa)</li>
                <li>( d ): 充装率 (默认 0.85)</li>
                <li>( K ): 海拔修正系数，默认1.0，最小0.565</li>
            </ul>
        </div>""", unsafe_allow_html=True)
        st.image("K_list.png")
        st.header("📝 七氟丙烷主要贮存标准（GB 50370-2005）")
        st.image("qifubw.png")


# 选择灭火剂类型
agent_type = st.selectbox(
    label="请选择灭火剂类型",
    options=["全氟己酮", "七氟丙烷"],
    index=0,
    key="agent_type_selectbox",
    #style={'width': '200px', 'height': '50px'}
)

# 输入参数布局
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if agent_type == "全氟己酮":
        density = st.number_input(
            label="全氟己酮密度 (kg/m³)",
            min_value=1000,
            max_value=2000,
            value=1420,
            step=1,
            format="%d",
            help="请输入全氟己酮的密度，单位为kg/m³。默认值为在4.2MPa贮存压力下，1420 kg/m³。",
            key="density"
        )

    else:
        density = st.number_input(
            label="七氟丙烷密度 (kg/m³)",
            min_value=1000,
            max_value=2000,
            value=1120,
            step=1,
            format="%d",
            help="请输入七氟丙烷的密度，单位为kg/m³。默认值为在4.2MPa贮存压力下1120 kg/m³。",
            key="density"
        )
        altitude_coefficient = st.number_input(
            label="海拔修正系数 (K)",
            min_value=0.565,
            max_value=1.0,
            value=1.0,
            step=0.01,
            format="%.3f",
            help="请输入海拔修正系数，默认值1.0。",
            key="altitude_coefficient"
        )

with col2:
    concentration = st.number_input(
        label="设计浓度 (%)",
        min_value=0.1,
        max_value=20.9,
        value=9.0,
        step=0.1,
        format="%.1f",
        help="请输入设计所需的灭火剂浓度，单位为百分比 (%)。应小于100%。",
        key="concentration"
    )

with col3:
    temp = st.number_input(
        label="环境最低温度 (°C)",
        min_value=-15,
        max_value=30,
        value=20,
        step=1,
        format="%d",
        help="请输入环境的最低温度，单位为摄氏度 (°C)。最大值为30°C。",
        key="temp"
    )

with col4:
    volume = st.number_input(
        label="防护区域体积 (m³)",
        min_value=1.0,
        max_value=100.0,
        value=20.0,
        step=0.1,
        format="%.2f",
        help="请输入防护区域的总体积，单位为立方米 (m³)。",
        key="volume"
    )


with col5:
    filling_ratio = st.number_input(
        label="充装率 (d)",
        min_value=0.1,
        max_value=1.0,
        value=0.85,
        step=0.01,
        format="%.2f",
        help="请输入充装率，必须在0到1之间。默认值为0.85。",
        key="filling_ratio"
    )



# 计算按钮
if st.button("点击计算获取所需灭火剂容量 →"):
    try:
        if agent_type == "全氟己酮":
            # 计算全氟己酮质量
            agent_mass = calculate_agent_mass_fluoroketone(
                volume,
                concentration,
                temp,

            )
        else:
            # 计算七氟丙烷质量
            agent_mass = calculate_agent_mass_hfc(
                volume,
                concentration,
                temp,
                altitude_coefficient=altitude_coefficient
            )

        if density <= 0:
            raise ValueError(f"{agent_type} 密度必须大于0 kg/m³。")

        # 计算所需灭火器体积
        required_volume = calculate_required_volume(
            agent_mass,
            density,
            filling_ratio
        )

        # 结果展示
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("<h3>计算结果:</h3>")
        st.markdown(f"所需灭火剂质量: {agent_mass:.2f} kg")
        st.markdown(f"所需灭火器体积: {required_volume:.2f} L")
        st.markdown(f"参考标准: GB50193, T/CECS 10171-2022")
        st.markdown("</div>", unsafe_allow_html=True)

        # 注意事项提醒
        st.markdown('<div class="warning-box">', unsafe_allow_html=True)
        st.markdown("计算结果仅供参考，实际安装需考虑:")
        st.markdown("- 环境温度补偿系数")
        st.markdown("- 海拔高度修正")
        st.markdown("- 管道损失补偿")
        st.markdown("- 专业消防设计验收要求")
        st.markdown("</div>", unsafe_allow_html=True)

    except ValueError as e:
        st.error(e)


