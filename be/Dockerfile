FROM python:3.11
EXPOSE 80
WORKDIR /code
RUN pip install "fastapi[all]" "uvicorn[standard]"
COPY ./main.py /code/main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
