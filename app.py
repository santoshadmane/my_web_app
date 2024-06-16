from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Home Page</h1><a href='/page2'>Go to Page 2</a>"

@app.route('/page2')
def page2():
    return "<h1>This is Page 2</h1><a href='/'>Go back to Home Page</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
