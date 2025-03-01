import streamlit as st 

def closing():
    st.markdown('Find me on:')
    st.markdown(
        '''
        <div style ='display: inline;'>
            <a href='https://www.linkedin.com/in/mhaekalakiyat/'
                style='text-decoration:none; outline:none;'>
                <img src='https://static.vecteezy.com/system/resources/previews/023/986/926/large_2x/linkedin-logo-linkedin-logo-transparent-linkedin-icon-transparent-free-free-png.png', 
                width='30', height='30'>
            </a>
        </div>
        <div style ='display: inline;'>
            <a href='https://github.com/mhaekaal/'
            style='text-decoration:none; outline:none;'>
                <img src='https://pngimg.com/uploads/github/github_PNG40.png', 
                width='30', height='30'>
            </a>
        </div>
        <div style ='display: inline;'>
            <a href='http://wa.me/6281222452017'
            style='text-decoration:none; outline:none;'>
                <img src='https://ugc.production.linktr.ee/bab69f76-7f5e-44f4-ba84-52d30c525a99_-Pngtree-whatsapp-icon-whatsapp-logo-3584844.png?io=true&size=thumbnail-stack-v1_0', 
                width='30', height='30'>
            </a>
        </div>
        ''',
        unsafe_allow_html=True
    )
