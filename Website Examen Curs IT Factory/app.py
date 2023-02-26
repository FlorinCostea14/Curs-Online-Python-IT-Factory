from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title='My Online Portofolio', page_icon=':tada:', layout='wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style', unsafe_allow_html=True)

local_css('style/style.css')

lottie_coding = load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_w6dptksf.json')
lottie_coding2 = load_lottieurl('https://assets8.lottiefiles.com/packages/lf20_se3w0ukg.json')
img_githubcat = Image.open('images/githubcat.png')

with st.container():
    st.subheader('Hi, I am Florin Costea :wave:')
    st.title('A Junior Python Developer from Romania')
    st.subheader('I am passionate about coding :computer:, the automotive industry :car: and car parts :gear:')
    st.write('[More info on my LinkedIn page >](https://www.linkedin.com/in/florin-costea-74361b248/)')
    st.write('[Link to my CV >](https://drive.google.com/file/d/1NjUb_Y4oVQWaP1elhZGuyzIm-GHxqZA3/view?usp=share_link)')

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('Short story about me')
        st.write('##')
        st.write(
        '''
        - graduated the Babeș-Bolyai University from Cluj-Napoca Romania back in 2015, in Economics and International Business
        - then got a master's degree in 2017 at the same university, same domain
        - started working full-time as a sales agent at an auto parts warehouse, where I am still to this day
        - learned a lot about the automotive world, parts in particular, problems that occur to certain car models, what fails
        - learned how to work with people, how to work in a team, how a business is managed
        - I see myself as a motivated person in reaching my goals, loyal and organised
        - started learning a programming language called Python through an online course
        Skills are gained by hard working and commiting to something, this is what keeps me going.
        ''')
    with right_column:
        st_lottie(lottie_coding, height=300, key='coding')

with st.container():
    st.write('---')
    st.header('My Projects')
    st.write('##')
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_githubcat)
    with text_column:
        st.subheader('Github repository link')
        st.write('Here is a link to my Github repository where you can see all my projects from the IT Factory online course')
        st.markdown('[Github link...](https://github.com/FlorinCostea14/Curs-Python-IT-Factory)')

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('Get in touch with me!')
        st.write('##')
        contact_form = '''
        <form action="https://formsubmit.co/costeaflorin14@gmail.com" method="POST">
            <input type='hidden' name='_captcha' value='false'>
            <input type="text" name="name" placeholder='Your name' required>
            <input type="email" name="email" placeholder='Your email' required>
            <textarea name='message' placeholder='Your message here' required></textarea>
            <button type="submit">Send</button>
        </form>
        '''
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()

    with right_column:
        st_lottie(lottie_coding2, height=300, key='coding2')
