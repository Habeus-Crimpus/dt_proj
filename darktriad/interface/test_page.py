import streamlit as st
from darktriad.interface.result_page import result_page


#current_page = st.session_state.get("current_page","test_page")
start_button_clicked = False

if 'counter' not in st.session_state.keys():
   st.session_state.counter = 0
i = st.session_state.counter

if 'answers' not in st.session_state.keys():
   st.session_state.answers = []
global answers
answers = st.session_state.answers
#
questions = ["It's not wise to tell your secrets.",
            "I like to use clever manipulation to get my way.",
            "Whatever it takes, you must get the important people on your side. ",
            "Avoid direct conflict with others because they may be useful in the future.",
            "It’s wise to keep track of information that you can use against people later.",
            "You should wait for the right time to get back at people. ",
            "There are things you should hide from other people because they don’t need to know.",
            "Make sure your plans benefit you, not others.",
            "Most people can be manipulated.",
            "People see me as a natural leader. ",
            "I hate being the center of attention.",
            "Many group activities tend to be dull without me.",
            "I know that I am special because everyone keeps telling me so. ",
            "I like to get acquainted with important people. ",
            "I feel embarrassed if someone compliments me.",
            "I have been compared to famous people. ",
            "I am an average person.",
            "I insist on getting the respect I deserve.",
            "I like to get revenge on authorities.",
            "I avoid dangerous situations.",
            "Payback needs to be quick and nasty. ",
            "People often say I’m out of control. ",
            "It’s true that I can be mean to others. ",
            "People who mess with me always regret it.",
            "I have never gotten into trouble with the law.",
            "I enjoy having sex with people I hardly know.",
            "I’ll say anything to get what I want.",
            "Are you a US citizen?"]
#
def update(select):
   answers.append(int(select))
   global i
   i += 1
   st.session_state.answers = answers
   st.session_state.counter = i

global preds

def placement(x:int):
   if x == -1:
       st.write('You placed below the expected score')
   elif x == 0:
       st.write('You are within the expected range')
   else:
       st.write('You are above the expected score')

def show_q_a(i):
   select = st.selectbox(
       f"{i+1})  {questions[i]}",
       ('Select a number', '1', '2', '3', '4', '5')
   )
   if select != 'Select a number':
       st.write('You selected:', select)
       if (i < 27):
           name = 'Continue'
           st.button(name, on_click=update, args=select,key='a43')
       else:
           name = 'Submit'
           #st.button(name, on_click=, args=select,key='a43')
           if st.button("Submit"):
               page = "Result"
               result_page()
            #    global page
            #    page = "Result"
            #    st.session_state.page = "Result"
               
def test_page():
    st.header("Bla bla")
    show_q_a(i)
    
