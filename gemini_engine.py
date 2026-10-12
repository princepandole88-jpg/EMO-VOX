# gemini_engine.py - Core LLM Reasoning & Local Database Logging
import os
import google.generativeai as genai
from prompts import get_injected_prompt
import sqlite3

class EmoVoxEngine:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel("gemini-1.5-flash")
        else:
            self.model = None
            print("Warning: GEMINI_API_KEY not found. Running in offline mock mode.")

    def process_interaction(self, user_query: str, detected_emotion: str, confidence: float):
        final_prompt = get_injected_prompt(user_query, detected_emotion)
        
        if self.model:
            try:
                response = self.model.generate_content(final_prompt)
                ai_response = response.text
            except Exception as e:
                ai_response = f"Error communicating with Gemini API: {str(e)}"
        else:
            ai_response = f"[Mock Response] I notice you seem {detected_emotion}. I am here to help!"

        self._log_to_db(detected_emotion, confidence, user_query, ai_response)
        return ai_response

    def _log_to_db(self, emotion: str, confidence: float, query: str, response: str, db_name="emo_vox_memory.db"):
        try:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO emotion_logs (detected_emotion, confidence_score, user_query, ai_response)
                VALUES (?, ?, ?, ?)
            ''', (emotion, confidence, query, response))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Database logging error: {e}")

if __name__ == "__main__":
    engine = EmoVoxEngine()
    print("EMO-VOX Core Engine initialized successfully.")

