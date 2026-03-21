from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return """
    <h1>🚀 CI/CD Pipeline Working!</h1>
    <p>Jenkins + Docker + GitHub Integration Successful</p>
    """

@app.route('/health')
def health():
    return "App is running ✅"

@app.route('/version')
def version():
    return "Version 1.0 - Deployed via Jenkins CI/CD"

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
