from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/single')
def single():
    return render_template('/single.html')

@app.route('/categories')
def categories():
    return render_template('/categories.html')

@app.route('/contact')
def contact():
    return render_template('/contact.html')









if __name__ == '__main__':
    app.run(debug=True)
