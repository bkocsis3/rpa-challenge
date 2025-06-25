# RPA Challenge

### Challenge URL: [rpachallenge.com](https://rpachallenge.com/)

### Challenge Instructions
1. The goal of this challenge is to create a workflow that will input data from a spreadsheet into the form fields on the screen.
2. Beware! The fields will change position on the screen after every submission throughout 10 rounds thus the workflow must correctly identify where each spreadsheet record must be typed every time.
3. The actual countdown of the challenge will begin once you click the Start button until then you may submit the form as many times as you wish without receiving penalties.
Good luck!

### Setup
1. Download Python if needed: **[https://www.python.org/downloads/](https://www.python.org/downloads/)**
2. Open Command Prompt
3. CD into the 'Downloads' folder: **cd %USERPROFILE%\Downloads**
4. Clone this repo: **git clone https://github.com/bkocsis3/rpa-challenge.git**
5. CD into the repo folder: **cd rpa-challenge**
6. Create a virtual environment: **py -m venv rpa-challenge-venv**
7. Activate the virtual environment: **rpa-challenge-venv\Scripts\activate.bat**
8. Install dependancies in the virual environment: **pip install pandas requests selenium openpyxl**

### Running the Solution
There are two ways you can run this automation. If you want to watch it, use headed. If you want speed, use headless. It will run headless by default.
1. Headed: **py rpa-challenge.py --headtype=headed**
2. Headless: **py rpa-challenge.py** OR **py rpa-challenge.py --headtype=headless**

### To Do
1. Add error handling
2. Dockerize
