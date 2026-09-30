import os
import sys
import subprocess
import webbrowser
import time

def main():
    print("=" * 65)
    print("  PSG COLLEGE OF ARTS AND SCIENCE (PSGCAS)")
    print("  Career Development Center (CDC) - AI Placement Web Chatbot")
    print("=" * 65)
    
    # Target port
    port = 8000
    host = "127.0.0.1"
    url = f"http://{host}:{port}"
    
    # Path to backend directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.join(project_dir, "backend")
    
    sys.path.insert(0, backend_dir)
    
    print(f"[INFO] Starting FastAPI server on {url}...")
    
    try:
        import uvicorn
        from app import app
        
        # Open browser automatically after brief delay
        def open_browser():
            time.sleep(1.5)
            print(f"[INFO] Opening web browser at {url}...")
            webbrowser.open(url)
            
        import threading
        threading.Thread(target=open_browser, daemon=True).start()
        
        uvicorn.run(app, host=host, port=port)
        
    except ImportError as e:
        print(f"[ERROR] Missing Python dependency: {e}")
        print("Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", os.path.join(backend_dir, "requirements.txt")])
        print("[INFO] Re-running launcher...")
        os.execv(sys.executable, [sys.executable] + sys.argv)

if __name__ == "__main__":
    main()
