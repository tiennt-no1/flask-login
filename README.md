# Flask Login

Flask app to manage user login and registration.
  
Setup:
```
pip install vitualenv # if not already installed
git clone https://github.com/tiennt-no1/flask-login.git
cd flask-login
python -m virtualenv venv -p python3
source venv/bin/activate | .\venv\Scripts\activate.bat # depend os linux or windows
pip install -r requirements.txt # sometime need run as admin on windows
python3 app.py
```

Then open ```http://localhost:5000/``` in a web-browser.
------------------------
```
use pytest to run the tests
pytest --cov ./ --cov-report=html
pytest -n 3
```