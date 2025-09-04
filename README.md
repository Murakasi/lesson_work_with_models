# lesson_work_with_models
## README

### 1. Project Description

This repository contains a basic configuration of a Django project `base_cource_django`, created with `django-admin startproject`.
The project is built with Django 5.2.6, configured to use PostgreSQL, and environment variables are managed with `python-decouple`.

---

### 2. Requirements

Dependencies are listed in `requirements.txt`:

```
asgiref==3.9.1
Django==5.2.6
psycopg==3.2.9
python-decouple==3.8
sqlparse==0.5.3
tzdata==2025.2
```

---

### 3. Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/Murakasi/lesson_work_with_models.git
   cd base_cource_django
   ```

2. **Create and activate a virtual environment**
   Using `venv`:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   This project uses `python-decouple`.
   Create a `.env` file in the project root with the following variables:

   ```env
   DB_SECRET_KEY=your-django-secret-key
   DB_DEBUG=True           # or False in production
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

---

### 4. Settings Overview (`settings.py`)

* **Environment variables**
  `SECRET_KEY`, `DEBUG`, and database credentials are loaded with `config(...)` from `.env`.

* **Allowed hosts**
  Default: `ALLOWED_HOSTS = ["localhost", "127.0.0.1"]`.

* **Installed apps & middleware**
  Includes Django’s default apps (`admin`, `auth`, etc.) and middleware such as `SecurityMiddleware`, `SessionMiddleware`, and CSRF protection.

* **Paths**

  * `BASE_DIR`: project root.
  * Templates: stored in `templates/`.
  * Static files: in `static/` (collected into `staticfiles/`).

* **Database**
  Configured for PostgreSQL with credentials from `.env`.

* **Localization**

  * `LANGUAGE_CODE = 'en-us'`
  * `TIME_ZONE = 'Europe/Berlin'`
  * `USE_I18N = True` and `USE_TZ = True`

* **Authentication**
  Default password validators are enabled.

* **Default primary key**
  `DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'`.

---

### 5. Running the Project

1. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

2. **Create a superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

3. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your browser.

---

### 6. Production Deployment Tips

* Set `DEBUG = False`.
* Update `ALLOWED_HOSTS` with your domain(s).
* Use a strong, unique `SECRET_KEY`.
* Serve static files properly (`collectstatic` + WhiteNoise/CDN).
* Enable HTTPS and security settings:

  * `SECURE_HSTS_SECONDS`
  * `SECURE_SSL_REDIRECT`
  * `CSRF_COOKIE_SECURE`
  * `SESSION_COOKIE_SECURE`
* Consider external logging and monitoring tools.

---

### 7. Project Structure

```
base_cource_django/
├── base_cource_django/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py (if present)
├── templates/
├── static/
├── staticfiles/      # populated by collectstatic
├── manage.py
├── requirements.txt
└── .env              # DO NOT commit this file!
```

---

### 8. Contact

If you have any questions or need help, feel free to reach out.

