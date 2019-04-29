from flask import Flask, render_template, url_for, request
from flask import jsonify
from resources import Analysis


#import re 
#import tweepy 
#from tweepy import OAuthHandler 
#from textblob import TextBlob

app = Flask(__name__)





@app.route('/')
def search():
    return render_template('dynamic_input.html')

@app.route('/results', methods = ['GET', 'POST'])
def results():
    if request.method == 'GET':
        return redirect(url_for('search'))
    else:
        input_values = request.form.getlist('input_text[]')
        text = input_values[0]
        for i in input_values[1:]:
            text = text+'+'+ i
        print(text)  

        analysis = Analysis.Analysis(text)  
        analysis.run()
        print(analysis.sentiment)
        print(analysis.subjectivity)

        checkbox_values = request.form.getlist('input_checkbox')
        return render_template('dynamic_input_results.html',
                               input_values = input_values,
                               analysis = analysis,
                               checkbox_values = checkbox_values)

if __name__ == '__main__':
    app.run(debug = True)