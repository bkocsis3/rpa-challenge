#get official starter image
FROM selenium/standalone-chrome:latest

#set working directory
WORKDIR /app

#install python solution dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#copy python solution
COPY rpa-challenge.py ./

#set run command
CMD ["python", "rpa-challenge.py"]




