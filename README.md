# Axura-Detect — Backend deploy to Render

This repo contains a small Flask backend used by the GitHub Pages frontend. GitHub Pages cannot run Python backends; use Render (or another host) to run the backend and point the frontend to the deployed URL.

Quick deploy (Render)

1. Create a Render account and connect your GitHub account.
2. In Render, click "New" → "Web Service" and choose this repository (`Axura-Detect`).
3. Render will detect `render.yaml` and propose a service. If not using the manifest, set these values:
   - Environment: `Python`
   - Branch: `main`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Health Check Path: `/health`
4. Deploy the service. Render will provide a public URL, e.g. `https://axura-detect.onrender.com`.

Frontend update

- Open `script.js` and change the API base URL to the Render service URL (replace `BASE` or relative paths):

```javascript
const BASE = "https://your-render-url.onrender.com";
```

Notes and recommendations

- `requirements.txt` includes `tensorflow`, which is large and may cause slow builds or failures on free plans. Consider:
  - Training models offline, saving weights (.h5), and loading them at runtime instead of `model.fit()` on import.
  - Replacing TensorFlow models with lightweight scikit-learn models for faster deploys.
- You can also deploy the provided `Dockerfile` on Render by selecting the Docker option when creating the service.

Local testing

1. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate    # Windows
# or `source venv/bin/activate` on macOS/Linux
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the backend locally:

```bash
set PORT=5000
python app.py
```

4. Test an endpoint:

```bash
curl -X POST http://127.0.0.1:5000/predict/wildfire -H "Content-Type: application/json" -d "{\"temperature\":35,\"humidity\":20,\"wind_speed\":30,\"forest_size\":500}"
```

If TensorFlow installation is slow or fails locally, use the `Dockerfile` to build a container (Docker required):

```bash
docker build -t axura-detect .
docker run -p 5000:5000 axura-detect
```

If you want, I can:

- Walk through creating the Render service and confirm settings, or
- Deploy a Docker image to Render, or
- Replace TensorFlow training-on-import with saved model loads to speed deployment.
