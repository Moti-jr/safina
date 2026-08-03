# Safina Initiative — Django Website

A complete, modern Django website for the Safina Initiative nonprofit
organisation. Built with Django 5.1, Bootstrap 5.3, HTMX, and Alpine.js.

---

## Quick Start

```bash
# Clone the project
git clone <your-repo-url>
cd safina

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Start server
python manage.py runserver
```

Visit http://127.0.0.1:8000

Admin panel: http://127.0.0.1:8000/admin

---

## Project Structure
