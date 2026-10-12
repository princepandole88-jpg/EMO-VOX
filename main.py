# main.py - EMO-VOX Main Application Launcher with Voice Integration
import time
from database import init_db
from vision_engine import VisionEngine
from gemini_engine import EmoVoxEngine
from audio_engine import AudioEngine

def main():
    print("Initializing EMO-VOX System with Voice & Vision...")
    init_db()
    
    vision = VisionEngine()
    vision.start_capture()
    
    llm = EmoVoxEngine()
    audio = AudioEngine()
    
    audio.speak("EMO-VOX is online and ready.")
    print("\n--- EMO-VOX Voice & Vision Mode ---")
    
    try:
        while True:
            user_input = audio.listen_speech()
            if not user_input:
                user_input = input("You (fallback text): ")
                
            if user_input.lower() in ["exit", "quit"]:
                audio.speak("Shutting down EMO-VOX. Goodbye!")
                break
                
            if not user_input.strip():
                continue
                
            current_emotion, confidence = vision.get_current_state()
            print(f"[Detected Emotion: {current_emotion} ({confidence:.2f})]")
            
            response = llm.process_interaction(user_input, current_emotion, confidence)
            audio.speak(response)
            
    finally:
        vision.stop_capture()
        print("EMO-VOX shut down gracefully.")

if __name__ == "__main__":
    main()

