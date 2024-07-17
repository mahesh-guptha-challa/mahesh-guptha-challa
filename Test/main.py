from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    return {"Name": "Mahesh", "id": 12}


if __name__ == '__main__':
    app.run(debug=True)



