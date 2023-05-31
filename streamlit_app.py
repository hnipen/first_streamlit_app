import streamlit
import pandas

streamlit.title('My parents new UNhealthy dinner')

streamlit.header('Breakfast menu')
streamlit.text('🥣   Omega 3 & Blueberry')
streamlit.text('🥗   Kale, Spinach & Rocket Smnoothie')
streamlit.text('🐔   Hard-boiled Free-range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
