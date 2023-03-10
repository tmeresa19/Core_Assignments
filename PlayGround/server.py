from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_class():
    print("The server is listening!")
    return "Hi from root /"


@app.route("/play/<int:x>/<string:color>")
def play(x, color=None):
    return render_template("index.html", x=x, color=color)


# At the very end 
if __name__ == "__main__":
    app.run(debug=True, port=5001)
