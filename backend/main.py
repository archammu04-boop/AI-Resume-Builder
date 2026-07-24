import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Resume Builder Backend!"
    }

@app.post("/generate")
def generate_resume(data: dict):

    prompt = f"""
Generate the resume in Markdown format.

Requirements:

- Return ONLY the resume.
- Do NOT include ATS checklist.
- Do NOT include notes.
- Do NOT include explanations.
- Do NOT include tips.
- Center should contain only the Name and Contact.
- Use professional wording.
- Expand the user's skills and projects naturally.
- Make it ATS-friendly.

Format:

# Full Name

Email | Phone

Education

Skills

Projects

Experience

User Information

Name:
{data.get("name")}

Email:
{data.get("email")}

Phone:
{data.get("phone")}

Education:
{data.get("education")}

Skills:
{data.get("skills")}

Projects:
{data.get("projects")}

Experience:
{data.get("experience")}
"""

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return {
            "resume": response.text
        }

    except Exception as e:
        return {
            "resume": f"Error generating resume: {str(e)}"
        }

@app.post("/ats")
def generate_ats(data: dict):

    prompt = f"""
You are an ATS (Applicant Tracking System).

Analyze the following resume information.

Give:

ATS Score: X/100

Strengths:
- Point 1
- Point 2
- Point 3

Suggestions:
- Point 1
- Point 2
- Point 3

Return ONLY the ATS analysis.
Do NOT include explanations.

Resume Information

Name:
{data.get("name")}

Education:
{data.get("education")}

Skills:
{data.get("skills")}

Projects:
{data.get("projects")}

Experience:
{data.get("experience")}
"""

    try:

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return {
            "ats": response.text
        }

    except Exception as e:

        return {
            "ats": f"Error: {str(e)}"
        }


@app.post("/improve")
def improve_resume(data: dict):

    prompt = f"""
You are an expert resume writer.

Improve the following resume.

Requirements:

- Keep the same information.
- Do NOT invent fake experience.
- Do NOT add false skills.
- Improve wording using professional language.
- Use strong action verbs.
- Keep the resume within ONE A4 page.
- Make it ATS-friendly.

Use EXACTLY this order:

# Full Name

Email | Phone

Professional Summary

Education

Skills

Projects

Experience

Return ONLY the improved resume in Markdown.
Do NOT change the section order.

Resume:

{data.get("resume")}
"""

    try:

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return {
            "resume": response.text
        }

    except Exception as e:

        return {
            "resume": f"Error: {str(e)}"
        }


@app.post("/cover-letter")
def generate_cover_letter(data: dict):

    prompt = f"""
Generate a professional Cover Letter.

Requirements:

- Return ONLY the cover letter.
- Use a professional and formal tone.
- Address the hiring manager professionally.
- Highlight the candidate's education.
- Mention technical skills.
- Mention projects.
- Mention experience.
- Express enthusiasm for the position.
- Keep it within one page.

User Information

Name:
{data.get("name")}

Email:
{data.get("email")}

Phone:
{data.get("phone")}

Education:
{data.get("education")}

Skills:
{data.get("skills")}

Projects:
{data.get("projects")}

Experience:
{data.get("experience")}
"""

    try:

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return {
            "cover": response.text
        }

    except Exception as e:

        return {
            "cover": f"Error: {str(e)}"
        }

@app.post("/linkedin")
def generate_linkedin_summary(data: dict):

    prompt = f"""
Generate a professional LinkedIn About section.

Requirements:

- Return ONLY the LinkedIn summary.
- Around 150–250 words.
- Professional tone.
- Highlight education.
- Mention technical skills.
- Mention projects.
- Mention experience.
- Mention career goals.
- Suitable for students and fresh graduates.

User Information

Name:
{data.get("name")}

Education:
{data.get("education")}

Skills:
{data.get("skills")}

Projects:
{data.get("projects")}

Experience:
{data.get("experience")}
"""

    try:

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return {
            "linkedin": response.text
        }

    except Exception as e:

        return {
            "linkedin": f"Error: {str(e)}"
        }