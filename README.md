# Biometric-Access-Control-System
An access control system built with Django. It makes use of fingerprints to grant/deny access

## Setup

STEP 1: Clone the repository:

```sh
$ git clone https://github.com/IfeOlulesi/ToDo-App-Django.git
$ cd ToDo-App-Django
```

STEP 2: (Optional but Recommended) Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

STEP 3: Install the dependencies:

```sh
$ pip install -r requirements.txt
```
If you followed STEP 2, you should see an `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

STEP 4: Once `pip` has finished downloading the dependencies, run the following in your terminal:

```sh
$ cd TaskHelp
$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/todo/`.

To play around with the API, run
```
(env)$ python manage.py shell
```
