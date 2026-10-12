# vision_engine.py - Local OpenCV & DeepFace Emotion Tracking Engine
import cv2
import threading
from deepface import DeepFace
import time

class VisionEngine:
    def __init__(self):
        self.current_emotion = "Neutral"
        self.confidence = 0.0
        self.running = False
        self.thread = None
        
    def start_capture(self):
        """Starts the background webcam capture and emotion analysis thread."""
        self.running = True
        self.thread = threading.Thread(target=self._analyze_loop, daemon=True)
        self.thread.start()
        print("Vision Engine started background analysis.")

    def _analyze_loop(self):
        """Internal loop capturing frames every 2 seconds to optimize performance."""
        cap = cv2.VideoCapture(0)
        
        while self.running:
            if not cap.isOpened():
                time.sleep(1)
                continue
                
            ret, frame = cap.read()
            if not ret:
                time.sleep(0.5)
                continue
                
            try:
                # Analyze facial emotion locally using DeepFace
                analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                if isinstance(analysis, list):
                    analysis = analysis[0]
                    
                self.current_emotion = analysis.get('dominant_emotion', 'Neutral').capitalize()
                scores = analysis.get('emotion', {})
                self.confidence = float(scores.get(self.current_emotion.lower(), 0.0)) / 100.0
            except Exception as e:
                self.current_emotion = "Neutral"
                self.confidence = 0.0
                
            time.sleep(2.0)
            
        cap.release()

    def get_current_state(self):
        """Thread-safe method to fetch the latest detected emotion."""
        return self.current_emotion, self.confidence

    def stop_capture(self):
        """Stops the background vision thread."""
        self.running = False
        if self.thread:
            self.thread.join(timeout=1.0)
        print("Vision Engine stopped.")

if __name__ == "__main__":
    engine = VisionEngine()
    engine.start_capture()
    time.sleep(5)
    print("Test State:", engine.get_current_state())
    engine.stop_capture()

