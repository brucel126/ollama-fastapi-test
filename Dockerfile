FROM python

ENV OLLAMA_BASE_URL=http://host.docker.internal
ENV OLLAMA_PORT=11434

WORKDIR /server

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py"]