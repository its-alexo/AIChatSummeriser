import os
import openai
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def summarize_text(chat_text):
    prompt = f"Summarize the following chat:\n\n{chat_text}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )

    return response["choices"][0]["message"]["content"]

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None

    if request.method == "POST":
        chat_text = request.form["chat"]
        if chat_text:
            summary = summarize_text(chat_text)

    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
