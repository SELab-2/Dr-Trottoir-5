# Dr-trottoir django backend

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone git@github.com:SELab-2/Dr-Trottoir-5.git
$ cd Dr-Trottoir-5
$ cd backend
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:

### Database setup

Download and install postgresql from [here](https://www.postgresql.org/download/).
Make an empty database and a user for this project.

In the backend directory. Copy the env file and fill in you own values. 
The location of .env should be in the same location of settings.py:
```sh
(env)$ cp .env.example .env
```

### Run the backend
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.


## Tests

Todo setup tests and testing environment
