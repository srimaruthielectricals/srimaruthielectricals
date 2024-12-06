from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Render the home page, where body_template is passed dynamically
    return render_template('home.html', body_template='home_body.html')
    
@app.route('/learnmore')
def learnmore():
    return render_template('learnmore.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/carrers')
def carrers():
    return render_template('carrers.html')

if __name__ == '__main__':
    app.run(debug=True)
