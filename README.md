# AI-Powered Resume Screener

## Project Overview
AI-Powered Resume Screener is a web-based application that automatically analyzes resumes and compares them with a given job description. It extracts important candidate information and calculates a match score using TF-IDF and cosine similarity.

## Problem Statement
Manually screening multiple resumes is time-consuming. This project helps automate the resume screening process and ranks candidates based on their relevance to the job description.

## Key Features
- Resume upload
- Supports PDF, DOCX and TXT files
- Automatic extraction of candidate details
- Job Description input
- Job Skills Required input
- TF-IDF based matching
- Match score calculation
- Matched and missing skills
- Candidate ranking
- Selected / Not Selected decision

## Technologies Used
- Python
- Flask
- Scikit-learn
- spaCy
- pypdf
- python-docx
- HTML/CSS

## System Workflow
1. Upload resumes
2. Extract resume text
3. Enter Job Description and required skills
4. Compare resumes with the job requirements
5. Calculate match scores
6. Rank candidates
7. Display screening results

## Project Structure

```text
AI-09_AI_Resume_Screener/
├── app.py
├── requirements.txt
├── templates/
├── static/
└── uploads/
