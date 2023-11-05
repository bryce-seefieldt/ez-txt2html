import subprocess

subprocess.run(['flake8', './src/.'])
subprocess.run(['black', './src/.'])
