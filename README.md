# RPA Challenge

## 📖 Overview
The goal of this project is to provide a production-ready Python solution that:

1. Solves the [RPA Challenge](https://rpachallenge.com), a popular benchmark for RPA developers. This task involves extracting data from an Excel file and entering it into web form with randomly placed fields - ten times.
2. Is Docker-ready, allowing the solution to run easily across environments.
3. Supports both **headed mode** (for visual debugging) and **headless mode** (for fast, efficient execution).

** This was created on Windows, so some commands are Windows specific. 

---

## 🐳 If You're Using Docker
### ⚙️ Setup
1. Download Docker if needed: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. Download a VNC viewer if needed. I used Remote Ripple: [https://remoteripple.com/download/](https://remoteripple.com/download/)
4. Open Command Prompt
5. Navigate to Downloads:  
   ```bash
   cd %USERPROFILE%\Downloads
   ```
6. Clone the repository:
   ```bash
   git clone https://github.com/bkocsis3/rpa-challenge.git
   ```
7. Change into the repo folder:
   ```bash
   cd rpa-challenge
   ```
8. Build a Docker image using the repo Dockerfile:
   ```bash
   docker build -t rpa-challenge .
   ```

### 🏃Running the Solution in headed mode (for visual debugging)
1. Run the new image to create a container:  
    ```bash
    docker run -d -p 5900:5900 --name rpa-challenge-con rpa-challenge
    ```
2. Using your VNC viewer, connect to the new container using localhost:5900 & 'secret' as the password
3. Execute the Python solution
    ```bash
    docker exec rpa-challenge-con python rpa-challenge.py --headtype=headed
    ```  
4. Watch the automation in your VNC viewer

### 🏃Running the Solution in headless mode (for fast, efficient execution)
- Default command
    ```bash
    docker run --name rpa-challenge-con python rpa-challenge.py
    ```
or
- Explicit command
    ```bash
    docker run --name rpa-challenge-con python rpa-challenge.py --headtype=headless
    ```

---

## 🐍 If you're using Python
### ⚙️ Setup

1. Download Python if needed: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Open Command Prompt
3. Navigate to Downloads:  
   ```bash
   cd %USERPROFILE%\Downloads
   ```

6. Create a virtual environment:
   ```bash
   py -m venv rpa-challenge-venv
   ```
7. Activate the virtual environment:
   ```bash
   rpa-challenge-venv\Scripts\activate.bat
   ```
8. Install dependancies:
   ```bash
   pip install pandas requests selenium openpyxl
   ```

### 🏃Running the Solution in headed mode (for visual debugging)
```bash
    py rpa-challenge.py --headtype=headed
```

### 🏃Running the Solution in headless mode (for fast, efficient execution)
- Default command
    ```bash
    py rpa-challenge.py
    ```
   or
- Explicit command
    ```bash
    py rpa-challenge.py --headtype=headless
    ```

--- 

## 💡Improvement Ideas
- [ ] Add error handling to the Python solution
- [ ] Add a way to set a new VNC password for better security
