from fastapi import FastAPI
import socket

app = FastAPI(title="Aws Infra Enterprises API")

def get_system_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

@app.get("/")
def root():
    return {
        "private_ip": get_system_ip()
    }
