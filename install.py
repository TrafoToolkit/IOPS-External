import os
import glob
import subprocess
import pathlib

if __name__ == "__main__":
    list_paths_to_install_venv = [
        "./IOPS-mqtt-internal-interface/",
        "./IOPS-Data-Manager/",
        "./IOPS-Location-Engine-UWB/",
        "./IOPS-Logger/",
        "./IOPS-Live-Viewer/",
        "./IOPS-LivePNP/",
    ]

    reinstall = True
    python = "python3.11"


    for dirname in list_paths_to_install_venv:
        path_dir = pathlib.Path(os.getcwd()) / pathlib.Path(dirname)
        path_venv = (path_dir / "venv").resolve()
        posix_venv = path_venv.as_posix()

        print(f"Checking {path_venv}")

        if reinstall or not path_venv.exists():
            print("-> Installing....")
            if path_venv.exists():
                subprocess.run(["rm", "-r", "venv"], 
                            cwd=path_dir)
            subprocess.run([python, "-m", "venv", "venv"], 
                        cwd=path_dir)
            
            subprocess.run(["./venv/bin/python", "-m", "pip", "install", "-r", "requirements.txt"], 
                        cwd=path_dir, stdout=open(os.devnull, 'wb'))
            subprocess.run(["./venv/bin/python", "-m", "pip", "install", "--no-dependencies", "-e", "."], 
                        cwd=path_dir, stdout=open(os.devnull, 'wb'))
        else:
            print("-> Exists")
