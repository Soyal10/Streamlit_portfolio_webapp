import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from pathlib import Path

st.set_page_config(layout='wide')

CURR_DIR= Path(__file__).parent if "__file" in locals() else Path.cwd()
profile_pic_path= CURR_DIR/"videos"/"profile_pic.png"
car_pic_path= CURR_DIR/"videos"/"demo.png"
iris_pic_path= CURR_DIR/"videos"/"iris.png"
password_pic_path= CURR_DIR/"videos"/"Interface.PNG"
game_pic_path= CURR_DIR/"videos"/"my project.jpg"
@st.cache_resource
def load_education(url):
    r = requests.get(url)
    if r.status_code!= 200:
        return None
    return r.json()

@st.cache_resource
def load_achievement(url):
    r= requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()


@st.cache_resource
def load_car_price_pic(path):
    img= Image.open(path)
    st.image(img)

@st.cache_resource
def load_passwordManager_pic(path):
    pic= Image.open(path)
    st.image(pic)


@st.cache_resource
def load_profile_pic(path):
    profile_pic= Image.open(path)
    st.image(profile_pic)

@st.cache_resource
def load_game_pic(path):
    pic= Image.open(path)
    st.image(pic)

@st.cache_resource
def load_iris_pic(path):
    pic= Image.open(path)
    st.image(pic)

lottie_ach= load_achievement("https://lottie.host/7981d5e4-e174-443a-b2df-36fe7c90451d/OV6Ws5ojDv.json")
lottie_edu= load_education("https://lottie.host/b2797368-43b3-4e00-83d1-57f7e63712f5/pyrFzgd7sw.json")

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/soyal10/",
    "GitHub": "https://github.com/Soyal10",
}
contact_form="""
<form action="https://formsubmit.co/sohailsayyad10032002@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder= "Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea placeholder="Your Message" required ></textarea>
     <button type="submit">Send</button>
</form>"""

contact_form_style="""
<style>
 input[type="text"],
 input[type="email"],
textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 3px;
} 

button[type="submit"] {
  background-color: #007bff;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}
button[type="submit"]:hover {
  background-color: #0056b3;
}
</style>"""

right_col7,left_col7=st.columns((2,1))
with right_col7:
    st.subheader("Hey Guys :wave:")
    st.title('Welcome to my portfolio website')

st.write("---")

with st.container():
    selected = option_menu (
        menu_title= None,
        options=['About','Projects','Contact Me'],
        icons=['person','code-slash','chat-left-text-fill'],
        orientation='horizontal'
    )
if selected == 'About':
    with st.container():
        col3,col4 = st.columns(2)
        with col3:
            st.write('##')
            st.header('I am Soyal Sayyad')
            st.subheader("""Aspiring professional entering the exciting world of machine learning.""")
            st.write('##')

            st.write("""Passionate about data analysis and pattern recognition, I am dedicated to expanding 
                    my knowledge in machine learning algorithms and techniques. With a strong foundation in B.Tech CSE, 
                    I am committed to applying my skills to solve complex problems and deliver innovative solutions. 
                    Seeking opportunities to collaborate with industry experts and make a positive impact in the field of machine learning. 
                    Open to learning and growth as I embark on this new journey. Let's connect and explore the possibilities!""")


        with col4:
            load_profile_pic(profile_pic_path)

    st.write('---')

    st.subheader('Education ')
    st.write("##")
    with st.container():
        col5,col6= st.columns(2)
        with col5:
            st_lottie(lottie_edu)

        with col6:
            st.write('##')

            st.write('##')
            st.write("B.Tech 2020 - 2024")
            st.markdown("""- Pursing B.Tech (Computer Science and Eng.) from JIT, Nagpur \n - Cleared all semester with the average of 8 sgpa""")
            st.write("##")
            st.write("12th Maharashtra State Board 2018 - 2020")
            st.markdown("""- Scored 100 marks in Mathematics \n - Passed HSC examination with 77.08%""")
           # st.markdown("- Became the State mathematics topper")
            st.write("##")
            st.write("10th Maharashtra State Board 2016 - 2018")
            st.markdown("""- Passed SSC examination with 86.04% \n - Scored 100 marks in mathematics""")
    st.write("---")
    st.write("##")
    st.subheader("Achievements ")
    st.write("##")
    with st.container():
        col7,col8 = st.columns(2)
        with col7:
            st.markdown("- During my college life, I had the privilege of being an active member of the college committee, where I made significant contributions and achieved several milestones. My journey began as a dedicated NSS (National Service Scheme) member, and after six months of unwavering dedication and hard work, I earned the position of NSS Treasurer, a testament to my commitment and leadership abilities.")
            st.markdown("- As the NSS Treasurer, I played a crucial role in managing the finances and resources of the organization. This included budget planning, fund allocation, and ensuring that all financial transactions were executed efficiently. I took on this responsibility with utmost diligence, ensuring that the NSS initiatives and projects ran smoothly without financial constraints.")
            st.markdown("""- One of my most notable achievements during my college life was the organization of a webinar titled "MANN SE BAAT." This webinar focused on the crucial topic of emotional and mental health, addressing the well-being of students and the importance of seeking help when needed. It was a remarkable event that brought together experts, students, and faculty members to engage in insightful discussions and share valuable insights on mental health issues. "MANN SE BAAT" was widely appreciated and played a pivotal role in creating awareness about the significance of mental health support in the college community.""")
            st.markdown("""- My active involvement in the college committee, from being an NSS member to attaining the position of NSS Treasurer and organizing impactful events like "MANN SE BAAT," reflects my dedication, leadership skills, and commitment to making a positive impact on campus life. These achievements not only enriched my college experience but also left a lasting legacy of promoting mental well-being and community engagement within the college community.""")
        with col8:
            st_lottie(lottie_ach)
EMAIL= "sohailsayyad10032002@gmail.com"

if selected=="Contact Me":
    st.subheader(':mailbox: Get in touch with me')
    st.write("📫", EMAIL)
    st.write('##')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")
    st.markdown("""<style> a{"text-decoration": none} </style>""", unsafe_allow_html=True)
    st.write("##")
    st.markdown(contact_form,unsafe_allow_html=True)
    st.markdown(contact_form_style,unsafe_allow_html=True)


if selected=='Projects':

    st.write('##')
    st.subheader('Car Price Prediction WebApp')
    st.write('##')
    right_col1,left_col1=st.columns((2,1))
    with right_col1:
        st.markdown("""- Car price prediction model using Random Forest and Streamlit combines machine learning with a user-friendly web interface to offer estimates of car prices based on various input features. It provides a valuable tool for potential car buyers and sellers to make more informed decisions about car pricing.\n""")
        st.markdown("- When a user inputs the features, the Streamlit application sends this data to the trained Random Forest model. The model uses the provided features to make predictions about the car's price. The predicted price is then displayed to the user on the web interface.")
        st.markdown("- Streamlit, a Python library for building web applications with minimal code, is used to create the user interface. Users interact with the web application by inputting features of the car they want to estimate the price for, such as make, model, year, mileage, and more.")
        st.markdown("- The Random Forest algorithm is chosen for its ability to handle both numerical and categorical features, and its capability to capture complex relationships in the data. The dataset is split into a training set and a testing set for model evaluation. The Random Forest model is trained on the training data, learning from the historical car prices and their corresponding features.")
        st.markdown("- [Click me to see the github repository ](https://github.com/Soyal10/Streamlit-app)")

    with left_col1:
        load_car_price_pic(car_pic_path)

    st.write('##')
    st.subheader("Iris Flower Classification ML model")
    st.write('##')
    right_col,left_col= st.columns((1,2))
    with right_col:
        load_iris_pic(iris_pic_path)
    with left_col:
        st.markdown("- The iris data set is widely used as a beginner's dataset for machine learning purposes. The dataset is included in R base and Python in the machine learning library scikit-learn, so that users can access it without having to find a source for it. ")
        st.markdown("- The algorithm used in this model is SVM. In machine learning, support vector machines (SVMs, also support vector networks[1]) are supervised learning models with associated learning algorithms that analyze data for classification and regression analysis." )
        st.markdown("- Successfully done the EDA of the iris flower dataset")
        st.markdown("- [Click me to see the github repository](https://github.com/Soyal10/IrisFlowerModel)")
    st.write("##")
    st.subheader("Full Pledge Password Manager")
    st.write('##')
    right_col2,left_col2=st.columns((2,1))
    with left_col2:
        load_passwordManager_pic(password_pic_path)

    with right_col2:
        st.markdown("- The password manager with JSON file storage and master key access ensures that users' login credentials are kept secure through encryption and a hashed master key. This combination of features helps users safely manage their passwords, protecting them from unauthorized access.")
        st.markdown("- Users can input their login credentials (e.g., usernames and passwords) into the password manager application. This data is stored in a JSON file, which can organize and categorize passwords for different accounts or services.")
        st.markdown("- To enhance security, the master key is hashed using a cryptographic hash function (e.g., SHA-256). The resulting hash is what's actually stored in a separate TXT file, not the plaintext master key. This adds an extra layer of security.")
        st.markdown("- Users can add, edit, or delete stored passwords as needed. They can also organize passwords by categories (e.g., work, personal, financial) for easier management.")
        st.markdown("- [Click me to see the github repository](https://github.com/Soyal10/FULL-PLEDGE-PASSWORD-MANAGER)")
    st.write("##")

    st.subheader("Name the states game")
    right_col3,left_col3= st.columns((1,2))
    with right_col3:
        load_game_pic(game_pic_path)

    with left_col3:
        st.markdown("-  This Python project utilizes the Pandas library for data handling, Tkinter for the GUI, and a geographical dataset to create an educational and interactive game. Players are tasked with identifying and naming the states of a country, with their score increasing as they correctly name each state. It's a fun way to learn geography while enjoying a gaming experience.")
        st.markdown("- The user is presented with a text input field where they can type the names of the states or regions within that country. The user's objective is to correctly identify and name all the states.")
        st.markdown("- As the user types in state names, the program checks whether the entered state is correct or not. If the user types a correct state name, that state's name is displayed on the map, and the user's score is updated.")
        st.markdown("- The user's score is displayed on the GUI and increases each time they correctly identify a state. Incorrect entries do not affect the score negatively.")
        st.markdown("- [Click me to see the github repository](https://github.com/Soyal10/Name_the_states_game) ")