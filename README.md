# House-Price-Prediction



### Software and Tools Requirements

1. [Github Account](https://github.com)
2. [Vercel Account](https://vercel.com)
3. [VS Code IDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)



Create a new environment

```bash
python -m venv .venv
```

### Run The App Again

If you want to start the system back up again, open a terminal in the project folder and run:

```bash
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000/ in your browser.

On Windows PowerShell, use:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

### Deploy to Vercel

1. Push the project to GitHub.
2. Import the repository into Vercel.
3. Make sure Vercel sees `requirements.txt` at the repo root.
4. Deploy the project. Vercel can load the Flask `app` object from [app.py](app.py).

### Notes

- Keep `scikit-learn==1.6.1` pinned so the saved model loads with the expected version.
- If you recreate the virtual environment, run the install command again before starting the app.