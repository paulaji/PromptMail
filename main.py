from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "add here"

@app.route("/", methods=["GET", "POST"])
def index():
    generated_email = ""

    if request.method == "POST":
        from_text = request.form["from"]
        to_text = request.form["to"]
        subject_text = request.form["subject"]
        date_text = request.form["date"]
        content_idea = request.form["content"]

        prompt = f"From: {from_text}\nTo: {to_text}\nSubject: {subject_text}\nDate: {date_text}\nContent: {content_idea}\nGenerate email:"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )

        generated_email = response.choices[0].text.strip()

    return render_template("index.html", generated_email=generated_email)

if __name__ == "__main__":
    app.run(debug=True)
