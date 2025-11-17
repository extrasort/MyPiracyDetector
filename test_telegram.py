#!/usr/bin/env python3
"""
Helper script to test Telegram bot configuration.
Run this after setting up your bot to verify it works.
"""

import requests
import sys

def test_telegram_bot(bot_token, chat_id):
    """Send a test message via Telegram bot."""
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": "✅ <b>Success!</b>\n\nYour Telegram bot is configured correctly.\nYou'll receive piracy alerts here.",
            "parse_mode": "HTML"
        }
        resp = requests.post(url, json=payload, timeout=10)
        resp.raise_for_status()
        
        print("✅ Test message sent successfully!")
        print("Check your Telegram to confirm you received it.")
        return True
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        if resp.status_code == 404:
            print("   → Bot token is invalid or bot was deleted")
        elif resp.status_code == 400:
            print("   → Chat ID might be incorrect")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def get_bot_info(bot_token):
    """Get information about the bot."""
    try:
        url = f"https://api.telegram.org/bot{bot_token}/getMe"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        
        if data.get("ok"):
            bot_info = data.get("result", {})
            print("\n📱 Bot Information:")
            print(f"   Name: {bot_info.get('first_name')}")
            print(f"   Username: @{bot_info.get('username')}")
            print(f"   ID: {bot_info.get('id')}")
            return True
        return False
    except Exception as e:
        print(f"❌ Could not fetch bot info: {e}")
        return False

def main():
    print("=" * 50)
    print("Telegram Bot Configuration Test")
    print("=" * 50)
    
    # Get credentials from user
    print("\nEnter your Telegram bot credentials:")
    bot_token = input("Bot Token: ").strip()
    
    if not bot_token or bot_token == "YOUR_TELEGRAM_BOT_TOKEN_HERE":
        print("❌ Invalid bot token. Get one from @BotFather on Telegram.")
        sys.exit(1)
    
    # Verify bot exists
    print("\n🔍 Verifying bot...")
    if not get_bot_info(bot_token):
        sys.exit(1)
    
    chat_id = input("\nChat ID: ").strip()
    
    if not chat_id or chat_id == "YOUR_TELEGRAM_CHAT_ID_HERE":
        print("\n❌ Invalid chat ID.")
        print("\nTo get your chat ID:")
        print("1. Search for @userinfobot on Telegram")
        print("2. Send /start to get your chat ID")
        sys.exit(1)
    
    # Send test message
    print("\n📤 Sending test message...")
    if test_telegram_bot(bot_token, chat_id):
        print("\n" + "=" * 50)
        print("✅ Configuration is correct!")
        print("=" * 50)
        print("\nNext steps:")
        print("1. Update piracy_detector.py with these credentials")
        print("2. Run: python piracy_detector.py")
    else:
        print("\n" + "=" * 50)
        print("❌ Configuration failed")
        print("=" * 50)
        print("\nTroubleshooting:")
        print("1. Make sure you started a chat with your bot (send /start)")
        print("2. Verify the bot token from @BotFather")
        print("3. Verify your chat ID from @userinfobot")

if __name__ == "__main__":
    main()

