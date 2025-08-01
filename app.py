import streamlit as st

# 상태 저장용 초기 설정
if 'page' not in st.session_state:
    st.session_state.page = 'input'

# 제목
st.title("🌾 농약 GPT")

# 1️⃣ 이름과 주민번호 입력 화면
if st.session_state.page == 'input':
    st.markdown("### 1️⃣ 이름")
    name = st.text_input("이름을 입력하세요", key="name_input", label_visibility="collapsed")
    
    st.markdown("### 2️⃣ 주민번호")
    jumin = st.text_input("주민번호를 입력하세요", type="password", key="jumin_input", label_visibility="collapsed")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ 확인"):
            if name and jumin:
                st.session_state.page = 'consent'
            else:
                st.warning("이름과 주민번호를 모두 입력해주세요.")
    with col2:
        if st.button("🤖 임시상담"):
            st.session_state.page = 'chat'
    
    st.caption("임시상담은 맞춤형 상담이 어려운 점 양해 바랍니다.")

# 2️⃣ 개인정보 동의서 화면
elif st.session_state.page == 'consent':
    st.markdown("### 3️⃣ 개인정보 활용 동의서")
    st.image("개인정보동의서.png", use_container_width=True)

    agree = st.checkbox("위 내용에 동의합니다.")

    if st.button("✅ 확인"):
        if agree:
            st.session_state.page = 'chat'
        else:
            st.warning("동의란에 체크해야 상담이 가능합니다.")

# 3️⃣ 상담 화면 (채팅 이미지 + 외부 GPT 링크 버튼)
elif st.session_state.page == 'chat':
    st.image("채팅화면.png", use_container_width=True)
    st.markdown("### <span style='color:red; font-size:36px;'>말씀해주세요. 듣고 있습니다</span>", unsafe_allow_html=True)
    st.markdown("### 👉 [🔗 여기 클릭하여 상담 계속하기](https://chatgpt.com/g/g-688c7dbe0a0081919635c927bf1597d6-nongyag-gpt/)", unsafe_allow_html=True)
    st.info("※ 맞춤형 상담이 어려운 점 양해 바랍니다.")
