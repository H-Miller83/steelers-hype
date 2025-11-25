from flask import Flask, jsonify, render_template
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

players = [
    {
        "id": 1,
        "name": "T.J. Watt",
        "image": "/static/images/tj_watt.jpg",
        "video": "/static/videos/tj_watt_hype_video.mp4"  
    },
    {
        "id": 2,
        "name": "Ben Roethlisberger",
        "image": "/static/images/big_ben.jpg",
        "video": "/static/videos/big_ben.mp4"
    },
    {
        "id": 3,
        "name": "George Pickens",
        "image": "/static/images/pickens.jpg",
        "video": "/static/videos/george_pickens.mp4"
    },
    {
        "id": 4,
        "name": "Troy Polamalu",
        "image": "/static/images/troy_polamalu.jpg",
        "video": "/static/videos/troy_polamalu.mp4"
    },
    {
        "id": 5,
        "name": "Heath Miller",
        "image": "/static/images/heath_miller.jpeg",
        "video": "/static/videos/heath_miller.mp4"
    },
    {
        "id": 6,
        "name": "Antonio Brown",
        "image": "/static/images/antonio_brown.jpg",
        "video": "/static/videos/antonio_brown.mp4"
    },
    {
        "id": 7,
        "name": "Franco Harris",
        "image": "/static/images/franco_harris.jpg",
        "video": "/static/videos/franco_harris.mp4"
    },
    {
        "id": 8,
        "name": "Jerome Bettis",
        "image": "/static/images/jerome_bettis.jpg",
        "video": "/static/videos/jerome_bettis.mp4"
    },
    {
        "id": 9,
        "name": "James Harrison",
        "image": "/static/images/james_harrison.webp",
        "video": "/static/videos/james_harrison.mp4"
    },
    {
        "id": 10,
        "name": "Ryan Shazier",
        "image": "/static/images/ryan_shazier.jpg",
        "video": "/static/videos/ryan_shazier.mp4"
    },
    {
        "id": 11,
        "name": "Hines Ward",
        "image": "/static/images/hines_ward.jpg",
        "video": "/static/videos/hines_ward.mp4"
    },
    {
        "id": 12,
        "name": "Mean Joe Greene",
        "image": "/static/images/joe_greene.webp",
        "video": "/static/videos/joe_greene.mp4"
    }

]

@app.route("/")
def home():
    return render_template("index.html", players=players)

@app.route("/player/<int:player_id>")
def player_page(player_id):
    player = next((p for p in players if p["id"] == player_id), None)
    if not player:
        return "Player not found", 404
    return render_template("player.html", player=player)

@app.route("/health")
def health():
    logging.info("Health check requested")
    return {"status": "ok"}, 200

@app.route("/players")
def get_players():
    return jsonify(players)

@app.route("/works-cited")
def works_cited():
    return render_template("works_cited.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
