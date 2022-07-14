###SOAR Streamlit App - Independent Variables Page


#import package dependencies
#B -- Ignore, see main file for explanation
import streamlit as st

##Session State Object - for checking logic live
"Session State Dict *For Reference While Coding Page*", st.session_state

# Initialization
if 'inputUnit' not in st.session_state:
    st.session_state.inputUnit = 5000
if 'inputWage' not in st.session_state:
    st.session_state.inputWage = 20.00
if 'sqFtInput' not in st.session_state:
    st.session_state.sqFtInput = 5000
if 'workers' not in st.session_state:
    st.session_state.workers = 1
if 'pricePer' not in st.session_state:
    st.session_state.pricePer = 0.25
if 'timeNeeded' not in st.session_state:
    st.session_state.pricePer = 0.15

###Class definition - Independent Variables


###Functions
def update_input():
    st.session_state.sliderUnit = st.session_state.inputUnit
def update_slider():
    st.session_state.inputUnit = st.session_state.sliderUnit
def updateWage_input():
    st.session_state.sliderWage = st.session_state.inputWage
def updateWage_slider():
    st.session_state.inputWage = st.session_state.sliderWage
def updateSize_sqFt():
    st.session_state.unitsInput = (st.session_state.sqFtInput / st.session_state.inputUnit)
def updateSize_units():
    st.session_state.sqFtInput = (st.session_state.unitsInput * st.session_state.inputUnit)
###


###Title
st.title('Calculating an Individual SDR')

st.header('Declaring Independent Variables')

###########################
####     Variables     ####
###########################

#####
#Standard Unit Size
st.subheader('Standard Unit Size')
st.write('What is the standard unit size in Sq.Ft of a scan? We charge by the # of units')
col1, buff, col2 = st.columns([2,1,2])
with col1:
  st.number_input(label='', key='inputUnit', step = 1, on_change=update_input)
with buff:
  st.subheader('Sq.Ft')
with col2:
  st.slider(label='', min_value = 0, max_value = 10000, key='sliderUnit', on_change=update_slider)
#####


#####
#Standard Hourly Wage
st.subheader('Standard Hourly Wage')
st.write('What is the standard worker paid in terms of dollars/hour scanned')
col3, buff2, col4 = st.columns([2,1,2])
with col3:
  st.number_input(label='', key='inputWage', step = 1.00, on_change=updateWage_input)
with buff2:
  st.subheader('$ Per Hour')
with col4:
  st.slider(label='', min_value = 0.00, max_value = 100.00, key='sliderWage', on_change=updateWage_slider)
#####

#####
#Price/SqFt
st.subheader('Price/Sq.Foot')
st.write('What is the price per square foot')
st.slider('In Cents', min_value = 0.05, max_value = 1.0, key = 'pricePer')
#####

st.button('Set')





#Headers

st.header('Specify Order')


#####
#Total Sq Feet of Order
st.subheader('Total Sq. Ft')
st.write('How large is the order')
col7, buff4, col8 = st.columns([2,1,2])
with col7:
  st.number_input(label='sqFt', key='sqFtInput', step = 1.00, on_change=updateSize_sqFt)
with buff4:
  st.subheader('=')
with col8:
  st.number_input(label='Units', key='unitsInput', on_change=updateSize_units)
#####

st.subheader('Estimated needed to scan:')
timeNeeded = ((st.session_state.sqFtInput/9.18)/60)
st.write(timeNeeded, ' minutes')
st.write(timeNeeded/60, ' hours')

st.session_state['timeNeeded'] = (timeNeeded/60)


#####
#number of workers who fulfill order
st.subheader('Number of scanners who fulfill the order')
st.number_input('', key= 'workers', step = 1)



st.subheader('Cost of Workers:')
cost = st.session_state.workers * (st.session_state.inputWage * st.session_state.timeNeeded)
st.write(cost, ' USD')

st.subheader('Revenue from Order:')
revenue = ((st.session_state.pricePer * st.session_state.sqFtInput) * st.session_state.workers)
st.write(revenue, ' USD')

st.subheader('Profit from Order:')
profit = (revenue - cost)
st.write(profit, ' USD')


st.subheader('Margins:')
margins = (profit/cost)
st.write('Every ', 1, ' dollar spent : Gained ', margins, ' Dollars')