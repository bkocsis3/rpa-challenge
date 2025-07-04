# RPA Challenge Solution

---

### 📖 Overview
The goal of this project is to provide a production-ready RPA solution that:

1. Solves the [RPA Challenge](https://rpachallenge.com), a popular benchmark for RPA developers. The task involves extracting data from a provided Excel file and inputting it into a dynamically shuffled web form ten times.
2. Is Docker-ready, allowing the solution to run easily across environments.
3. Supports both **headed mode** (for visual debugging) and **headless mode** (for fast, efficient execution).

---

### ⚙️ Setup (Without Docker)

1. Download Python if needed: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Open Command Prompt
3. Navigate to Downloads:  
   ```
   cd %USERPROFILE%\Downloads
4. Clone the repository:
   ```
   git clone https://github.com/bkocsis3/rpa-challenge.git
5. Change into the repo folder:
   ```
   cd rpa-challenge
6. Create a virtual environment:
   ```
   py -m venv rpa-challenge-venv
7. Activate the virtual environment:
   ```
   rpa-challenge-venv\Scripts\activate.bat
8. Install dependancies:
   ```
   pip install pandas requests selenium openpyxl


### Running the Solution (Without Docker)
You can run this solution in two ways. 
* Headed (for Visual Debugging):
  ``` bash#
  py rpa-challenge.py --headtype=headed
  ```
* Headless (for Normal Operation):
  ``` bash#
  py rpa-challenge.py
  ```
   OR
  ``` bash#
  py rpa-challenge.py --headtype=headless
  ```

---

### 🧠 To Do
- [ ] Add error handling
- [ ] Extend headed mode to Docker

