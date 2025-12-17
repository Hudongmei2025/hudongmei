import streamlit as st

st.set_page_config(page_title="多功能应用集合", page_icon="🚀", layout="wide")

# 你原来的CSS样式
st.markdown("""
<style>
.stButton button {
    background: white; color: black; border: 1px solid #e0e0e0; border-radius: 5px;
    margin: 2px 0; padding: 12px 20px; width: 100%; text-align: left;
    font-size: 16px; transition: 0.2s;
}
.stButton button:hover { background: #f5f5f5; border-color: #999; }
.stButton button:active, .stButton button:focus { 
    background: #424242; color: white; border-color: #424242; 
}
</style>
""", unsafe_allow_html=True)

# 侧边栏
st.sidebar.title("📱 应用导航")
st.sidebar.markdown("---")

apps = ["🏠 首页", "🦐 南宁美食", "🎡 动漫视频", "📚 学生作业", "🖼️ 动漫相册", "🎶 音乐播放"]
app_files = {
    "🦐 南宁美食": "pages/delicacy.py",
    "🎡 动漫视频": "pages/video.py", 
    "📚 学生作业": "pages/homework.py",
    "🖼️ 动漫相册": "pages/image.py",
    "🎶 音乐播放": "pages/song.py"
}

for app in apps:
    if st.sidebar.button(app, use_container_width=True):
        st.session_state.app = app

if 'app' not in st.session_state:
    st.session_state.app = "🏠 首页"

st.sidebar.markdown("---")

# 显示内容
app = st.session_state.app

if app == "🏠 首页":
    st.image("https://www.gxvnu.edu.cn/lib/images/logo.png")
    st.title("🏠 应用首页")
    st.markdown("### 欢迎使用多功能应用集合")
    st.image("https://www.gxvnu.edu.cn/lib/images/home/ba01.jpg")
    st.text("欢迎来到我们的多功能应用乐园！这里汇集了大家最爱的精彩内容：南宁美食天地带你探索地道老友味，动漫影视馆有蜡笔小新陪你欢乐每一天，学习小伙伴帮你轻松管理作业进度，动漫画廊展示精美动漫图集，音乐时光机提供随时随地的美妙陪伴。点击左侧导航栏，开始探索这些精彩功能吧！每个应用都有独特惊喜等着你发现，让生活更便捷，让时光更美好！✨😊")

elif app in app_files:
    try:
        with open(app_files[app], 'r', encoding='utf-8') as f:
            exec(f.read())
    except:
        st.title(app)
        st.error("应用加载失败")
