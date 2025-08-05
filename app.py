import speech_recognition as sr
import paramiko

# TonyPi SSH credentials
HOST = "192.168.1.52"   # Replace with your robot's IP
USERNAME = "pi"
PASSWORD = "raspberry"  # Replace if changed

def send_to_tonypi(text):
    """Send text to TonyPi to speak via espeak."""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(HOST, username=USERNAME, password=PASSWORD)
        command = f'espeak "{text}"'
        ssh.exec_command(command)
        ssh.close()
        print(f"✅ TonyPi said: {text}")
