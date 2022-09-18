from flask import Flask, render_template
import os

app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route('/', methods=['GET', 'POST'])
def home():
    hotdog_logo = os.path.join(app.config['UPLOAD_FOLDER'], 'hotdogshere.png')
    return render_template('index.html', user_image=hotdog_logo)

if __name__ == '__main__':
    app.run(debug=True)

