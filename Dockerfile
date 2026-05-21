# use official AWS Lambda Python 3.12 base image
FROM public.ecr.aws/lambda/python:3.12

# copy requirements first for better caching
COPY requirements.txt .

# install dependencies without cache
RUN pip install --no-cache-dir -r requirements.txt

# copy all project files into container
COPY . .

# lambda handler entrypoint
CMD ["lambda_handler.handler"]