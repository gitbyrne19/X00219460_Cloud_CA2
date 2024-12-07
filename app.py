import os
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Home route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        return jsonify({"success": True, "name": name, "message": message})
    return render_template("index.html")

# Health check route
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "Healthy"}), 200

if __name__ == "__main__":
    # Get the PORT from the environment variable or default to 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)