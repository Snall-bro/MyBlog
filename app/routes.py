from app import app

@app.route('/')
def undex():
    return "Hello world!"
