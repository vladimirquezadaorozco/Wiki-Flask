from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods = ["POST"])
def search():
    search_query = request.form.get("search_query")
    print("Search query recibido:", search_query)
    return jsonify({"search_query": search_query})


if __name__ == "__main__":
    app.run(debug=True)