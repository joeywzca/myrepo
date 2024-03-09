import streamlit as st
import pandas as pd
import plost

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('CDC Operation Dashboard')

st.sidebar.subheader('Outbound Flow')
time_hist_color = st.sidebar.selectbox('Color by', ('Parcel', 'Penguin','Bolt','RXO','Windsor','London','Barrie','MANITL','TODO Store','SCAR Store','TODO CP','SCAR CP','UTG')) 

st.sidebar.subheader('Inbound Type')
donut_theta = st.sidebar.selectbox('Select data', ('Perryville', 'Beauharnois','Supplier','Kleinburg'))

st.sidebar.subheader('Order Booked By Route')
plot_data = st.sidebar.multiselect('Select data', ['Parcel', 'Penguin','YL','MANITL','TODO CP','SCAR CP'], ['Parcel', 'Penguin','YL','MANITL','TODO CP','SCAR CP'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

st.sidebar.markdown('''
---
Welcome to CDC Toronto.
''')


# Row A
st.markdown('### Operation Overview FY24')
col1, col2, col3 = st.columns(3)
col1.metric("Picking Goal", "22.36 Lines/Hr", "-0.01")
col2.metric("Packing Goal", "16 Pkg/Hr", "2.23")
col3.metric("HCS Goal", "75", "Week 8: -2")

# Row B
seattle_weather = pd.read_csv('Orders_Booked.csv')
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Orderline Fulfilled VS STP')
    plost.time_hist(
    data=seattle_weather,
    date='Date',
    x_unit='Week',
    y_unit='OLs',
    color=time_hist_color,
    aggregate='median',
    legend=None,
    height=345,
    use_container_width=True)
with c2:
    st.markdown('### Inbound Overview')
    plost.donut_chart(
        data=stocks,
        theta=donut_theta,
        color='company',
        legend='bottom', 
        use_container_width=True)

# Row C
st.markdown('### Order Booked By Route')
st.line_chart(seattle_weather, x = 'Date', y = 'OLs', height = plot_height)
