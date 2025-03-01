import streamlit as st
import pandas as pd

def aboutme():
    st.markdown('''<h1 style='text-align:left;font-size:30px;font-weight:bolder;'>
            Hello!
         </h1>''', unsafe_allow_html=True)
    st.markdown('''
            <h1 style='text-align:left;font-size:15px;font-weight:normal;text-indent:30px; line-height:2;'>
            My name is Muhammad Haekal Akiyat, Electrical engineering graduate with three years 
            experience in maintenance facility at harbour sectors, 
            now fully focused on gaining the abilities needed to succeed as a data scientist.
            Enthusiastic about pursuing a career as a data scientist, 
            with a strong desire to acquire new skills and adapt to the rapidly changing industry. 
            Having a solid foundation in data analytics, machine learning, and statistical modeling skills
            through a Dibimbing.ID Data Science Bootcamp. 
            Well suited to assist in data-driven decision making and solving business problems 
            due to a continuous desire to learn and grow.
            </h1>
            ''',
            unsafe_allow_html=True)
    st.markdown('         ')
    
    edu = {'Name':['University of Brawijaya','dibimbing.id'],
           'Major': ['Electrical Engineer', 'Data Science'],
           'Year':['2016-2020', '2024-2025']}
    education = pd.DataFrame(edu)
    st.markdown(
        '''
            <h1 style='text-align: left; font-size:20px;'>
               Education
            </h1>
        ''',
        unsafe_allow_html=True
    )
    st.table(education.reset_index(drop=True))
    st.markdown('         ')
    st.markdown(
        '''
            <h1 style='text-align: left; font-size:20px;'>
               Skills
            </h1>
        ''',
        unsafe_allow_html=True
    )
    # Baris pertama (3 kolom)
    col1_atas, col2_atas, col3_atas = st.columns(3)
    
    with col1_atas:
        st.selectbox('**Programming**', ['Details', 'Python', 'Google Colab', 'Microsoft Excels'])
        # Tambahkan konten Anda di sini
    
    with col2_atas:
        st.selectbox('**Data Visualization**', ['Details', 'Power BI', 'Tableau', 'Matplotlib', 'Seaborn', 'Looker Studio', 'Pivot Table'])
        # Tambahkan konten Anda di sini
    
    with col3_atas:
        st.selectbox('**Database Management**', ['Details', 'PostgreSQL', 'SQL', 'DBeaver', 'SQLite'])
        # Tambahkan konten Anda di sini
    
    # Baris kedua (3 kolom)
    col1_bawah, col2_bawah, col3_bawah = st.columns(3)
    
    with col1_bawah:
        st.selectbox('**Machine Learning**', ['Details', 'Classification', 'Regression', 'Clustering', 'Forecasting', 'Recommendation System'])
        # Tambahkan konten Anda di sini
    
    with col2_bawah:
        st.selectbox('**Data Wrangling**', ['Details', 'Statistics', 'A/B Testing', 'Hypothesis testing', 'Data Cleaning', 'Feature Engineering', 'Exploratory Data Analysis'])
        # Tambahkan konten Anda di sini
    
    with col3_bawah:
        st.selectbox('**Soft Skills**', ['Details', 'Analytical Skills', 'Storytelling', 'Problem Solving', 'Teamwork', 'Business Interpretability'])
    # Tambahkan konten Anda di sini
    '''
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox('**Hard Skills**', ['Details', 'Statistics', 'Python', 'Web Scraping', 'Data Visualization','Data Wrangling', 'Machine Learning', 'SQL', ])
    with col2:
        st.selectbox('**Tools**', ['Details', 'Jupiter Notebook', 'VScode', 'Tableau', 'Looker', 'Power BI', 'Streamlit', 'PostgreSQL', 'Dbeaver'])
    '''
    st.markdown('         ')
    st.markdown(
        '''
            <h1 style='text-align: left; font-size:20px;'>
               Certificate & Coursework
            </h1>
        ''',
        unsafe_allow_html=True
    )
    
    st.selectbox('** **',['Details','Data Science Bootcamp', 'Data Analysis Bootcamp', 'Python for Data Science and Machine Learning Bootcamp', 'The Complete SQL Bootcamp from Zero to Hero', 'Lean Six Sigma White Belt and Yellow Belt'])

    st.markdown('         ')
    st.markdown(
        '''
            <h1 style='text-align: left; font-size:20px;'>
               Honor & Awards
            </h1>
        ''',
        unsafe_allow_html=True
    )
    
    st.selectbox('** **',['Details','1st Runner Up Performer Data Science Bootcamp', 'Award Charter Power Electronics Laboratory Assistant']) 


