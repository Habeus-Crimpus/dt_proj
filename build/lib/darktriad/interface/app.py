'''
Creates the interface (streamlit)
'''
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
#import ipdb
from darktriad.interface.info_page import info_page
from darktriad.interface.front_page import front_page
from darktriad.interface.test_page import test_page
from darktriad.interface.result_page import result_page

start_button_clicked = False
#
#if 'counter' not in st.session_state.keys():
#    st.session_state.counter = 0
#i = st.session_state.counter
#
#if 'answers' not in st.session_state.keys():
#    st.session_state.answers = []
#global answers
#answers = st.session_state.answers
##
#questions = ["It's not wise to tell your secrets.",
#             "I like to use clever manipulation to get my way.",
#             "Whatever it takes, you must get the important people on your side. ",
#             "Avoid direct conflict with others because they may be useful in the future.",
#             "It’s wise to keep track of information that you can use against people later.",
#             "You should wait for the right time to get back at people. ",
#             "There are things you should hide from other people because they don’t need to know.",
#             "Make sure your plans benefit you, not others.",
#             "Most people can be manipulated.",
#             "People see me as a natural leader. ",
#             "I hate being the center of attention.",
#             "Many group activities tend to be dull without me.",
#             "I know that I am special because everyone keeps telling me so. ",
#             "I like to get acquainted with important people. ",
#             "I feel embarrassed if someone compliments me.",
#             "I have been compared to famous people. ",
#             "I am an average person.",
#             "I insist on getting the respect I deserve.",
#             "I like to get revenge on authorities.",
#             "I avoid dangerous situations.",
#             "Payback needs to be quick and nasty. ",
#             "People often say I’m out of control. ",
#             "It’s true that I can be mean to others. ",
#             "People who mess with me always regret it.",
#             "I have never gotten into trouble with the law.",
#             "I enjoy having sex with people I hardly know.",
#             "I’ll say anything to get what I want.",
#             "Are you a US citizen?"]
##
#def update(select):
#    answers.append(int(select))
#    global i
#    i += 1
#    st.session_state.answers = answers
#    st.session_state.counter = i
#
#global preds
#
#def placement(x:int):
#    if x == -1:
#        st.write('You placed below the expected score')
#    elif x == 0:
#        st.write('You are within the expected range')
#    else:
#        st.write('You are above the expected score')
#
#def finish(select):
#        api_url = f'http://localhost:4000/predict?user_answers={answers}'
#
#        response = requests.get(api_url)
#        global preds
#        preds = response.json()
#
#
#        st.write('PSYCHOPATHY')
#        placement(preds["Psych_Pred"])
#        st.write('NARCISSISM')
#        placement(preds["Narc_Pred"])
#        st.write('MACHIAVELLIANISM')
#        placement(preds["Mach_Pred"])
#
#
#
#def show_q_a(i):
#    select = st.selectbox(
#        f"{i+1})  {questions[i]}",
#        ('Select a number', '1', '2', '3', '4', '5')
#    )
#    if select != 'Select a number':
#        st.write('You selected:', select)
#        if (i < 27):
#            name = 'Continue'
#            st.button(name, on_click=update, args=select,key='a43')
#        else:
#            name = 'Submit'
#            st.button(name, on_click=finish, args=select,key='a43')
#

#
#
#
#
#
#
#def show_plots():
#    df = pd.read_csv(DATA_PATH, delimiter = '\t')
#    #df.head()#

#    df_after_preprocess = preprocess(df)
#    df_after_featureng = feature_engineering(df_after_preprocess)#

#    #Averages
#    #df_after_featureng
#    df_average = df_after_featureng.mean(axis=0)
#    df_average_traits = df_average.iloc[:27]
#    average_df = pd.DataFrame(df_average_traits)#

#    fig = px.bar(average_df,title="Average score for each question")
#    fig.update_layout(xaxis_title="Average scores", yaxis_title="Questions")
#    fig.update_traces(marker=dict(size=12,
#                                line=dict(width=2,
#                                            color='DarkSlateGrey')),
#                                            selector=dict(mode='markers'))#

#    # Display the bar chart in Streamlit
#    st.plotly_chart(fig)#

#    fig2 = go.Figure(go.Indicator(
#        mode = "number+gauge+delta",
#        gauge = {'shape': "bullet"},
#        delta = {'reference': 4.3},
#        domain = {'x': [0.1, 1], 'y': [0.2, 0.9]},
#        value = 5,
#        title = {'text': "Average score"}))#

#    st.plotly_chart(fig2)#

#    fig3 = go.Figure(go.Indicator(
#        mode="number+delta",
#        value=3,
#        number={'suffix': "", 'prefix': "Your score: ", 'font': {'size': 52}},
#        delta={'position': "bottom", 'reference': 4},
#        title={'text': " average score for question"}))#

#    # Update layout
#    fig3.update_layout(paper_bgcolor="lightgray",)
#    st.plotly_chart(fig3)
#
#
def show_initial_text():
    if not start_button_clicked:
        st.subheader("Introducing the Psychopathy, Narcissism, Machiavellianism Assessment: Discover Your Personality Score!")
        links = "[Machiavellianism](https://en.wikipedia.org/wiki/Machiavellianism_(psychology))&nbsp;&nbsp;[Narcissism](https://en.wikipedia.org/wiki/Narcissism) &nbsp; &nbsp;[Psychopathy](https://en.wikipedia.org/wiki/Psychopathy)"
        st.markdown(f"""
            - Uncover intriguing insights about your personality with just a few clicks!
            - Not sure what they are? &nbsp; {links}
        """)

        st.markdown("""
            Our interactive web interface offers a quick and engaging way to assess your Machiavellian tendencies. No lengthy explanations or excessive reading required!
            Simply answer 28 questions by selecting a score from 1 to 5. It's as easy as giving your honest opinion.
        """)

        st.markdown("1 - Strongly Disagree &nbsp;&nbsp; 2 - Disagree &nbsp;&nbsp;  3 - Neutral &nbsp;&nbsp;  4 - Agree &nbsp;&nbsp;  5 - Strongly Agree")

        st.markdown("Trust your instincts for the most accurate results.")
        st.markdown("Once you've finished answering all the questions, we'll generate your personalized Machiavellianism/Psychopathy/Narcissism score and compare it to the average score of other 2 traits.")
        st.markdown("Curious to see where you stand?")
        st.markdown("But wait, there's more! We'll also provide you with a predicted Machiavellianism/Psychopathy/Narcissism score based on your responses. Unleash your inner strategist and uncover the hidden aspects of your personality.")
        st.markdown("Ready to dive in? Begin the assessment now and unlock a fascinating glimpse into your Machiavellianism/Psychopathy/Narcissism score. Let's get started!")

        st.write(
            "<style>div.stButton > button {display: block; margin: 0 auto;}</style>",
            unsafe_allow_html=True
        )
    return True
#
# show_initial_text()
# show_q_a(i)
#show_plots()
#st.write('answers', answers)


st.title("Dark Triad App")

# Sidebar navigation or menu selection
page = st.sidebar.selectbox("Select Page", ("Info", "Front", "Test", "Result"))

# Display the selected page
if page == "Info":
    info_page()
elif page == "Front":
    front_page()
elif page == "Test":
    test_page()
elif page == "Result":
    result_page()
