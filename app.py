import streamlit as st
from calculator_service import calculate_agent_mass, calculate_required_volume

# 设置页面配置
st.set_page_config(
    page_title="新能源电池消防系统灭火器容量计算器",
    page_icon="🧯",
    layout="wide"
)

# 自定义CSS样式
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        color: #0066cc;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #333;
        text-align: center;
        margin-bottom: 2rem;
    }
    .result-card {
        background-color: #f0f8ff;
        border-left: 5px solid #0066cc;
        padding: 1.5rem;
        border-radius: 8px;
        margin-top: 2rem;
    }
    .warning-box {
        background-color: #fff8e6;
        border-left: 5px solid #ff9900;
        padding: 1rem;
        border-radius: 5px;
        margin-top: 1rem;
    }
    .formula-box {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .parameter-table {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# 主页标题与介绍
st.markdown('<h1 class="main-header">新能源电池消防系统灭火器容量计算器 - 精准计算灭火剂容积需求</h1>',
            unsafe_allow_html=True)
st.markdown(
    '<p class="sub-header">本工具专为新能源电池储能系统设计，帮助您快速准确计算出所需灭火剂容积，确保符合NFPA、GB等国际国内标准要求。</p>',
    unsafe_allow_html=True)

# 在侧边栏显示公式说明
with st.sidebar:
    st.header("📝 计算公式")
    st.markdown("""
    <div class="formula-box">
        全氟己酮质量公式: m = c × v / (S × (100 - c) \n
        灭火剂容量公式: V = m / (p × d) \n
        比容公式: ( S = 0.0664 + 0.000274 × T \)
        其中:
        
            ( m ): 全氟己酮质量 (kg) \n
            ( c ): 设计浓度 (%) \n
            ( v ): 防护区体积 (m³) \n
            ( S ): 比容 (m³/kg ) \n
            ( T ): 环境最低温度 ( °C )：默认20 °C \n
            ( p ): 全氟己酮密度(4.2 MPa) ： 1420  kg/m³ \n
            ( d ): 充装率 (默认 0.85)
        
        
    </div>
    """, unsafe_allow_html=True)
    st.header("📝 全氟己酮主要参数表（T/CECS 10171-2022）")
    st.sidebar.image("list.jpg")

# 输入参数表格
st.header("💡 输入参数")

# 使用表格布局输入参数
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    volume = st.number_input(
        label="防护区域体积 (m³)",
        min_value=1.0,
        max_value=10000.0,
        value=20.0,
        step=0.1,
        format="%1.1f",
        help="请输入防护区域的总体积，单位为立方米 (m³)。"
    )

with col2:
    concentration = st.number_input(
        label="设计浓度 (%)",
        min_value=0.1,
        max_value=20.9,
        value=9.0,
        step=0.1,
        format="%1.3f",
        help="请输入设计所需的灭火剂浓度，单位为百分比 (%)。必须小于100%。"
    )

with col3:
    temp = st.number_input(
        label="环境最低温度 (°C)",
        min_value=-30.0,
        max_value=30.0,
        value=20.0,
        step=0.1,
        format="%1.1f",
        help="请输入环境的最低温度，单位为摄氏度 (°C)。最大值为30°C。"
    )

with col4:
    density = st.number_input(
        label="全氟己酮密度 (kg/m³)",
        min_value=1000.0,
        max_value=2000.0,
        value=1420.0,
        step=1.0,
        format="%1.0f",
        help="请输入全氟己酮的密度，单位为kg/m³。默认值为在4.2MPa贮存压力下，1420 kg/m³。"
    )

with col5:
    filling_ratio = st.number_input(
        label="充装率 (d)",
        min_value=0.1,
        max_value=1.0,
        value=0.85,
        step=0.01,
        format="%1.2f",
        help="请输入充装率，必须在0到1之间。默认值为0.85。"
    )

# 计算按钮
if st.button('点击计算获取所需灭火剂容量 →'):
    try:
        # 计算全氟己酮质量
        agent_mass = calculate_agent_mass(volume, concentration, temp)

        # 计算所需灭火器体积
        required_volume = calculate_required_volume(agent_mass, density, filling_ratio)

        # 结果展示
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(f"计算结果:")
        st.markdown(f"所需灭火剂质量: {agent_mass:.3f} kg")
        st.markdown(f"所需灭火器体积: {required_volume:.3f} 升(L)")
        st.markdown(f"符合标准: GB50193, NFPA2001")
        st.markdown('</div>', unsafe_allow_html=True)

        # 注意事项提醒
        st.markdown('<div class="warning-box">', unsafe_allow_html=True)
        st.markdown("计算结果仅供参考，实际安装需考虑:")

        st.markdown("环境温度补偿系数")
        st.markdown("海拔高度修正")
        st.markdown("管道损失补偿")
        st.markdown("专业消防设计验收要求")

        st.markdown('</div>', unsafe_allow_html=True)

    except ValueError as e:
        st.error(e)


