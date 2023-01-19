import streamlit as st 
import streamlit.components.v1 as components
import static
from PIL import Image

st.set_page_config(page_title="Eshban Suleman", layout="wide", page_icon="👨‍🔬")

image = Image.open("./media/imgs/me.jpeg")

with st.sidebar:
    components.html(static.embeds["linkedin"], height=200)
    st.image(image)

st.header("About Me 📖")
st.write(static.info["intro"])

st.sidebar.caption("Contact me at")
st.sidebar.write(f"📧 {static.info['email']}")
pdfFileObj = open(static.info["resume"], 'rb')
st.sidebar.download_button("Download Resume", pdfFileObj, file_name="CV_Eshban.pdf", mime="pdf")

st.header("Experience ⏳")
st.subheader("Senior Data Scientist")
st.caption("Foretheta (November 2019 - Present)")
tab1, tab2 = st.tabs(["Responsibilities", "Tech Stack"])
with tab1:
        for r in static.responsibilities:
            st.markdown(r)
with tab2:
        for s in static.stack:
            st.markdown(s)

st.header("Skills & Tools ⚒️")
levels = ["Advance", "Intermediate", "Beginner"]
for tab, level in zip(st.tabs(levels), levels):
    with tab:
        for i, j, k in zip(static.skills[level][::3], static.skills[level][1::3], static.skills[level][2::3]):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(i)
            with col2:
                st.markdown(j)
            with col3:
                st.markdown(k)


st.header("Projects 🗃")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Reginald von Doom 🤵🏽")
    with st.expander("Info"):
        for item in static.projects_info["Reginald von Doom"]:
            st.markdown(item)
    with st.expander("Reginald von Doom Quick Demo"):
        video_file = open(static.vids["reginald-vid"], "rb")
        video_bytes = video_file.read()
        st.video(video_bytes)

with col2:
    st.subheader("Movie Recommendation Engine 🎥")
    with st.expander("Info"):
        for item in static.projects_info["MRE"]:
            st.markdown(item)
    with st.expander("Movie Recommendation Engine Quick Demo"):
        video_file = open(static.vids["mre-vid"], "rb")
        video_bytes = video_file.read()
        st.video(video_bytes)

st.header("Certifications 🗂")
counter = 0
with st.container():
    with st.expander("View My Certificates Below"):
        for row in range(2):
            for col in st.columns(3):
                with col:
                    col.image(static.imgs[counter])
                    st.subheader(static.imgs_titles[counter])
                    st.markdown(static.imgs_captions[counter], unsafe_allow_html=True)
                    counter += 1
        st.markdown(f"To see more, [click here]({static.link})", unsafe_allow_html=True)

st.header("Blogs ✍🏽")
with st.expander("Read My Blogs Below"):
    st.markdown("""<a href={}> Access Full Profile Here</a>""".format(static.info["medium"]), unsafe_allow_html=True)
    components.html(static.embeds["medium"], height=500)

st.header("Twitter 🔔")
with st.expander("Follow Me On Twitter"):
    components.html(static.embeds["twitter-feed"], height=500)
    components.html(static.embeds["twitter-profile"], height=100)