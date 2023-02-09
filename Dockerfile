FROM python:3
WORKDIR /AssistantNyraServer
COPY ./requirements.txt ./
COPY ./src ./src
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
