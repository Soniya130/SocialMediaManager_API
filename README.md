# Social Media Manager API

A Django REST Framework–based backend project for managing social media posts. This project allows you to **create, read, update, delete (CRUD)** posts, view **basic analytics**, and **fetch sample posts from an external API**. It is suitable for learning Django REST APIs and can be extended with a frontend or authentication.

---

## 📁 Project Structure

```
SocialMediaManager/
│── social_posts/           # Django app for posts
│   │── migrations/
│   │── admin.py            # Admin panel registration
│   │── apps.py             # App configuration
│   │── models.py           # Post model
│   │── serializers.py      # DRF serializers
│   │── views.py            # API views (CRUD, analytics, external API)
│   │── tests.py
│
│── socialmanager/          # Project settings
│   │── settings.py
│   │── urls.py
│   │── asgi.py
│   │── wsgi.py
│
│── db.sqlite3              # SQLite database
│── manage.py               # Django entry point
│── venv/                   # Virtual environment
│── README.md               # Project documentation
```

---

## 🚀 Features

* ✅ CRUD operations for social media posts
* 📊 Analytics API (count posts by category)
* 🌐 External API integration (JSONPlaceholder sample posts)
* 🛠 Django Admin panel support
* 🔄 RESTful APIs using Django REST Framework

---

## 🧱 Tech Stack

* **Backend:** Django 5.x
* **API Framework:** Django REST Framework
* **Database:** SQLite3
* **Language:** Python 3.11+
* **External API:** JSONPlaceholder

---

## 📌 Post Model

Each post contains:

* `title` – Post title
* `content` – Post description/content
* `category` – Type of post (Marketing, Ads, Content, etc.)
* `created_at` – Auto-generated timestamp

---

## 🔗 API Endpoints

### 1️⃣ Posts CRUD

Base URL:

```
http://127.0.0.1:8000/api/posts/
```

| Method      | Endpoint           | Description       |
| ----------- | ------------------ | ----------------- |
| GET         | `/api/posts/`      | Get all posts     |
| POST        | `/api/posts/`      | Create a new post |
| GET         | `/api/posts/<id>/` | Get a single post |
| PUT / PATCH | `/api/posts/<id>/` | Update a post     |
| DELETE      | `/api/posts/<id>/` | Delete a post     |

**Sample POST JSON:**

```json
{
  "title": "LinkedIn Strategy",
  "content": "Share weekly data science tips on LinkedIn.",
  "category": "Content"
}
```

---

### 2️⃣ Analytics Report

```
GET /api/report/
```

Returns number of posts grouped by category.

Example response:

```json
[
  {"category": "Content", "total_posts": 3},
  {"category": "Marketing", "total_posts": 2}
]
```

---

### 3️⃣ External Posts API

```
GET /api/external-posts/
```

* Fetches sample posts from **JSONPlaceholder**
* Returns first 10 placeholder posts

---

## ⚙️ Setup Instructions

### 1️⃣ Clone / Open Project

```bash
cd SocialMediaManager
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install django djangorestframework requests
```

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6️⃣ Start Server

```bash
python manage.py runserver
```

Open:

* API: [http://127.0.0.1:8000/api/posts/](http://127.0.0.1:8000/api/posts/)
* Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🧪 Testing Using Python Requests

```python
import requests

r = requests.get("http://127.0.0.1:8000/api/posts/")
print(r.status_code)
print(r.json())
```

---

## 📚 Learning Outcomes

* Django project & app structure
* REST API development using DRF
* Model–Serializer–ViewSet workflow
* External API integration
* API testing using Python `requests`

---

## 🏁 Conclusion

This project demonstrates a complete **backend REST API** for managing social media posts. It is ideal for academic submission, resume projects, and as a base for adding authentication or a frontend.

---

👩‍💻 **Author:** Soniya Patil
