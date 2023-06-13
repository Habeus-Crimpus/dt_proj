import streamlit as st
import json
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
#from params import DATA_PATH
from darktriad.ml_logic.preprocess import preprocess
from darktriad.ml_logic.Feat_engine import feature_engineering
import requests

def result_page():
    
    st.header("Page Result Content")
    st.markdown("Hello")
    # Add content specific to Page 4
    # scores
    # plots
    # interpretation
    
def placement(x:int):
   if x == -1:
       st.write('You placed below the expected score')
   elif x == 0:
       st.write('You are within the expected range')
   else:
       st.write('You are above the expected score')
  
    
def finish(select):
       api_url = f'http://localhost:4000/predict?user_answers={answers}'

       response = requests.get(api_url)
       global preds
       preds = response.json()


       st.write('PSYCHOPATHY')
       placement(preds["Psych_Pred"])
       st.write('NARCISSISM')
       placement(preds["Narc_Pred"])
       st.write('MACHIAVELLIANISM')
       placement(preds["Mach_Pred"])
