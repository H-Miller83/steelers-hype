from flask import Flask, jsonify

app = Flask(__name__)

# Health check endpoint
@app.route("/health")
def health():
    return {"status": "ok"}, 200

# Temporary hardcoded players
players = [
    {"id": 1, "name": "T.J. Watt"},
    {"id": 2, "name": "George Pickens"},
    {"id": 3, "name": "Najee Harris"},
]

@app.route("/players")
def get_players():
    return jsonify(players)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
