import streamlit as st
def display_page_header(title: str, subtitle: str = “”, icon_name: str = “”):
    st.markdown(f”## {title}“)
    if subtitle:
        st.markdown(f”**{subtitle}**“)
    if icon_name:
        st.markdown(f”![icon](https://img.icons8.com/ios-filled/50/000000/{icon_name})“)
def load_custom_css():
    st.markdown(“”"
        <style>
            body {
                background-color: #F9F9F9;
            }
            .stButton>button {
                background-color: #4CAF50;
                color: white;
            }
        </style>
    “”", unsafe_allow_html=True)
def display_interactive_background():
    pass  # You can add a Lottie animation or custom background later