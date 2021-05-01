# Biometric-Access-Control-System
An access control system built with Django. It makes use of fingerprints to grant/deny access

## Hardware Requirements
Secugen Hampster Pro Fingerprint scanner (recommended)

## Software Requirements
Secugen Web API. Here are the download links:
- For Windows 64 bit machines: https://webapi.secugen.com/download/SGI_BWAPI_Win_64bit.exe
- For Windows 32 bit machines: https://webapi.secugen.com/download/SGI_BWAPI_Win_32bit.exe

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
$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`

To play around with the API, run
```
(env)$ python manage.py shell
```
