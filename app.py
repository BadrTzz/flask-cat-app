from flask import Flask, render_template, url_for
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
    
    gifs = [f for f in os.listdir('static') if f.endswith('.gif')]
  
    gif = random.choice(gifs)
   
    url = url_for('static', filename=gif)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
