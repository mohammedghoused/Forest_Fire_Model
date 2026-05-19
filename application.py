from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
import sklearn.preprocessing import StandardScaler

application = Flask(__name__)