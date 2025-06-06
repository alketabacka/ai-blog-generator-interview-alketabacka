
# AI Blog Generator – Alketa Backa

This Flask-based application generates SEO-optimized blog posts using the OpenAI API. It runs both on-demand via HTTP requests and automatically on a daily schedule using APScheduler.

---

## 📦 Features

- Fetches SEO metrics for a given keyword (mocked)
- Uses OpenAI to generate a blog post
- Saves output as a Markdown file (`.md`)
- Automatically runs daily at a scheduled time (or every minute for testing)

---

## 🚀 Technologies Used

- Python 3.11+
- Flask
- OpenAI API
- APScheduler

---

## 📂 Project Structure


ai-blog-generator-interview-alketa/
│
├── app.py                 # Main Flask app with scheduler
├── seo\_fetcher.py         # Mock SEO metrics generator
├── ai\_generator.py        # Generates content using OpenAI
├── outputs/               # Folder where .md files are saved
├── requirements.txt
└── README.md



---

## 🔑 Setup & Run

1. **Clone the repo**

```bash
git clone https://github.com/your-username/ai-blog-generator-interview-alketa.git
cd ai-blog-generator-interview-alketa
````

2. **Create and activate virtual environment (optional)**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set your OpenAI API key**

Create a `.env` file:

```bash
OPENAI_API_KEY=your_api_key_here
```

Or export it in your terminal:

```bash
export OPENAI_API_KEY=your_api_key_here
```

5. **Run the app**

```bash
python3 app.py
```

---

## 🧪 Test the Blog Generator

To manually trigger blog generation:

Open browser or use curl:

```bash
http://localhost:5000/generate?keyword=wireless%20earbuds
```

Generated files will be saved in `outputs/` folder.

---

## 🕒 Scheduling

By default, the blog post is generated every minute for testing:

```python
@scheduler.scheduled_job('cron', minute='*/1')
```

You can change it to daily at 6 AM:

```python
@scheduler.scheduled_job('cron', hour=6)
```

---

## ✅ Sample Output

Markdown files will be saved like:

```
outputs/2025-06-05_wireless_earbuds.md
```

---

## 🧠 Author

**Alketa Backa**
📧 \abacka22@gmail.com
💼 \alketabacka

---

````

---

### ✅ `requirements.txt`

```txt
flask
openai
apscheduler
python-dotenv
````


