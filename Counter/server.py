from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "password1234"

app = Flask(__name__)
app.secret_key = 'dskhgdlhgfkdjghjka'


@app.route('/')
def home():
    session['count'] = session.get('count', 0) + 1
    return render_template('home.html', count=session['count'])


@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('home')) 


# At the very end don't forget to place the "run" command
if __name__ == "__main__":
    app.run(debug = True, port=5001 )
