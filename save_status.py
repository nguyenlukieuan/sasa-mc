import subprocess
script_path = """
cd /home/user/games/sasa-mc && git pull
"""

try:
    subprocess.run(script_path, shell=True, check=True)
    print("Pull code completed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing the shell command: {e}")
