import os
import subprocess

def open_app(app):
    apps = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "whatsapp": r"shell:AppsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App",
        "calculator": "calc.exe",
        "notepad": "notepad.exe"
    }

    if app in apps:
        if apps[app].startswith("shell:"):
            os.startfile(apps[app])
        else:
            subprocess.Popen(apps[app])
        return f"{app} opened."

    return "I don't know that application."