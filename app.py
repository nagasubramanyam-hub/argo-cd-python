from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Argo CD Python Demo</h1>
    <h2>Status: Running on Kubernetes</h2>
    <h3>CI/CD using GitOps</h3>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)