from flask import Flask, render_template
app = Flask (__name__)
@app.route("/")
def hello_world():
    return render_template("main.html")
@app.route("/yo")
def yo():
    return render_template("main2.html")
@app.route("/button")
def button():
    return render_template("main3.html")
@app.route("/dance")
def dance():
    return render_template("main4.html")
if __name__ == "__main__":
    app.run(debug = True) 
    