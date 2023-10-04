FROM python:3.10.7-slim
ADD pipline_executor.py /home/pipline_executor.py
ADD requirements.txt ./
RUN pip install -r requirements.txt
ENTRYPOINT ["python","/home/pipline_executor.py"]