from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/result3", methods=["POST"])
def result3():
    name = request.form.get("name")
    phone = request.form.get("phone")

    return render_template("result1.html", name=name, email=email)



if __name__ == '__main__':
    app.run(debug=True)
