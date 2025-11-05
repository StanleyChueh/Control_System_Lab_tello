# 🛩️ Tello Drone Environment Setup (Conda)

This guide walks you through setting up a Conda environment for running Tello drone control with **djitellopy**, **OpenCV**, **MediaPipe**, and **cvzone**.

---

## 🧰 1. Install Conda Env

### Conda window
```
Invoke-WebRequest https://repo.anaconda.com/archive/Anaconda3-2025.06-0-Windows-x86_64.exe -OutFile "$env:USERPROFILE\Downloads\Anaconda3-2025.06-0-Windows-x86_64.exe"
```

```
Start-Process "$env:USERPROFILE\Downloads\Anaconda3-2025.06-0-Windows-x86_64.exe"
```
Add to environment variable
```
[Environment]::SetEnvironmentVariable(
  "Path",
  $env:Path + ";$env:USERPROFILE\anaconda3;$env:USERPROFILE\anaconda3\Scripts;$env:USERPROFILE\anaconda3\Library\bin",
  "User"
)
```

Verify
```
conda --version
```
you should see something like this:
```
conda 25.5.1
```

### Linux
```
wget https://repo.anaconda.com/archive/Anaconda3-2025.06-1-Linux-x86_64.sh
bash Anaconda3-2025.06-1-Linux-x86_64.sh
```

### Tello Env

Accept Conda ToS
```
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/msys2
```
```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Create conda environment
create another terminal
```
conda init
conda create -n tello python=3.8 -y
```

```
pip install -r .\requirement.txt
```

