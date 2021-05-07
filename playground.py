from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)	# notice the 2 new named arguments!

@app.route('/play')
def play():
    print()
    return render_template("index3.html")


@app.route('/play/<int:amount>')
def playBoxes(amount):
    print(amount)
    return render_template("index4.html", amount=amount)

@app.route('/play/<int:amount>/<color>')
def changeBoxes(amount, color):
    print(amount, color)
    return render_template("index2.html", amount=amount, color=color)

if __name__=="__main__":
    app.run(debug=True)