# 🛒 AI Marketplace Backend & Recommendation System

An end-to-end Backend Engineering project building a scalable marketplace API using FastAPI, PostgreSQL, authentication, and an AI recommendation system.

This project demonstrates a full backend workflow:

API Design → Database Integration → Authentication → AI Recommendation → Analytics

---

## 🌐 API Documentation

Interactive API documentation available via Swagger:

👉 http://127.0.0.1:8000/docs

---

## 🎯 Project Objective

Build a backend system for a marketplace platform where users can:

• Register and securely authenticate  
• Create and manage item listings  
• Search marketplace items  
• Receive AI-based item recommendations  
• Analyse marketplace insights using analytics endpoints  

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Backend Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Authentication | JWT Tokens |
| Security | Bcrypt Password Hashing |
| Machine Learning | Scikit-learn |
| Infrastructure | Docker |
| Documentation | Swagger / OpenAPI |
| Version Control | Git & GitHub |

---

## 🔄 Project Workflow

### 1️⃣ User Authentication System

Users can securely register and log in.

Validation rules:

• Username must be **6–12 characters**  
• Password must contain **uppercase, lowercase, number, and special character**  
• Email validation included  

Endpoints:

• POST /users/register  
• POST /users/login  

JWT tokens are generated after login for secure API access.

---

### 2️⃣ Marketplace Item Listing

Users can create and manage marketplace listings.

Item attributes include:

• Title  
• Price  
• Category  
• Description  
• Seller ID  

Endpoints:

• POST /items/create  
• GET /items  
• GET /items/{item_id}  
• DELETE /items/{item_id}

---

### 3️⃣ Item Search System

Marketplace search functionality allows users to quickly find items.

Features:

• Keyword search  
• Category filtering  

Endpoint:

• GET /items/search?q=keyword

Example:

• /items/search?q=iphone

---

### 4️⃣ AI Recommendation Engine

The backend includes a simple AI recommendation system that suggests similar items.

Machine Learning approach:

• TF-IDF text vectorisation  
• Cosine similarity comparison  

Endpoint:

• GET /recommendations/{item_id}

The API returns items that are most similar based on item description and category.

---

### 5️⃣ Marketplace Analytics

Analytics endpoints provide insights about marketplace activity.

Endpoints:

• GET /analytics/popular-items  
• GET /analytics/top-categories  
• GET /analytics/price-distribution  

These endpoints help analyse:

• Most popular listings  
• Category trends  
• Price distribution across the marketplace

---

## ▶️ Run Locally

Clone repository:

git clone https://github.com/YOUR_USERNAME/smart-marketplace-engine.git

Navigate into project:

cd smart-marketplace-engine

Install dependencies:

pip install -r requirements.txt

Start PostgreSQL container:

docker compose up -d

Run API server:

uvicorn app.main:app --reload

Open API documentation:

http://127.0.0.1:8000/docs

---

## 📂 Project Structure

smart-marketplace-engine/

app/  
 ├── api/  
 │   ├── users.py  
 │   ├── items.py  
 │   └── analytics.py  

 ├── ai/  
 │   └── recommender.py  

 ├── database/  
 │   └── db.py  

 ├── models/  
 │   ├── user.py  
 │   └── item.py  

 ├── schemas/  
 │   ├── user_schema.py  
 │   └── item_schema.py  

 ├── utils/  
 │   ├── auth.py  
 │   └── jwt_handler.py  

 └── main.py  

scripts/  
 └── seed_data.py  

Dockerfile  
docker-compose.yml  
requirements.txt  
README.md  

---

## 📊 Key Features

• Secure authentication using JWT  
• Marketplace item listing system  
• Search functionality  
• AI recommendation engine  
• Marketplace analytics APIs  
• PostgreSQL database integration  
• Docker container deployment  

---

## 🚀 Future Improvements

• Advanced ranking algorithm for item search  
• Redis caching for faster API responses  
• Real-time recommendation updates  
• Frontend marketplace interface  
• Cloud deployment (AWS / Render / GCP)

---

## 👤 Author

Prem Nadh Gajula  
Aspiring Data Scientist / ML Engineer / Backend Developer

Interested in:

• AI systems  
• backend architecture  
• machine learning applications  

If you like this project, please ⭐ the repository!