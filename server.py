from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    search_query = request.form.get("search_query")
    print("Search query received:", search_query)
    return jsonify({"search_query": search_query})

@app.route("/css/<path:filename>")
def serve_css(filename):
    print("CSS Changed.")
    return send_from_directory("static", filename)
    

if __name__ == "__main__":
    app.run(debug=True)
