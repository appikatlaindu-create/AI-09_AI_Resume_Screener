from flask import Flask, request, render_template_string
import os
import re

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI-Powered Resume Screener</title>
    <style>
        body {
            font-family: Arial;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
        }

        h1 {
            text-align: center;
        }

        .box {
            border: 1px solid #ddd;
            padding: 25px;
            border-radius: 10px;
            margin-top: 20px;
        }

        button {
            padding: 10px 20px;
            cursor: pointer;
        }

        .result {
            margin-top: 25px;
            padding: 20px;
            background: #f4f4f4;
            border-radius: 10px;
        }
    </style>
</head>

<body>

<h1>AI-Powered Resume Screener</h1>

<div class="box">

<h2>Upload Resume</h2>

<form method="POST" enctype="multipart/form-data">

<input type="file" name="resume" accept=".pdf,.txt" required>

<br><br>

<label><b>Job Skills Required:</b></label>
<br><br>

<input type="text"
       name="job_skills"
       placeholder="python, java, sql, machine learning"
       style="width:80%; padding:10px;"
       required>

<br><br>

<button type="submit">Screen Resume</button>

</form>

{% if result %}

<div class="result">

<h2>Screening Result</h2>

<p><b>Resume:</b> {{ filename }}</p>

<p><b>Match Score:</b> {{ score }}%</p>

<p><b>Matched Skills:</b> {{ matched }}</p>

<p><b>Missing Skills:</b> {{ missing }}</p>

</div>

{% endif %}

</div>

</body>
</html>
"""


def extract_text(file_path):

    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read().lower()

    return ""


@app.route("/", methods=["GET", "POST"])
def home():

    result = False
    filename = ""
    score = 0
    matched = []
    missing = []

    if request.method == "POST":

        file = request.files.get("resume")
        job_skills = request.form.get("job_skills", "")

        if file and file.filename:

            filename = file.filename

            safe_name = re.sub(r"[^a-zA-Z0-9._-]", "_", filename)

            file_path = os.path.join(UPLOAD_FOLDER, safe_name)

            file.save(file_path)

            resume_text = extract_text(file_path)

            required_skills = [
                skill.strip().lower()
                for skill in job_skills.split(",")
                if skill.strip()
            ]

            for skill in required_skills:

                if skill in resume_text:
                    matched.append(skill)
                else:
                    missing.append(skill)

            if required_skills:
                score = round(
                    (len(matched) / len(required_skills)) * 100
                )

            result = True

    return render_template_string(
        HTML,
        result=result,
        filename=filename,
        score=score,
        matched=", ".join(matched) if matched else "None",
        missing=", ".join(missing) if missing else "None"
    )


if __name__ == "__main__":
    app.run(debug=True)