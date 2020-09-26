
from flask import Flask, render_template, request, Markup

import numpy as np
import matplotlib.pyplot as plt
import random
import pickle
import keras

app = Flask(__name__)

@app.route("/")
def get_sms_view():
	return render_template('sms_view.html', spam_message = '');


@app.route("/sms_prediction", methods=['POST'])
def get_sms_spam():
    sms_model_count = pickle.load(open('models_pre_trained/model_count_spam.pickle', "rb"))
    sms_model = pickle.load(open('models_pre_trained/model_spam.pickle', "rb"))

    result = sms_model.predict(sms_model_count.transform(np.array([request.form['text']])))
    
    if result[0] == 0:
        spam_message = 'Not a Spam Message'
        spam_flag = False
    elif result[0] == 1:
        spam_message = 'It is a Spam Message'
        spam_flag = True

    return render_template('sms_view.html', spam_message = spam_message, spam_flag = spam_flag);

if __name__ == '__main__':
   app.run(debug = True)