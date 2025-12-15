# Password Challange

[Challange](https://github.com/itidigital/backend-challenge)

## Requirements

- [ ] Python >= 3.13
- [ ] Docker Engine
- [ ] Docker Compose

## Execution

### Setup Environment

```bash
# create virtualenv
virtualenv .venv

# enable virtualenv(Linux)
source .venv/bin/activate

# install requirements/dependencies
pip install --requirement requirements.txt
```

### Running with Python

```bash
python src/main.py
```

### Running with FastAPI CLI

```bash
fastapi run ./src/app.py
```

### Running with Docker

```bash
docker compose up --build
```

> [!IMPORTANT]
> This application is designed to run on `localhost:8000`

> [!TIP]
> Check the documentation endpoint: http://localhost:8000/docs

## Testing

```bash
# all
pytest

# unit
pytest tests/unit

# integrated
pytest tests/integrated
```

## Making a Request

### With curl

Replace the `very complex value` on the following snippet to validate the desired value

```bash
curl -X POST http://localhost:8000/v1/auth/password \
    -H "Content-Type: application/json" \
    -d '{"password":"very complex value"}' 
```
