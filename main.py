# main.py - EMO-VOX Main Application Launcher
import time
from database import init_db
from vision_engine import VisionEngine
from gemini_engine import EmoVoxEngine

def main():
    print("Initializing EMO-VOX System...")
    
    # 1. Initialize local SQLite database
    init_db()
    
    # 2. Start vision background tracking
    vision = VisionEngine()
    vision.start_capture()
    
    # 3. Initialize Gemini LLM Engine
    llm = EmoVoxEngine()
    
    print("\n--- EMO-VOX CLI Test Harness ---")
    print("Type 'exit' to quit.\n")
    
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                break
                
            # Get real-time emotion from vision thread
            current_emotion, confidence = vision.get_current_state()
            print(f"[Detected Emotion: {current_emotion} ({confidence:.2f})]")
            
            # Process query with Gemini API
            response = llm.process_interaction(user_input, current_emotion, confidence)
            print(f"EMO-VOX: {response}\n")
            
    finally:
        vision.stop_capture()
        print("EMO-VOX shut down gracefully.")

if __name__ == "__main__":
    main()

