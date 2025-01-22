#pip install snowflake-snowpark-python

# Import python packages
from snowflake.snowpark.session import Session

import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col



###########
# Define connection parameters
connection_parameters = {
    "account": "AHOIGHT-MDB97041",
    "user": "ANJALI30",
    "password": "123Gumpaste2002",
    "role": "SYSADMIN",
    "warehouse": "COMPUTE_WH",
    "database": "SMOOTHIES",
    "schema": "PUBLIC"
}

# Attempt to create a session
try:
    new_session = Session.builder.configs(connection_parameters).create()
    #st.success("Successfully connected to Snowflake!")
except Exception as e:
    st.error(f"Error creating Snowflake session: {e}")
########




# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie:cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom Smoothie!
    """)

#import streamlit as st

name_on_order = st.text_input('Name on Smoothie: ')
st.write("The name on your smoothie will be:", name_on_order)

cnx=st.connection("snowflake")
session=cnx.session()
#connection_parameters={
 #   "account":"AHOIGHT-MDB97041",
  #  "user":"ANJALI30",
 #   "password":"123Gumpaste2002",
  #  "role":"SYSADMIN",
   # "warehouse":"COMPUTE_WH",
  #  "database":"smoothies",
   # "schema":"PUBLIC"
#}
###new_session=Session.builder.configs(connection_parameters).create()
#session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    "Choose up to 5 ingredients:",
   my_dataframe ,
    max_selections=5
)

if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)

    ingredients_string = ''

    for fruit_chosen in ingredients_list:
    
        ingredients_string += fruit_chosen + ' '

    #st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order + """')"""

    #st.write(my_insert_stmt)
    #st.stop()
    #st.write(my_insert_stmt)
    time_to_insert = st.button('Submit Order')
    
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        #st.success('Your Smoothie is ordered!',icon="✅")
        st.success(f"Your Smoothie is ordered, {name_on_order}!", icon="✅")
###import requests
###smoothiefroot_response = requests.get("https://www.fruityvice.com/#3")
#st.text(smoothiefroot_response.json)
###sf_df=st.dataframe(data=smoothiefroot_response.json(), use_container_width=True)
import requests
smoothiefroot_response = requests.get("https://www.fruityvice.com/#3")
#st.text(smoothiefroot_response.json())
#print(smoothiefroot_response.text) 
#st.content(smoothiefroot_response)
print("Content-Type:", response.headers.get('Content-Type'))
import requests
smoothiefroot_response = requests.get("https://www.fruityvice.com/#3")
st.text(smoothiefroot_response)
#("https://my.smoothiefroot.com/api/fruit/watermelon"
