import pandas as pd
import numpy as np
import streamlit as st
import sys, os, time
from flask import Flask
from flask import request
from flask import render_template

def main(): 
    challenge       = request.args.get('hub.challenge',    default = '*', type = str)
    verify_token    = request.args.get('hub.verify_token', default = '',  type = str)
    if challenge != '*' and verify_token == 'aqui vai o token que tu configura no Workplace':
        print(challenge)

    data = request.data.decode('utf-8')
    st.write(data)

if __name__ == '__main__':
    main()