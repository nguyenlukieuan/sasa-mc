import subprocess
script_path = """
git add . && git commit -m "save status" && git push 

"""

try:
    subprocess.run(script_path, shell=True, check=True)
    print("Update status completed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing the shell command: {e}")
