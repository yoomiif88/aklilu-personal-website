# Aklilu Tesfaye Personal Portfolio

A modern personal portfolio website built with Python and Flask.

## Requirements
- Python 3.10 or newer
- pip

## Run on Windows

Open Command Prompt or PowerShell inside this folder:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open the local address shown in the terminal, normally:
http://127.0.0.1:5000

## Run on macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Customize
- Replace `static/images/profile.jpg` with a different profile photo if needed.
- Edit `templates/index.html` to change your content.
- Edit `static/css/style.css` to change the design.
- Change `app.secret_key` before deploying publicly.

The contact form currently gives a confirmation message. It does not send email or save messages to a database yet.
