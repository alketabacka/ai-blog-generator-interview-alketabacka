import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog_post(keyword, metrics):
    prompt = f"""Write a blog post about '{keyword}'.

    SEO Metrics:
    - Search Volume: {metrics['search_volume']}
    - Keyword Difficulty: {metrics['keyword_difficulty']}
    - Avg CPC: {metrics['avg_cpc']}

    Structure:
    - Use headings and paragraphs
    - Include at least 3 sections
    - Insert placeholder affiliate links like {{AFF_LINK_1}}, {{AFF_LINK_2}}, etc.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful blog writer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response['choices'][0]['message']['content']
