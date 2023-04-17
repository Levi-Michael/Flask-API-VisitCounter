from flask import *

app = Flask("Website visit counter", static_url_path="")
app.secret_key = "sadasw4566edf1er8grt1h9tyj1kuy65k4318fdsa9fa1s55d46ad1"


@app.route("/api/counter", methods=["GET"])
def counter():
    if session.get("visit"):
        session["visit"] += 1
    else:
        session["visit"] = 1

    return jsonify({"visit": session["visit"]})


debug = True
app.run(host='0.0.0.0', port=4455, debug=debug)
