
import streamlit as st
import pandas as pd
from datetime import datetime
import sqlite3
import pymysql
import base64

import matplotlib.pyplot as plt

conn = pymysql.connect(host="localhost",user="root",password="Sure@1206",database="nasa_db")
cursor=conn.cursor()
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;color: #1108BBE'> Insight -Nasa Asteroid </h1>", unsafe_allow_html=True)
#st.image(r"C:/Users/Hashvetha/OneDrive/Desktop/ast2.jpg")
with open(r"C:/Users/Hashvetha/Downloads/nasaim.webp", "rb") as image_file:
 
    img_base64 = base64.b64encode(image_file.read()).decode('utf-8')
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.divider()

with st.sidebar:
 page = st.sidebar.radio("Go to", ["About Nasa Project", "Filter Criterias", "SQL-Asteroids Data"])

# -------------------------------- PAGE 1: Introduction --------------------------------
if page == "About Nasa Project":
    st.title(" NEO Data Analysis")
    st.subheader(" A Streamlit App for Analysing Asteroids & to Explore Astronomical data.")
    st.write("""
    This project analyzes Asteroids,astronomical data month wise using an MYSQL database.
    It provides visualizations for Asteroid with highest Brightness, Asteroid Speed, count of hazardous vs non-hazardous asteroids
    and asteroid with the most close approaches.
    **Features:**
    - View and filter asteroids data by month, close approaches
    - Generate dynamic visualizations.
    - Run predefined SQL queries to explore insights.
    **Database Used:** `Nasa_DB`
    """)

# -------------------------------- PAGE 2:  Data Visualization --------------------------------

elif page=="SQL-Asteroids Data":
        
 #with st.sidebar:

               options = st.selectbox("Queries",[
                      "1. No.of Times each asteroid has approached Earth(count)",
                      "2. Average velocity of each asteroid over multiple approaches",
                      "3. Top 10 fastest asteroids",
                      "4. Potentially hazardous asteroids that have approached Earth more than 3 times",
                      "5. Month with the most asteroid approaches",
                      "6. Asteroid with the fastest ever approach speed",
                      "7. Asteroids by maximum estimated diameter (descending)",
                      "8. Asteroid whose closest approach is getting nearer over time",
                      "9. Asteroids name, date & miss_distance of Asteroids closest approach to Earth.",
                      "10. Names of asteroids that approached Earth with velocity > 50,000 km/h",
                      "11. Count of approaches happened per month",
                      "12. Asteroid with the highest brightness",
                      "13. Number of hazardous asteroids",
                      "14. Number of non-hazardous asteroids",
                      "15. Asteroids,close_approach_date and distance that passed closer than the Moon",
                      "16. Asteroids that came within 0.05 AU(astronomical distance)"
                      ],placeholder='Select an option...',index=None)
               if options == "1. No.of Times each asteroid has approached Earth(count)":
                        cursor.execute('select id, count(distinct(id)) from asteroids group by 1')
                        result =  cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description]
                        data = pd.DataFrame(result,columns=columns)
                        st.dataframe(data) 

               elif options == "2. Average velocity of each asteroid over multiple approaches":
                        cursor.execute('select neo_reference_id, AVG(relative_velocity_kmph) AS Avg_Veloicty FROM close_approach group by neo_reference_id')
                        result = cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description]
                        data = pd.DataFrame(result,columns=columns)
                        st.dataframe(data) 

               elif options == "3. Top 10 fastest asteroids":
                        cursor.execute('select distinct(relative_velocity_kmph),neo_reference_id AS Asteroid_ID FROM close_approach ORDER BY relative_velocity_kmph DESC LIMIT 10')
                        result = cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description]
                        data = pd.DataFrame(result,columns=columns)
                        st.dataframe(data) 
               elif options == "4. Potentially hazardous asteroids that have approached Earth more than 3 times":
                        cursor.execute("SELECT a.name,ca.neo_reference_id, COUNT(*) as close_approach_count from nasa_db.close_approach as ca inner join nasa_db.asteroids as a on ca.neo_reference_id = a.id WHERE a.is_potentially_hazardous_asteroid = 0 AND orbiting_body = 'Earth'GROUP BY a.name,ca.neo_reference_id HAVING COUNT(*) > 3 ORDER BY close_approach_count DESC")
                        result = cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description]
                        data = pd.DataFrame(result,columns=columns)
                        st.dataframe(data) 


               elif options == "5. Month with the most asteroid approaches":
                        cursor.execute('select neo_reference_id, AVG(relative_velocity_kmph) AS Avg_Veloicty FROM close_approach group by neo_reference_id')
                        result = cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description]
                        data = pd.DataFrame(result,columns=columns)
                        st.dataframe(data) 

               elif options == "6. Asteroid with the fastest ever approach speed":
                        cursor.execute('select neo_reference_id, AVG(relative_velocity_kmph) AS Avg_Veloicty FROM close_approach group by neo_reference_id')
                        result = cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description]
                        data = pd.DataFrame(result,columns=columns)
                        st.dataframe(data) 
                
               elif options == "7. Asteroids by maximum estimated diameter (descending)":
                        cursor.execute('select neo_reference_id, AVG(relative_velocity_kmph) AS Avg_Veloicty FROM close_approach group by neo_reference_id')
                        result = cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description]
                        data = pd.DataFrame(result,columns=columns)
                        st.dataframe(data)
                
               elif options == "8. Asteroid whose closest approach is getting nearer over time":
                        cursor.execute('select a.name,COUNT(c.neo_reference_id) AS approach_count FROM asteroids a JOIN close_approach c ON a.id = c.neo_reference_id GROUP BY a.name ORDER BY approach_count DESC')
                        result = cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description]
                        data = pd.DataFrame(result,columns=columns)
                        st.dataframe(data)  
                
               elif options == "9. Asteroids name, date & miss_distance of Asteroids closest approach to Earth.":
                        cursor.execute("select a.name,ca.close_approach_date,ca.miss_distance_km FROM close_approach ca JOIN  asteroids a ON a.id = ca.neo_reference_id WHERE ca.orbiting_body = 'Earth'")
                        result = cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description]
                        data = pd.DataFrame(result,columns=columns)
                        st.dataframe(data)  
                
               elif options == "10. Names of asteroids that approached Earth with velocity > 50,000 km/h":
                        cursor.execute("select DISTINCT a.name,ca.relative_velocity_kmph FROM close_approach ca JOIN asteroids a ON a.id = ca.neo_reference_id WHERE ca.orbiting_body = 'Earth'AND ca.relative_velocity_kmph*10000")
                        result = cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description]
                        data = pd.DataFrame(result,columns=columns)
                        st.dataframe(data)  
                
               elif options == "11. Count of approaches happened per month":
                        cursor.execute("SELECT DATE_FORMAT(close_approach_date, '%Y-%d') as ym, count(*) FROM close_approach GROUP BY ym ORDER BY ym")
                        result = cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description]
                        data = pd.DataFrame(result,columns=columns)
                        st.dataframe(data)  
                
               elif options == "12. Asteroid with the highest brightness":
                        cursor.execute('SELECT name,  absolute_magnitude_h FROM asteroids ORDER BY  absolute_magnitude_h ASC LIMIT x`1')
                        result = cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description]
                        data = pd.DataFrame(result,columns=columns)
                        st.dataframe(data)  
                
               elif options == "13. Number of hazardous asteroids":
                        cursor.execute('select id,count(id) as cnt_Hazardous_Asteroid from  nasa_db.asteroids where is_potentially_hazardous_asteroid =1 group by 1')
                        result = cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description]
                        data = pd.DataFrame(result,columns=columns)
                        st.dataframe(data)  
                
               elif options == "14. Number of non-hazardous asteroids":
                        cursor.execute('select id,count(id) as cnt_Non_Hazardous_Asteroid from  nasa_db.asteroids where is_potentially_hazardous_asteroid =0 group by 1')
                        result = cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description]
                        data = pd.DataFrame(result,columns=columns)
                        st.dataframe(data)  
                
               elif options == "15. Asteroids,close_approach_date and distance that passed closer than the Moon":
                        cursor.execute("SELECT  a.name AS asteroid_name, ca.close_approach_date, ca.miss_distance_km FROM  close_approach ca JOIN  asteroids a ON a.id = ca.neo_reference_id WHERE ca.orbiting_body = 'Earth' AND ca.miss_distance_lunar<1 ORDER BY ca.miss_distance_km asc")
                        result = cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description]
                        data = pd.DataFrame(result,columns=columns)
                        st.dataframe(data)  
                
               elif options == "16. Asteroids that came within 0.05 AU(astronomical distance)":
                        cursor.execute('Select neo_reference_id,astronomical from close_approach where astronomical<=0.05')
                        result = cursor.fetchall()
                        columns = [desc[0] for desc in cursor.description]
                        data = pd.DataFrame(result,columns=columns)
                        st.dataframe(data)  
# -------------------------------- PAGE 3: Filter --------------------------------




elif page =="Filter Criterias":
 c1,a,c2,b,c3=st.columns([0.4,0.4,0.4,0.4,0.4])
 with c1:
    mag_min=st.slider("Min Magnitude",19.00,19.38,(19.00,19.38 ))

#Diameter
    diam_min=st.slider("Min Est Diam in KM",0.70,0.800,value=(0.70,0.800))
    diam_max=st.slider("Max Est Diam in KM",0.30,0.800,value=(0.30,0.800))

 with c2:
    velocity=st.slider("Rel_velocity",15,20,value=(15,20))
    astro=st.slider("Astro Unit",5.16453e-05,0.4999515747)
    hazardous=st.selectbox("only show pot hazardous",options =[0,1],index=0)

 with c3:
    start_date=st.date_input("start date",datetime(2024,1,1))
    end_date=st.date_input("End date",datetime(2025,1,13))

 if st.button("Apply Filters"):
        query = f"""
            SELECT *
            FROM nasa_db.asteroids a
            JOIN nasa_db.close_approach c ON a.id = c.neo_reference_id
            WHERE a.absolute_magnitude_h  BETWEEN {mag_min[0]} AND {mag_min[1]}
              AND a.estimated_diam_min_km  BETWEEN {diam_min[0]} AND {diam_min[1]}
              AND a.estimated_diam_max_km  BETWEEN {diam_max[0]} AND {diam_max[1]}
              AND c.relative_velocity_kmph BETWEEN {velocity[0]} AND {velocity[1]}
              AND c.astronomical >= {astro}
              AND a.is_potentially_hazardous_asteroid = {hazardous}
              AND DATE(c.close_approach_date) BETWEEN DATE('{start_date}') AND DATE('{end_date}')
            LIMIT 10000;
        """

        cursor.execute(query)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        if result:
            df = pd.DataFrame(result, columns=columns)
            st.dataframe(df)
        else:
            st.warning("No asteroids found for the given filter criteria.")

    