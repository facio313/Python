from flask import Flask
from flask.templating import render_template
    
app = Flask(__name__)

@app.route('/')
@app.route('/three')
def three():
    return render_template('three.html')

if __name__ == '__main__':
    app.run()