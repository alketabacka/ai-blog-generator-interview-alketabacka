import openai
import os

# Make sure you have set your OpenAI API key in an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog_post(keyword, metrics):
    prompt = f"""
Write a detailed, engaging, SEO-friendly blog post about "{keyword}".

Make sure to:
- Use the keyword naturally throughout the article
- Mention the search volume: {metrics['search_volume']}
- Mention the keyword difficulty: {metrics['keyword_difficulty']}
- Mention the average CPC: ${metrics['avg_cpc']}
- Include a short list with 3 placeholder affiliate links at the end

Use markdown format for headings and structure.

Begin the blog post below:
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful SEO blog writer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
    )

    blog_post = response['choices'][0]['message']['content']
    return blog_post
