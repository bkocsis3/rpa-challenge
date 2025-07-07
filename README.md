# RPA Challenge Solution

---

### 📖 Overview
The goal of this project is to provide a production-ready Python solution that:

1. Solves the [RPA Challenge](https://rpachallenge.com), a popular benchmark for RPA developers. The task involves extracting data from a provided Excel file and inputting it into a dynamically shuffled web form - ten times.
2. Is Docker-ready, allowing the solution to run easily across environments.
3. Supports both **headed mode** (for visual debugging) and **headless mode** (for fast, efficient execution).

---

### ⚙️ Setup (Using Docker, Assuming on Windows)

1. Download Docker if needed: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. Download a VNC viewer if needed. I used Remote Ripple: [https://remoteripple.com/download/](https://remoteripple.com/download/)
4. Open Command Prompt
5. Navigate to Downloads:  
   ``` bash#
   cd %USERPROFILE%\Downloads
   ```
6. Clone the repository:
   ``` bash#
   git clone https://github.com/bkocsis3/rpa-challenge.git
   ```
7. Change into the repo folder:
   ``` bash#
   cd rpa-challenge
   ```
8. Build the Docker image:
   ``` bash#
   docker build -t rpa-challenge .
   ```
   
---

### 🏃Running the Solution (With Docker, Assuming on Windows)
You can run this solution one of two ways. 
- Headed (for Visual Debugging):
   1. Run the docker image:
      ``` bash#
      docker run -d -p 5900:5900 --name rpa-challenge-con rpa-challenge
      ```
   2. VNC into the container. See the screenshots below if using Remote Ripple.
      -1
      -2
      -3
   4. Execute the Python solution
      ``` bash#
      docker exec rpa-challenge-con python rpa-challenge.py --headtype=headed
      ```
   
- Headless (for Fast, Efficient Execution):
    ``` bash#
   py rpa-challenge.py
   ```
   or
   ``` bash#
   py rpa-challenge.py --headtype=headless
   ```

---

### ⚙️ Setup (Without Docker, Just Python, Assuming on Windows)

1. Download Python if needed: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Open Command Prompt
3. Navigate to Downloads:  
   ``` bash#
   cd %USERPROFILE%\Downloads
   ```

6. Create a virtual environment:
   ``` bash#
   py -m venv rpa-challenge-venv
   ```
7. Activate the virtual environment:
   ``` bash#
   rpa-challenge-venv\Scripts\activate.bat
   ```
8. Install dependancies:
   ``` bash#
   pip install pandas requests selenium openpyxl
   ```

### 🏃Running the Solution (Without Docker, Just Python, Assuming on Windows)
You can run this solution one of two ways. 
- Headed (for Visual Debugging):
   ``` bash#
   py rpa-challenge.py --headtype=headed
   ```
- Headless (for Fast, Efficient Execution):
    ``` bash#
   py rpa-challenge.py
   ```
   or
   ``` bash#
   py rpa-challenge.py --headtype=headless
   ```

---

### 🧠 To Do
- [ ] Add error handling

