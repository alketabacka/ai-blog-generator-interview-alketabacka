from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import os

# Mock modules - replace with your real ones
from seo_fetcher import get_keyword_metrics
from ai_generator import generate_blog_post

app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start()

KEYWORD = "wireless earbuds"

def generate_content_and_save(keyword):
    # Absolutely no use of Flask request here!
    metrics = get_keyword_metrics(keyword)
    content = generate_blog_post(keyword, metrics)

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')
    filename = f"outputs/{timestamp}_{keyword.replace(' ', '_')}.md"
    os.makedirs("outputs", exist_ok=True)
    with open(filename, "w") as f:
        f.write(content)

    print(f"[{timestamp}] Blog post generated: {filename}")
    return {
        "keyword": keyword,
        "metrics": metrics,
        "status": "generated",
        "output_file": filename
    }

@app.route("/generate")
def generate():
    keyword = request.args.get("keyword", KEYWORD)
    result = generate_content_and_save(keyword)
    return jsonify(result)

@scheduler.scheduled_job('cron', minute='*/1')  # Every 1 minute
def scheduled_generate():
    keyword = KEYWORD  # Use default or hardcoded keyword
    generate_content_and_save(keyword)  # ✅ Pure Python function, safe to call here


if __name__ == "__main__":
    app.run(debug=True)
