import streamlit

streamlit.title('my parents new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega3 & Blueberry Oatmeal')
streamlit.text('Kale,Spinach and Rocket smoothie')
streamlit.text('Hard boiled free range egg')  


fruits_seleced = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
streamlit.dataframe(fruits_to_show)
