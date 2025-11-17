#!/usr/bin/env python3
"""
Web server wrapper for Railway deployment.
Provides HTTP endpoints to trigger the piracy detection script.
"""

from flask import Flask, jsonify, request
import os
import threading
from piracy_detector import main as run_piracy_check

app = Flask(__name__)

# Secret key for triggering scans (set via environment variable)
SECRET_KEY = os.getenv("SCAN_SECRET_KEY", "change_this_secret_key")

@app.route('/')
def index():
    """Health check endpoint."""
    return jsonify({
        "status": "online",
        "service": "Novel Piracy Detector",
        "novel": os.getenv("NOVEL_TITLE", "Not configured"),
        "author": os.getenv("AUTHOR_NAME", "Not configured")
    })

@app.route('/health')
def health():
    """Health check for Railway."""
    return jsonify({"status": "healthy"}), 200

@app.route('/scan', methods=['POST', 'GET'])
def trigger_scan():
    """
    Trigger a piracy scan.
    Requires secret key for authentication.
    """
    # Check secret key
    provided_key = request.args.get('key') or request.headers.get('X-Secret-Key')
    
    if provided_key != SECRET_KEY:
        return jsonify({
            "error": "Unauthorized",
            "message": "Invalid or missing secret key"
        }), 401
    
    # Run scan in background thread to avoid timeout
    def run_scan():
        try:
            print("🔍 Starting piracy scan...")
            run_piracy_check()
            print("✅ Scan completed")
        except Exception as e:
            print(f"❌ Scan error: {e}")
    
    thread = threading.Thread(target=run_scan)
    thread.daemon = True
    thread.start()
    
    return jsonify({
        "status": "success",
        "message": "Piracy scan started. Results will be sent to Telegram."
    }), 200

@app.route('/config')
def show_config():
    """Show current configuration (without sensitive data)."""
    config = {
        "novel_title": os.getenv("NOVEL_TITLE", "Not set"),
        "author_name": os.getenv("AUTHOR_NAME", "Not set"),
        "telegram_enabled": os.getenv("TELEGRAM_ENABLED", "true"),
        "serpapi_configured": bool(os.getenv("SERPAPI_KEY") and os.getenv("SERPAPI_KEY") != "YOUR_SERPAPI_KEY_HERE"),
        "telegram_configured": bool(os.getenv("TELEGRAM_BOT_TOKEN") and os.getenv("TELEGRAM_BOT_TOKEN") != "YOUR_TELEGRAM_BOT_TOKEN_HERE")
    }
    return jsonify(config)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    print(f"🚀 Starting Novel Piracy Detector on port {port}")
    print(f"📚 Novel: {os.getenv('NOVEL_TITLE', 'Not configured')}")
    print(f"✍️ Author: {os.getenv('AUTHOR_NAME', 'Not configured')}")
    app.run(host='0.0.0.0', port=port)

