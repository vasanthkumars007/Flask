from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    courses = ["Python","Java","C++","C#"]
    is_logged_in = True
    return render_template('index.html',courses=courses)

@app.route('/about')
def about():
    return '<h3>About Us</h3><p>This is a simple example of learning flask</p>'

@app.route('/contact')
def contact():
    return '<h3>Contact us </h3><p>you can contact us at'

#dynamic routing 

@app.route('/users/<name>')
def user(name):
    fruits = ["apple","banana","mango","orange"]
    profile = {
        "name":name,
        "email":"{}@example.com".format(name)}
    return render_template("users.html" , user_name=name , fruits=fruits , profile = profile)


if __name__=='__main__':
    app.run(debug=True)