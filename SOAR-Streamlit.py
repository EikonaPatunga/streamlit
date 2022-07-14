###SOAR Streamlit App - Main Page


#import package dependencies
#B -- Ignore, you would only use this if you wanted to import NEW components that are not built into Streamlit by default, 
# and I can always help with this step!
import streamlit as st

"Session State Dict *For Reference While Coding Page*", st.session_state
###Title
st.title('SOAR - Data Visualization/Generator')

#Header
st.header('Categories')

st.subheader('Business Model')
st.write ('Independent Variables')