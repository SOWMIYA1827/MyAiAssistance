import tkinter as tk
import webbrowser
import os
import subprocess
import re
import time

from datetime import datetime


# ============================================================
# OPEN APPLICATION
# ============================================================

def open_app(app_name):

    apps = {

        "chrome": [
            "cmd",
            "/c",
            "start",
            "",
            "chrome"
        ],

        "calculator": [
            "calc.exe"
        ],

        "notepad": [
            "notepad.exe"
        ],

        "vscode": [
            "code"
        ],

        "whatsapp": [
            "cmd",
            "/c",
            "start",
            "",
            "whatsapp:"
        ],

        "cmd": [
            "cmd.exe"
        ]
    }

    if app_name not in apps:
        return f"I don't know how to open {app_name} yet."

    try:

        subprocess.Popen(
            apps[app_name],
            shell=False
        )

        return f"{app_name.capitalize()} opened."

    except Exception as e:

        return f"Could not open {app_name}."


# ============================================================
# CLOSE APPLICATION
# ============================================================

def close_app(app_name):

    processes = {

        "chrome": "chrome.exe",

        "calculator": "CalculatorApp.exe",

        "notepad": "notepad.exe",

        "whatsapp": "WhatsApp.exe",

        "vscode": "Code.exe"
    }

    if app_name not in processes:

        return f"I don't know how to close {app_name} yet."

    process = processes[app_name]

    try:

        result = subprocess.run(
            [
                "taskkill",
                "/IM",
                process,
                "/F"
            ],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:

            return f"{app_name.capitalize()} closed."

        else:

            return f"{app_name.capitalize()} is not running."

    except Exception:

        return f"Could not close {app_name}."


# ============================================================
# CLOSE SPECIFIC CHROME TAB
# ============================================================

def close_chrome_tab(tab_name):

    """
    Attempts to close only a specific Chrome tab.

    Uses Chrome's Tab Search:
        Ctrl + Shift + A

    Then searches for the requested tab.
    """

    try:

        # Make sure Chrome is available
        chrome_check = subprocess.run(
            [
                "tasklist",
                "/FI",
                "IMAGENAME eq chrome.exe"
            ],
            capture_output=True,
            text=True
        )

        if "chrome.exe" not in chrome_check.stdout.lower():

            return "Chrome is not running."

        # Give Chrome focus
        subprocess.Popen(
            [
                "cmd",
                "/c",
                "start",
                "",
                "chrome"
            ]
        )

        time.sleep(1)

        try:

            import pyautogui

        except ImportError:

            return (
                "Please install pyautogui first using: "
                "pip install pyautogui"
            )

        # Open Chrome Tab Search
        pyautogui.hotkey(
            "ctrl",
            "shift",
            "a"
        )

        time.sleep(0.7)

        # Search tab
        pyautogui.write(
            tab_name,
            interval=0.03
        )

        time.sleep(0.7)

        # Select first result
        pyautogui.press("down")

        pyautogui.press("enter")

        time.sleep(0.7)

        # Close selected tab
        pyautogui.hotkey(
            "ctrl",
            "w"
        )

        return f"{tab_name.capitalize()} tab closed."

    except Exception as e:

        return f"Could not close {tab_name} tab."


# ============================================================
# CALCULATOR
# ============================================================

def calculate(command):

    """
    Supports:

    add 10 + 5
    subtract 20 - 5
    multiply 5 * 4
    divide 20 / 4

    Also:

    10 + 5
    20 - 5
    5 * 4
    20 / 4
    """

    expression = command

    # Remove words
    expression = re.sub(
        r"\b(add|plus|calculate|what is|what's)\b",
        "",
        expression
    )

    expression = expression.strip()

    # Only allow numbers and mathematical operators
    if not re.fullmatch(
        r"[0-9+\-*/().\s]+",
        expression
    ):

        return None

    try:

        # Safe evaluation
        result = eval(
            expression,
            {
                "__builtins__": None
            },
            {}
        )

        # Remove .0 from integer results
        if isinstance(result, float) and result.is_integer():

            result = int(result)

        return f"The answer is {result}."

    except Exception:

        return None


# ============================================================
# PROCESS COMMAND
# ============================================================

def process_command():

    command = entry.get().lower().strip()

    if not command:
        return

    result = None


    # ========================================================
    # CLEAR CHAT
    # ========================================================

    if command == "clear chat":

        chat.delete(
            "1.0",
            tk.END
        )

        entry.delete(
            0,
            tk.END
        )

        return


    # ========================================================
    # OPEN APPLICATIONS
    # ========================================================

    elif command == "open whatsapp":

        result = open_app("whatsapp")


    elif command == "open chrome":

        result = open_app("chrome")


    elif command == "open calculator":

        result = open_app("calculator")


    elif command == "open notepad":

        result = open_app("notepad")


    elif command in [
        "open vscode",
        "open vs code"
    ]:

        result = open_app("vscode")


    elif command in [
        "open cmd",
        "open command prompt"
    ]:

        result = open_app("cmd")


    # ========================================================
    # OPEN WEBSITES
    # ========================================================

    elif command == "open leetcode":

        webbrowser.open_new_tab(
            "https://leetcode.com"
        )

        result = "LeetCode opened."


    elif command == "open linkedin":

        webbrowser.open_new_tab(
            "https://www.linkedin.com"
        )

        result = "LinkedIn opened."


    elif command == "open github":

        webbrowser.open_new_tab(
            "https://github.com"
        )

        result = "GitHub opened."


    elif command == "open youtube":

        webbrowser.open_new_tab(
            "https://youtube.com"
        )

        result = "YouTube opened."


    elif command == "open google":

        webbrowser.open_new_tab(
            "https://google.com"
        )

        result = "Google opened."


    elif command == "open chatgpt":

        webbrowser.open_new_tab(
            "https://chatgpt.com"
        )

        result = "ChatGPT opened."


    # ========================================================
    # CLOSE APPLICATIONS
    # ========================================================

    elif command == "close chrome":

        result = close_app("chrome")


    elif command == "close calculator":

        result = close_app("calculator")


    elif command == "close notepad":

        result = close_app("notepad")


    elif command == "close whatsapp":

        result = close_app("whatsapp")


    elif command in [
        "close vscode",
        "close vs code"
    ]:

        result = close_app("vscode")


    # ========================================================
    # CLOSE SPECIFIC CHROME TABS
    # ========================================================

    elif command == "close leetcode":

        result = close_chrome_tab(
            "LeetCode"
        )


    elif command == "close linkedin":

        result = close_chrome_tab(
            "LinkedIn"
        )


    elif command == "close github":

        result = close_chrome_tab(
            "GitHub"
        )


    elif command == "close youtube":

        result = close_chrome_tab(
            "YouTube"
        )


    elif command == "close chatgpt":

        result = close_chrome_tab(
            "ChatGPT"
        )


    # ========================================================
    # DATE
    # ========================================================

    elif command in [
        "date",
        "today",
        "today date",
        "today's date",
        "what is today's date",
        "what is the date",
        "what is today's date today",
        "tell me today's date"
    ]:

        today = datetime.now().strftime(
            "%d-%m-%Y"
        )

        result = (
            f"Today's date is {today}."
        )


    # ========================================================
    # TIME
    # ========================================================

    elif command in [
        "time",
        "current time",
        "what time",
        "what is the time",
        "tell me the time",
        "what is current time"
    ]:

        current_time = datetime.now().strftime(
            "%I:%M:%S %p"
        )

        result = (
            f"The current time is {current_time}."
        )


    # ========================================================
    # CALCULATION
    # ========================================================

    elif (
        re.search(r"\d+\s*[\+\-\*/]\s*\d+", command)
        or command.startswith("add ")
        or command.startswith("calculate ")
        or command.startswith("plus ")
    ):

        result = calculate(command)

        if result is None:

            result = (
                "I could not calculate that."
            )


    # ========================================================
    # GREETINGS
    # ========================================================

    elif command in [
        "hi",
        "hello",
        "hey"
    ]:

        result = (
            "Hello! How can I help you?"
        )


    elif "how are you" in command:

        result = (
            "I'm doing great! "
            "Ready to help you."
        )


    # ========================================================
    # WINDOWS FILE EXPLORER
    # ========================================================

    elif command in [
        "open windows",
        "open file explorer",
        "open explorer"
    ]:

        subprocess.Popen(
            "explorer.exe"
        )

        result = (
            "Windows File Explorer opened."
        )


    # ========================================================
    # DOWNLOADS
    # ========================================================

    elif command == "open downloads":

        downloads_path = os.path.expanduser(
            "~/Downloads"
        )

        try:

            os.startfile(
                downloads_path
            )

            result = (
                "Downloads folder opened."
            )

        except Exception:

            result = (
                "Could not open Downloads."
            )


    # ========================================================
    # GOOGLE SEARCH
    # ========================================================

    elif command.startswith("search "):

        search_query = command[
            len("search "):
        ].strip()

        if search_query:

            url = (
                "https://www.google.com/search?q="
                + search_query.replace(
                    " ",
                    "+"
                )
            )

            webbrowser.open_new_tab(
                url
            )

            result = (
                f"Searching Google for "
                f"{search_query}."
            )

        else:

            result = (
                "What should I search for?"
            )


    # ========================================================
    # EXIT
    # ========================================================

    elif command in [
        "exit",
        "quit",
        "close assistant"
    ]:

        result = "Goodbye!"

        chat.insert(
            tk.END,
            "You: " + command + "\n"
        )

        chat.insert(
            tk.END,
            "AI: " + result + "\n\n"
        )

        chat.see(tk.END)

        window.after(
            1000,
            window.destroy
        )

        return


    # ========================================================
    # UNKNOWN COMMAND
    # ========================================================

    else:

        result = (
            "I don't understand this command yet."
        )


    # ========================================================
    # DISPLAY RESULT
    # ========================================================

    chat.insert(
        tk.END,
        "You: " + command + "\n"
    )

    chat.insert(
        tk.END,
        "AI: " + result + "\n\n"
    )

    chat.see(
        tk.END
    )

    entry.delete(
        0,
        tk.END
    )


# ============================================================
# GUI
# ============================================================

window = tk.Tk()

window.title(
    "My AI Assistant"
)

window.geometry(
    "600x500"
)


# ============================================================
# CHAT
# ============================================================

chat = tk.Text(
    window,
    font=("Arial", 12)
)

chat.pack(
    padx=10,
    pady=10,
    fill="both",
    expand=True
)


# ============================================================
# INPUT
# ============================================================

entry = tk.Entry(
    window,
    font=("Arial", 12)
)

entry.pack(
    side="left",
    padx=10,
    pady=10,
    fill="x",
    expand=True
)


# ============================================================
# SEND BUTTON
# ============================================================

button = tk.Button(
    window,
    text="Send",
    command=process_command,
    font=("Arial", 11)
)

button.pack(
    side="right",
    padx=10,
    pady=10
)


# ============================================================
# ENTER KEY
# ============================================================

entry.bind(
    "<Return>",
    lambda event: process_command()
)


# ============================================================
# START
# ============================================================

entry.focus()

window.mainloop()