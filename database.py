# database.py - EMO-VOX Local Privacy Database Setup
import sqlite3

def init_db(db_name="emo_vox_memory.db"):
    """
    Initializes the local SQLite database for EMO-VOX.
    Stores emotion analysis logs and user settings strictly on the user's local machine.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Table to store local interaction history and emotion metrics
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emotion_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            detected_emotion TEXT NOT NULL,
            confidence_score REAL NOT NULL,
            user_query TEXT,
            ai_response TEXT
        )
    ''')
    
    # Table to store local system configuration and preferences
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_preferences (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    print(f"Database '{db_name}' initialized successfully with privacy-first schema.")

if __name__ == "__main__":
    init_db()


