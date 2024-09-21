import subprocess
script_path = """
cd /home/user/games && git clone https://github.com/nguyenlukieuan/sasa-mc.git
"""

try:
    subprocess.run(script_path, shell=True, check=True)
    print("Backup completed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing the shell command: {e}")
