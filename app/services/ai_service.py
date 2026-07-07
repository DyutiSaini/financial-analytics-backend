import os

import json

import google.generativeai as genai

from dotenv import load_dotenv


load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API Key not found.")


genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_with_gemini(prompt: str):

    try:

        response = model.generate_content(prompt)

        text = response.text.strip()

        # Remove markdown if Gemini returns ```json ... ```
        if text.startswith("```json"):
            text = text.replace("```json", "", 1)

        if text.endswith("```"):
            text = text[:-3]

        text = text.strip()

        try:

            parsed_json = json.loads(text)

            return {
                "success": True,
                "analysis": parsed_json
            }

        except json.JSONDecodeError:

            return {
                "success": False,
                "message": "Gemini did not return valid JSON.",
                "raw_output": text
            }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }