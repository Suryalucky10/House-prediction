import pandas as pd
from flask import Flask, render_template, request
import pickle 
import numpy as np
app=Flask(__name__)
with open('trained_mod.pkl','rb') as f:
    rfg.pickle.load(f);
