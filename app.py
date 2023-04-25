from flask import *

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form.get("sector1"):
            print('financeiro')
        elif request.form.get("sector2"):
            print('administração')
        print(request.form["name"])
        print(request.form["email"])
        print(request.form["msg"])
    return render_template("index.html")

if __name__ == "__main__":
    app.run()