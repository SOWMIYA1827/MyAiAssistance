# ai.py

def understand_command(command):
    """
    Convert user's natural language command
    into a simple action.
    """

    command = command.lower().strip()

    

    # Open WhatsApp
    if "whatsapp" in command and (
        "open" in command or
        "launch" in command or
        "start" in command
    ):
        return {
            "action": "open_app",
            "app": "whatsapp"
        }

    # Open Chrome
    if "chrome" in command and (
        "open" in command or
        "launch" in command
    ):
        return {
            "action": "open_app",
            "app": "chrome"
        }

    # Open Calculator
    if "calculator" in command and (
        "open" in command or
        "launch" in command
    ):
        return {
            "action": "open_app",
            "app": "calculator"
        }

    # Open Notepad
    if "notepad" in command and (
        "open" in command or
        "launch" in command
    ):
        return {
            "action": "open_app",
            "app": "notepad"
        }

    # Create folder
    if "create" in command and "folder" in command:
        return {
            "action": "create_folder"
        }

    # Unknown command
    return {
        "action": "unknown",
        "message": "I don't understand this command yet."
    }