---
# FandomX — The Fandom Explorer

---

## ✨ Overview

**FandomX** is a Flask-powered web application that allows users to explore characters from the Harry Potter universe using a live REST API.

Built with a focus on **clean architecture, UI/UX excellence, and real-world API integration**, this project transforms raw data into a visually engaging and interactive experience.

---

## 🎯 Features

### 🔍 Dynamic Search & Filtering
- Search characters by name (case-insensitive)
- Filter by Hogwarts house
- Combine filters seamlessly

### 🔄 Smart Sorting
- Sort characters A–Z or Z–A

### 📄 Pagination
- Efficient data slicing for performance
- Smart pagination navigation (First, Previous, Next, Last)

### 🧠 API Integration
- Live data from external REST API  
- Handles API errors gracefully  
- Cached API calls using `lru_cache` for better performance  

### 🎨 Premium UI/UX
- Cinematic dark theme with gold accents  
- Smooth hover animations and transitions  
- Glassmorphism-inspired panels  
- Responsive card-based layout  

### 🧾 Character Detail View
- Interactive detail panel (drawer/modal depending on version)  
- Displays:
  - Full name  
  - Actor  
  - House  
  - Birthdate  
  - Nickname  
  - Children  

### ⚡ Loading Experience
- Initial page loader  
- Loading overlay during navigation  
- Smooth transitions for a polished feel  

### 📱 Fully Responsive
- Optimized for desktop, tablet, and mobile  

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML5, CSS3, Bootstrap 5  
- **Templating:** Jinja2  
- **API:** https://potterapi-fedeperin.vercel.app/en/characters  
- **Libraries:**
  - `requests`
  - `functools.lru_cache`

---
## 🌐 Live Demo

[🚀 View Live App](https://fandom-x-chi.vercel.app/)


## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/FandomX.git
cd FandomX

2. Create a virtual environment

python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

3. Install dependencies

pip install flask requests

4. Run the application

python app.py

5. Open in your browser

http://127.0.0.1:5000
---

📊 How It Works

1. Fetches character data from the API


2. Caches the data to reduce repeated API calls


3. Applies filtering, sorting, and pagination


4. Renders results dynamically using Jinja templates

---

🚀 Future Improvements

⭐ Favorites system (local storage or database)

🔐 User authentication

🎭 Multi-fandom support (Marvel, Anime, etc.)

⚡ Infinite scrolling

🌐 Deployment (Vercel / Render / Railway)

---

🧠 Key Learnings

Real-world API integration and error handling

Flask routing and templating

Data filtering and transformation in Python

UI/UX design with Bootstrap and custom CSS

Performance optimization with caching


---

🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

📜 License

This project is open-source and available under the MIT License.

---

👤 Author

Nathaniel Katugwa
Computer Science Student | Entrepreneur | Builder

---

💡 Inspiration

Built as part of the 100 Days of Code (Python) journey — evolving from simple scripts to full-stack applications.

---
