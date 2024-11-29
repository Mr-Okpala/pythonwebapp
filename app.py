from flask import Flask, render_template

app = Flask(__name__)

#Route for the homepage
@app.route('/')
def home():
    return render_template('home.html')

# Route for About page
@app.route('/about')
def about():
    return render_template('about.html')

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=5000)