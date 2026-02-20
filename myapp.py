import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello Streamlit")
st.write("lorem10")
st.text("lorem20")

name= st.text_input("Enter your name")
if st.button("Submit"):
    st.success("hello,{name}!")

df= pd.DataFrame(np.random.randn(10,2),columns=['A','B'])
st.line_chart(df)
st.bar_chart(df)

# media layout
st.sidebar.title("navigation")
st.image("https://t4.ftcdn.net/jpg/13/88/07/53/360_F_1388075302_D6UDD0gW1JH6MhfyQhFGGgBT0IPyKi5a.jpg", caption="sample image")
st.video("https://www.youtube.com/watch?v=TwC0Db7oerM")

# upload file 

upload_file = st.file_uploader("upload a csv", type='csv')
if upload_file:
    df=pd.read_csv(upload_file)
    st.dataframe(df)


st.title("📝 Text and Markdown Demo")

st.header("This is a header")
st.subheader("This is a subheader")

st.markdown("**Bold**, *italic*, `code`, [Link](https://streamlit.io)")

st.code("for i in range(5): print(i)", language="python")

name = st.text_input("What's your name?")
text = st.text_area("Write something...")

number = st.number_input("Pick a number", min_value=0, max_value=100)
range_val = st.slider("Choose a range", 0, 100)

fruit = st.selectbox("Select a fruit", ["Apple", "Bananas", "Mango"])
toppings = st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])

choice = st.radio("Pick one", ["Option A", "Option B"])
agree = st.checkbox("I agree to the terms")

if name:
    st.write(f"Hello, {name} 👋")

st.write("Number:", number)
st.write("Range:", range_val)
st.write("Fruit:", fruit)
st.write("Toppings:", toppings)
st.write("Choice:", choice)
st.write("Agreed:", agree)