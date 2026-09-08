import os
from flask import Flask, request, jsonify
from birdnet_analyzer import analyze

app = Flask(__name__)
MODEL_PATH = os.environ.get("BIRDNET_MODEL", "")
@app.route('/health')
def health(): return 'ok'
@app.post("/analyze")
def analyze_audio():
    if "audio" not in request.files:
        return jsonify({"error": "no audio file"}), 400
    audio = request.files["audio"]
    tmp = f"/tmp/{audio.filename}"
    audio.save(tmp)
    result = analyze(
        tmp,
        min_conf=float(request.form.get("min_conf", 0.1)),
        sensitivity=float(request.form.get("sensitivity", 1.0)),
    )
    return jsonify({"detections": result})

