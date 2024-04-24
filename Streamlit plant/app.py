import streamlit as st
from st_on_hover_tabs import on_hover_tabs
import pandas as pd

st.set_page_config(layout="wide")

st.header("Botanix Ayurvedic Website")
# st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)
df= pd.read_csv('gj.csv')

with st.sidebar:
    tabs = on_hover_tabs(tabName=['CNN', 'Chatbot', 'Information'],
                          iconName=['dashboard', 'money', 'economy'], 
                         default_choice=0)

if tabs =='CNN':
    # st.title("Scanner App")
    
    from PIL import Image
    import tensorflow as tf
    import numpy as np
    model = tf.keras.models.load_model(r"plant.h5") 

    # st.title('Plant')
    st.write('Plant checker')

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

        image = Image.open(uploaded_file)
        image = image.resize((224, 224))  
        image = tf.keras.preprocessing.image.img_to_array(image)
        image = tf.image.convert_image_dtype(image, tf.float32)
        image = np.expand_dims(image, axis=0)  # Add an extra dimension for batch

        # Make prediction
        prediction = model.predict(image)
        pred = np.argmax(prediction, axis=1)
        # st.write(pred)
        
        if pred == 0:
            st.write("Aloevera - ઘૃતકુમાર (Ghritakumār)")
            st.write("Climate:")
            st.write(df['Climate'][0])
            st.write("How to grow:")
            st.write(df['How'][0])
            st.write("Region:")
            st.write(df['region'][0])
            st.write("Soil:")
            st.write(df['soil'][0])
            st.write("Uses:")
            st.write(df['uses'][0])
            st.write("Who should avoid:")
            st.write(df['who'][0])
            
        if pred == 1:
            st.write("Jamun - જાંબુ (Jāmbu)")
            st.write("Aloevera - ઘૃતકુમાર (Ghritakumār)")
            st.write("Climate:")
            st.write(df['Climate'][1])
            st.write("How to grow:")
            st.write(df['How'][1])
            st.write("Region:")
            st.write(df['region'][1])
            st.write("Soil:")
            st.write(df['soil'][1])
            st.write("Uses:")
            st.write(df['uses'][1])
            st.write("Who should avoid:")
            st.write(df['who'][1])
        if pred == 2:
            st.write("Jasmine - મોગરો (Mogaro)")

        if pred == 3:
            st.write("Mango - કેરી (Kerī)")
            st.write("Climate:")
            st.write(df['Climate'][2])
            st.write("How to grow:")
            st.write(df['How'][2])
            st.write("Region:")
            st.write(df['region'][2])
            st.write("Soil:")
            st.write(df['soil'][2])
            st.write("Uses:")
            st.write(df['uses'][2])
            st.write("Who should avoid:")
            st.write(df['who'][2])
        if pred == 4:
            st.write("Mint - પુદીનો (Pudīnō)")
        if pred == 5:
            st.write("Neem - લીમડો (Līmaḍō)")
            st.write("Climate:")
            st.write(df['Climate'][1])
            st.write("How to grow:")
            st.write(df['How'][1])
            st.write("Region:")
            st.write(df['region'][1])
            st.write("Soil:")
            st.write(df['soil'][1])
            st.write("Uses:")
            st.write(df['uses'][1])
            st.write("Who should avoid:")
            st.write(df['who'][1])
        if pred == 6:
            st.write("Peepal - પીપળ (Pīpaḷ)")
        if pred == 7:
            st.write("Tulsi - તુલસી (Tulasi)")
            st.write("Climate:")
            st.write(df['Climate'][3])
            st.write("How to grow:")
            st.write(df['How'][3])
            st.write("Region:")
            st.write(df['region'][3])
            st.write("Soil:")
            st.write(df['soil'][3])
            st.write("Uses:")
            st.write(df['uses'][3])
            st.write("Who should avoid:")
            st.write(df['who'][3])
            
            

elif tabs == 'Chatbot':
    import openai
    st.title("Botanix Bot")

    openai.api_key = "sk-48BKsWFBr2KhQdQzBeINT3BlbkFJWWa3jT7zGLdzQnf409PoS"

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for response in openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            ):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    
    
    
elif tabs == 'Information':
    st.dataframe(df)
    



# from PIL import Image
# import tensorflow as tf
# import numpy as np






# model = tf.keras.models.load_model(r"plant.h5") 

# st.title('Plant')
# st.write('Plant checker')

# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# if uploaded_file is not None:
#     st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

#     image = Image.open(uploaded_file)
#     image = image.resize((224, 224))  
#     image = tf.keras.preprocessing.image.img_to_array(image)
#     image = tf.image.convert_image_dtype(image, tf.float32)
#     image = np.expand_dims(image, axis=0)  # Add an extra dimension for batch

#     # Make prediction
#     prediction = model.predict(image)
#     pred = np.argmax(prediction, axis=1)
#     # st.write(pred)
    
#     if pred == 0:
#         st.write("Aloevera - ઘૃતકુમાર (Ghritakumār)")
#     if pred == 1:
#         st.write("Jamun - જાંબુ (Jāmbu)")
#     if pred == 2:
#         st.write("Jasmine - મોગરો (Mogaro)")
#     if pred == 3:
#         st.write("Mango - કેરી (Kerī)")
#     if pred == 4:
#         st.write("Mint - પુદીનો (Pudīnō)")
#     if pred == 5:
#         st.write("Neem - લીમડો (Līmaḍō)")
#     if pred == 6:
#         st.write("Peepal - પીપળ (Pīpaḷ)")
#     if pred == 7:
#         st.write("Tulsi - તુલસી (Tulasi)")
    

    

