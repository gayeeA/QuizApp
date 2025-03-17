# Let's Quiz

![alt text](image.png)

## Current Features

### Site access features:

- User must be logged in to access the Quiz.
- For signup user is required to give _username_, _first name_, _last name_, _e-mail address_ and _password_.
- For login the user will be required to enter _username_ and _password_ only.

### Features of the quiz:

- All questions are multiple choice question.
- Each question is displayed only once per user.
- Questions are displayed randomly for every user.
- If the user by-mistake presses refresh or go back to the previous page, there will be a new question for the user and the
  question he/she was on will be marked as attempted.
- A message will be displayed after every attempted question whether the answer was correct or incorrect.

### Leaderboard features:

- Leaderboard is a shorted list according to the score obtained by the users.
- If two users are having same score, the user who has signed up earlier will have good ranking than the one who joined late.
- Leaderboard is open to all. No login required.

### Administrative features:

- Only admin can add questions.
- Admin can add questions and modify them until they are not marked as _Has been published?_
- Once a question has been published, it can neither be modified nor can be accessed. Admin can only see a list of questions.
- Admin can search questions by question text or choice text.
- Admin can filter questions based on whether the questions have been published or not.

## Getting started with development

Dependencies:

- Python 3.6.x
- Django 1.11.x
- Ubuntu 17.04 or later or Linux Mint 18.2 or later

### 1. Clone this repository

```bash
git clone https://github.com/akashgiricse/lets-quiz.git
cd lets_quiz
```

### 2. Install [Pipenv](https://pipenv.pypa.io/en/latest/)

#### ( or )

### Install pipenv:

Open your terminal and install pipenv using pip:

```bash
pip install pipenv
```

### 3. Create the virtualenv

```bash
## run following command from `lets_quiz` directory
pipenv shell
```

### 4. Install python packages

```bash
pip install -r requirements.txt
```

### 5. Install crispy-forms:

```bash
pip install crispy-forms
```

### 6. Install the django-model-utils package:

```bash
pip install django-model-utils
```

### 7. Setup the database

_TODO - Add instructions for this when I start using MySQL database._

### 8. Run database migrations

```bash
cd lets_quiz
python manage.py migrate
```

### 9. Create superuser

```bash
python manage.py createsuperuser
```

### 10. Run development server

```bash
python manage.py runserver
```

#### issues

if you are facing any issues in sign up add the user through the admin aftercreating the supeuser
