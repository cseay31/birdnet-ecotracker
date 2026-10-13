# BirdNET EcoTracker

BirdNET EcoTracker is a lightweight Flask service that accepts uploaded audio and runs BirdNET analysis to identify bird species from sound recordings.

This project is designed to run as a small HTTP wrapper around the BirdNET analyzer library, making it easy to integrate with other services or home-automation workflows.

## What it does

- Exposes a `/health` endpoint for simple uptime checks
- Accepts uploaded audio via HTTP POST to `/analyze`
- Runs BirdNET inference on the provided file
- Returns the detection results as structured JSON
- Supports configurable confidence and sensitivity values

## Project structure

- `server.py` – Flask app entrypoint and HTTP route definitions
- `requirements.txt` – Python dependencies
- Uses the BirdNET Analyzer library from GitHub for actual species detection

## Local setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set the BirdNET model path if needed:

```bash
export BIRDNET_MODEL="/path/to/model"
```

4. Run the service:

```bash
gunicorn server:app --bind 0.0.0.0:8000
```

## API

### Health check

```bash
curl http://localhost:8000/health
```

### Analyze audio

```bash
curl -X POST http://localhost:8000/analyze \
  -F "audio=@example.wav" \
  -F "min_conf=0.1" \
  -F "sensitivity=1.0"
```

Example response:

```json
{
  "detections": [
    {
      "common_name": "American Robin",
      "scientific_name": "Turdus migratorius",
      "confidence": 0.87
    }
  ]
}
```

## Notes

This repository is intentionally small and focused: it is a backend API layer on top of BirdNET, rather than a full web app or dashboard.

## License

No explicit license has been specified for this repository.
