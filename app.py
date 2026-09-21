import os
from flask import Flask, render_template, request, flash
import resend

app = Flask(__name__)
app.secret_key = "change-this-secret-key"

# Load the Resend API key from environment variables
resend.api_key = os.environ.get("RESEND_API_KEY")

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
        try:
            # Send email via Resend
            resend.Emails.send({
                "from": "portfolio-website@resend.dev",   # safe default sender
                "to": "yourgmail@example.com",            # replace with your Gmail
                "subject": f"New message from {name}",
                "html": f"""
                    <p><strong>Name:</strong> {name}</p>
                    <p><strong>Email:</strong> {email}</p>
                    <p><strong>Message:</strong> {message}</p>
                """
            })
            flash("✅ Thank you! Your message has been sent.", "success")
        except Exception as e:
            flash(f"❌ Error sending message: {str(e)}", "error")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
