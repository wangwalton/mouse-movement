cd "C:\Users\Alias\Desktop\Hackathon"

# Create and start/enter python 3 venv
py -3 --version
py -3 -m venv venv
.\venv\Scripts\Activate.ps1

# Run app
$env:FLASK_APP = "WebApp.py"
flask run

#shutdown/exit python3 venv
deactivate