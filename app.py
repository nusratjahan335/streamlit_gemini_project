import streamlit as st 
from api_calling import note_generator,audio,quiz_genaretor
from PIL import Image


st.title("Note summary and Quiz Generator")
st.markdown("Upload atmost 3 images")
st.divider()

with st.sidebar:
    st.header("Controls")

    images = st.file_uploader(
        "Upload the photos of ur notes",
        type=['jpg','png','jpge'],
        accept_multiple_files=True
    )

    pil_image = []

    for img in images:
        #name must be different
        pil_img = Image.open(img)
        pil_image.append(pil_img)

    if pil_image:
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            st.subheader("Uploaded images")
            colume = st.columns(len(images))  

            for i,img in enumerate(images):
                with colume[i]:
                    st.image(img)
    #difficulty
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy","Medium","Hard"),
        index=None
    )  

  
    prassed = st.button("Click the button to initiate AI",type="primary")  

if prassed:
    if not images:
        st.error("u must upload 1 image")
    if not selected_option:
        st.error("You must select a difficulty") 
    if images and selected_option:

        #note
        with st.container(border= True):
            st.subheader("Your Notes")

            with st.spinner("AI is generating the notes"):
                generated_notes = note_generator(pil_image)
                st.markdown(generated_notes)

        # audio
        with st.container(border= True):
            st.subheader("Audio")
            with st.spinner("AI is generating the audio"):
                generated_notes = generated_notes.replace("#","")
                generated_notes = generated_notes.replace("*","")
                generated_notes = generated_notes.replace("-","")
                generated_notes = generated_notes.replace("'","")
                

                audio_trans = audio(generated_notes)
                st.audio(audio_trans)
        # 
        # quiz
        with st.container(border= True):
            st.subheader(f"Quiz ({selected_option}) Difficulty")

            with st.spinner("AI is generating the quizzes"):
                quizzes = quiz_genaretor(pil_image,selected_option)
                st.markdown(quizzes)       


            

        