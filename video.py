import streamlit as st

st.set_page_config(page_title="动漫世界", page_icon='🎡')
st.markdown("## 蜡笔小新第十季")

video_arr=[{
        'url':'https://apd-e5ffce9b9f3cd1ccccc3128f3c9f7002.v.smtcdns.com/vhot2.qqvideo.tc.qq.com/AM0eTcNxNhJR1WOsI31SmKZkJ6EFSwLnjsg3KnfV6tm4/B_3k--xdVBUHYl1q0K2jODe3Czy6jN--S5qKjbKKcWhqc36DnShajnw1opCrr4ZImT980xUUCvORBKLdHtA8ctS0jkVWFGysIyz7HPgphyihA0cqxafmT-MvEkl4o_7uNVKIvFvNEedTY97p2xGmq39Q/svp_50069/gzc_1000035_0b53faaa6aaapyam2e345nujkkgdb4uaad2a.f622.mp4?vkey=320DF7C3B3DDBB8313588485AED7CBE683C7D86A1EEDACB9E0745D89B1E59C7B1A1CE184F6B034F1511189BB98A876B591D64EDB41310F98DBF49A2553A3CFAF441CB4DA13D84C715E2AC9837D9F87F90DB42C44A25B247948227F9E9D64E64352135381ABB8716DF72B1FEE032FE8880DCC962C7319B8723F1C5AF5D5DF9BA7',
        'title':'第一集',
        'text':'分身乏术'
        
    },{
        'url':'https://www.w3schools.com/html/movie.mp4',
        'title':'第二集',
        'text':'美容院'
        
        },{
        'url':'https://apd-d64588010e147bdfa919c62c434ebd56.v.smtcdns.com/vhot2.qqvideo.tc.qq.com/ACPhms7uGSaZpfGvFqJOOCmyCtXGCnn2T3CT7gHe-MCI/B_3k--xdVBUHYl1q0K2jODe5f6JVJ8MdJx_nihwnX5O2Fy3a15JBYi1bR6t3S_EI8QOnAXkZ87L4ZY1KPkQEoZKhgdXQkylk0dM87G_iQBDzo0cqxafmT-MvEkl4o_7uNVKIvFvNEedTY97p2xGmq39Q/svp_1047/gzc_8345_1047_0b535qaxgaabsmaor26x7vtbn3aeopwac42a.f204110.mp4?vkey=C57B89FD0A389E60B9D208AD94939E94EEF1E6D99F746ACD6DED9C1F110DE52C69273529EA0848938E92C43DB25D0922DF1446AEB014687E4024BFB5F43A2EAF722CDA2662C6D8F020AD90ED443998E411E1F27D010C0DE61EF1790A1F633A34723379417C60A3DDBC65A310A222105003FD7C865CB3320F9EAA5EF2133E5DCC',
        'title':'第三集',
        'text':'对讲机'
        
        },{
        'url':'https://apd-e5ffce9b9f3cd1ccccc3128f3c9f7002.v.smtcdns.com/vhot2.qqvideo.tc.qq.com/AM0eTcNxNhJR1WOsI31SmKZkJ6EFSwLnjsg3KnfV6tm4/B_3k--xdVBUHYl1q0K2jODe3Czy6jN--S5qKjbKKcWhqc36DnShajnw1opCrr4ZImT980xUUCvORBKLdHtA8ctS0jkVWFGysIyz7HPgphyihA0cqxafmT-MvEkl4o_7uNVKIvFvNEedTY97p2xGmq39Q/svp_50069/gzc_1000035_0b53faaa6aaapyam2e345nujkkgdb4uaad2a.f622.mp4?vkey=320DF7C3B3DDBB8313588485AED7CBE683C7D86A1EEDACB9E0745D89B1E59C7B1A1CE184F6B034F1511189BB98A876B591D64EDB41310F98DBF49A2553A3CFAF441CB4DA13D84C715E2AC9837D9F87F90DB42C44A25B247948227F9E9D64E64352135381ABB8716DF72B1FEE032FE8880DCC962C7319B8723F1C5AF5D5DF9BA7',
        'title':'第四集',
        'text':'电视频道'
        
        },{
        'url':'https://media.w3.org/2010/05/sintel/trailer.mp4',
        'title':'第五集',
        'text':'留胡子'
        
        }]

if 'ind' not in st.session_state:
    st.session_state['ind']=0

# 显示当前集数标题和内容简介
current_video = video_arr[st.session_state['ind']]
st.markdown(f"### {current_video['title']}")
st.markdown(f"**内容简介：** {current_video['text']}")

st.video(current_video['url'])

def play(i):
    st.session_state['ind']=int(i)

# 横排按钮
cols = st.columns(len(video_arr))  # 添加这一行创建横排
for i in range(len(video_arr)):
    with cols[i]:  # 添加这一行将按钮放入列中
        st.button('第'+str(i+1)+'集',use_container_width=True,on_click=play,args=([i]))

# 添加主要角色介绍
st.markdown("### 主要角色")

# 角色信息
characters = [
    {'name': '蜡笔小新', 'img_url': 'https://picx.zhimg.com/v2-64e1f6f922e41e90a6e5e5f41376ae8a_720w.jpg?source=172ae18b'},
    {'name': '美伢', 'img_url': 'https://img1.fjdaily.com/app/images/2025-04/15/t0_(0X229X300X429)ed45ee05-4107-454f-890e-25e818172fc5.JPEG'},
    {'name': '野原广志', 'img_url': 'https://i.bobopic.com/small/80835859.jpg'},
    {'name': '小葵', 'img_url': 'https://pic4.zhimg.com/v2-cacb627341245b8ccf0d807a226294a5_1440w.jpg'},
    {'name': '小白', 'img_url': 'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1659988190,3144626163&fm=253&gp=0.jpg'}
]

# 创建横排显示角色
char_cols = st.columns(len(characters))

for i, char in enumerate(characters):
    with char_cols[i]:
        # 圆形图片样式
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="{char['img_url']}" width="80" height="80" style="border-radius: 50%; object-fit: cover;">
                <p style="margin-top: 5px;"><strong>{char['name']}</strong></p>
            </div>
            """,
            unsafe_allow_html=True
        )
