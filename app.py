from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "change-this-secret-key"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please complete all contact fields.", "error")
    else:
        # For now, we display a confirmation.
        # Later, this can be connected to email or a database.
        flash("Thank you! Your message has been received.", "success")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="10.11.241.198", port=5000, debug=True)
