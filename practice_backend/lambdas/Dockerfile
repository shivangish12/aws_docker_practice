FROM public.ecr.aws/lambda/python:3.11

# Copy requirements first
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy handler
COPY handler.py .

CMD ["handler.lambda_handler"]