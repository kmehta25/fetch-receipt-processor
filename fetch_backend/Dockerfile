FROM python:3.11

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY . /app/

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Add an entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

# CMD ["/entrypoint.sh"]
