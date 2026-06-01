# Job Tracker

Job Tracker is a Django web application for tracking job applications. Users can log in, add jobs, update application status, and view a dashboard with total applications, applied jobs, interviews, and offers.

## Features

- User login and logout
- Protected dashboard for logged-in users
- Add, edit, and delete job applications
- Track company, role, status, and applied date
- Dashboard summary cards
- Django admin panel
- Render-ready deployment setup

## Tech Stack

- Python 3.10
- Django 5.2.11
- SQLite for local development
- PostgreSQL support for Render deployment
- Gunicorn for production server
- Bootstrap and Bootstrap Icons for UI

## Project Creation Commands

These are the main commands used to create and run the project locally.

```powershell
cd C:\Users\Lenovo\Desktop\django_projects
python -m venv venv
.\venv\Scripts\activate
pip install django
django-admin startproject jobtracker
cd jobtracker
python manage.py startapp jobs
```

After creating the app, `jobs` was added to `INSTALLED_APPS` in `jobtracker/settings.py`.

## Database Commands

```powershell
python manage.py makemigrations
python manage.py migrate
```

## Create Admin User

```powershell
python manage.py createsuperuser
```

## Run Locally

```powershell
cd C:\Users\Lenovo\Desktop\django_projects\jobtracker
..\venv\Scripts\activate
python manage.py runserver
```

Open the app:

```text
http://127.0.0.1:8000/
```

Open Django admin:

```text
http://127.0.0.1:8000/admin/
```

## Important App URLs

```text
/login/       Login page
/logout/      Logout
/             Job dashboard
/jobs/        Job dashboard alias
/add/         Add job
/edit/<id>/   Edit job
/delete/<id>/ Delete job
/admin/       Django admin
```

## Install Dependencies

The project dependencies are stored in `requirements.txt`.

```powershell
pip install -r requirements.txt
```

## Check Project

```powershell
python manage.py check
```

## Collect Static Files

For production hosting:

```powershell
python manage.py collectstatic --noinput
```

## GitHub Push Commands

The project was pushed to GitHub using:

```powershell
git status
git add .
git commit -m "Update job tracker"
git push origin main
```

Local-only files are ignored using `.gitignore`, including:

```text
db.sqlite3
__pycache__/
venv/
.env
staticfiles/
```

## Render Hosting

The project was hosted live using Render as a web service connected to the GitHub repository.

### Render Build Command

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

### Render Start Command

The project uses this `Procfile` command:

```bash
python manage.py migrate && gunicorn jobtracker.wsgi:application
```

This runs database migrations first, then starts the Django app using Gunicorn.

## Render Environment Variables

Set these variables in the Render dashboard:

```text
DEBUG=False
SECRET_KEY=your-secure-secret-key
CSRF_TRUSTED_ORIGINS=https://your-app-name.onrender.com
DATABASE_URL=your-render-postgresql-database-url
```

`DATABASE_URL` is provided automatically if a Render PostgreSQL database is connected to the web service.

## Live Database and Login

The local `db.sqlite3` file is not pushed to GitHub. That means local users do not automatically exist on Render.

After deployment, create a live admin user on Render:

```bash
python manage.py createsuperuser
```

Use that Render-created username and password to log in on the live site and admin panel.

## Updating the Live Site

After making changes locally:

```powershell
git status
git add .
git commit -m "Describe your changes"
git push origin main
```

Render will auto-deploy the latest GitHub commit if auto-deploy is enabled. If it does not start automatically, use:

```text
Render Dashboard -> Your Web Service -> Manual Deploy -> Deploy latest commit
```

## Useful Commands

```powershell
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py changepassword username
python manage.py check
python manage.py collectstatic --noinput
```
