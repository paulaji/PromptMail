from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "OPEN_AI_API"

@app.route("/", methods=["GET", "POST"])
def index():
    generated_subject = generated_content = ""
    error_message = ""

    if request.method == "POST":
        subject_text = request.form["subject"]
        content_idea = request.form["content"]

        try:
            # Generate content prompt
            content_prompt = "Generate a proper email body content only- Content: " + content_idea
            content_response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=content_prompt,
                max_tokens=150  # Adjust the token limit as needed
            )
            generated_content = content_response.choices[0].text.strip()

            # Generate subject prompt
            subject_prompt = "Generate a proper formal email subject from: " + content_idea
            subject_response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=subject_prompt,
                max_tokens=50  # Adjust the token limit as needed
            )
            generated_subject = subject_response.choices[0].text.strip()

        except Exception as e:
            error_message = "An error occurred. Please refresh and try again."

    return render_template("index.html", generated_subject=generated_subject, generated_content=generated_content, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
