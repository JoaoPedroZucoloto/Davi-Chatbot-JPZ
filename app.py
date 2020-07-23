from flask import Flask
from flask import request
from flask import render_template
import sys, os, time
import streamlit as st

st.title('Roi')

application = Flask(__name__)

@application.route('https://davi-chatbot-jpz.herokuapp.com/', methods=['GET', 'POST'])
def webhook():    
    challenge       = request.args.get('hub.challenge',    default = '*', type = str)
    verify_token    = request.args.get('hub.verify_token', default = '',  type = str)
    if challenge != '*' and verify_token == 'token-da-loucura':
        return challenge
       
    data = request.data.decode('utf-8')
        
    return 'Oi :)'