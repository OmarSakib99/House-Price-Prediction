# House Price Prediction

This repository is a Flask app that predicts Boston house prices using a saved scikit-learn model.

## Project Summary

- Flask serves the web UI and prediction endpoints.
- The main app entrypoint is [app.py](app.py).
- The HTML form lives in [templates/home.html](templates/home.html).
- The model artifacts are [regmodel.pkl](regmodel.pkl) and [scaler.pkl](scaler.pkl).
- The dataset source is [Boston House Price Data.csv](Boston%20House%20Price%20Data.csv).
- Live deployment URL: [https://house-price-prediction-zi57.vercel.app/](https://house-price-prediction-zi57.vercel.app/)

## Local Development

1. Activate the virtual environment:
   - `source .venv/bin/activate`
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Run the app:
   - `python app.py`
4. Open the app at:
   - `http://127.0.0.1:5000/`

## Routes

- `GET /` renders the prediction form.
- `POST /predict` accepts form data and returns the prediction on the same page.
- `POST /predict_api` accepts JSON payloads and returns JSON.

## Important Implementation Details

- The model files are loaded from the same directory as [app.py](app.py), not from the current working directory.
- Keep the input field order in [templates/home.html](templates/home.html) aligned with the model feature order.
- `scikit-learn==1.6.1` is pinned because the pickled model was created with that version.
- `requirements.txt` only lists what [app.py](app.py) actually imports at runtime (Flask, scikit-learn, numpy, gunicorn) — training-only libraries (pandas, matplotlib) live in the notebook's own environment, not here.

## Vercel Deployment Notes

- Documented zero-config Flask auto-detection (bare `app.py` + `requirements.txt`, no `builds` in vercel.json) does **not** trigger for this repo on the current CLI/platform — it silently resolves to the `@vercel/static` builder over `**`, which serves every repo file (including `app.py` and the `.pkl` model files) as a raw static asset and 404s on `/` since there's no `index.html`. Verified locally with `vercel build --debug` (`Resolved builders: "@vercel/static => undefined"`).
- The fix is the explicit `builds`/`routes` config in [vercel.json](vercel.json):
  ```json
  {
    "builds": [{ "src": "app.py", "use": "@vercel/python" }],
    "routes": [{ "src": "/(.*)", "dest": "app.py" }]
  }
  ```
  This forces `@vercel/python` on `app.py` and routes all paths to it. Verified locally: `Resolved builders: "@vercel/python => 6.47.3"`, and the resulting `.vercel/output/functions/app.py.func` is a single serverless function with a catch-all route — no file leakage.
- The live deployed app is available at [https://house-price-prediction-zi57.vercel.app/](https://house-price-prediction-zi57.vercel.app/).
- `builds` in vercel.json overrides Project Settings (Framework Preset/Build Command are ignored while it's present) — expected, do not "clean this up" by removing it in favor of zero-config again without re-verifying with `vercel build --debug` first.
- The Python builder installs from [pyproject.toml](pyproject.toml)'s `[project.dependencies]` (via `uv`), not `requirements.txt`, when both exist — keep the two in sync; `requirements.txt` is still what local dev uses via `pip install -r requirements.txt`.
- There is no Dockerfile or custom build script; keep it that way unless a real need for a custom build step comes up.

## Editing Guidelines

- Avoid changing the trained model files unless you are retraining or replacing the model.
- Avoid changing the form field names unless you also update the prediction input ordering.
- Prefer minimal edits that preserve the current Flask and Jinja structure.
