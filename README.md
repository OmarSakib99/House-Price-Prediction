# House-Price-Prediction



### Software and Tools Requirments

1. [Github Account](https://github.com)
2. [HerokuAccount](https://heroku.com)
3. [VS Code IDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)


Create a new environment

```python 
conda create -p venv python=3.9 -y

```

### Run The App Again

If you want to start the system back up again, open a terminal in the project folder and run:

```bash
source .venv/bin/activate
pip install -r Requirement.txt
python app.py
```

Then open http://127.0.0.1:5000/ in your browser.

On Windows PowerShell, use:

```powershell
\.venv\Scripts\Activate.ps1
pip install -r Requirement.txt
python app.py
```

### Notes

- The app uses `scikit-learn==1.6.1` in the requirements file.
- If you recreate the virtual environment, run the install command again before starting the app.