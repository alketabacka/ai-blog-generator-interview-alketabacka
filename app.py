from flask import Flask, request, jsonify
from seo_fetcher import get_keyword_metrics
from ai_generator import generate_blog_post
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import os

app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start()

KEYWORD = "AI"

from flask import Response

@app.route("/generate")
def generate():
    keyword = request.args.get("keyword", KEYWORD)
    metrics = get_keyword_metrics(keyword)
    content = generate_blog_post(keyword, metrics)

    # Save to file
    filename = f"outputs/{datetime.date.today()}_{keyword.replace(' ', '_')}.md"
    os.makedirs("outputs", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    # Return the content as plain text
    return Response(content, mimetype="text/plain")



# Daily job
@scheduler.scheduled_job('cron', hour=6)  # Run daily at 6 AM
def scheduled_generate():
    with app.app_context():
        generate()

if __name__ == "__main__":
    app.run(debug=True)
