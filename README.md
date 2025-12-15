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

> [!TIP]
> Check the documentation endpoint: http://localhost:8000/docs \
> It provides an interactive interface to test the API.

## Hexagonal Architecture

Hexagonal architecture (aka Ports & Adapters) organizes an application so the core domain logic is isolated from external concerns (HTTP, DB, UI). The domain sits in the center, defines ports (interfaces) and is implemented by adapters placed on the outside. Adapters call into the domain through ports, and the domain is independent of any framework or transport.

Key ideas:
- Dependency rule: outer layers depend on inner ones only through interfaces/ports.
- Core domain contains business rules and should have no framework dependencies.
- Adapters (HTTP, DB, CLI) implement ports and translate between external models and domain models.

Advantages:
- Testability: domain logic can be unit tested in isolation without HTTP or DB.
- Modularity: adapters can be swapped (e.g., replace REST with gRPC) with minimal domain changes.
- Clear separation of concerns reduces coupling and improves maintainability.

Disadvantages:
- Higher initial complexity and some boilerplate (interfaces, adapters) for small projects.
- Can be over-architected if the application is trivial.
- Requires discipline: poor boundary definitions can lead to unnecessary abstractions.

## Folder Structure

Below is a tre-like view of the repository focused on the application code and a short comment for each file/folder. This maps the hexagonal roles (domain, ports, adapters) to concrete files.

```
.                         # repository root
├── docker-compose.yaml   # docker compose for running containers
├── Dockerfile            # image build instructions
├── requirements.txt      # Python dependencies
├── src/                  # application source (hexagonal layers)
│   ├── app.py            # FastAPI app & wiring (adapter/bootstrap)
│   ├── main.py           # application entrypoint (runner)
│   ├── domain/           # core business rules (domain layer)
│   │   └── entities/
│   │       └── password.py  # Password entity: validation & strength rules
│   ├── services/         # application services / use-cases (ports)
│   │   └── auth.py       # Auth service: orchestrates password checks
│   ├── entrypoints/      # inbound adapters (HTTP routes)
│   │   └── routes/
│   │       └── v1/
│   │           └── auth.py  # FastAPI route for /v1/auth/password
│   └── schemas/
│       └── password.py   # Pydantic DTOs: request/response models (boundary)
└── tests/                # unit & integration tests
```

This layout shows where each hexagonal layer lives and which files act as adapters (HTTP, bootstrap) versus domain/core logic and application ports.

## High-level Request Flow

1. Client calls POST /v1/auth/password with JSON body (handled by FastAPI route).
2. Route uses a Pydantic schema from `src/schemas/password.py` to validate and parse the request.
3. Route calls an application service in `src/services/auth.py` which acts as the use-case / port.
4. The service performs domain operations (instantiates or delegates to domain entities in `src/domain/entities/password.py`).
5. The domain entity encapsulates password rules and returns results (valid/invalid, messages, metadata).
6. Service adapts domain result into a response schema or primitive and route returns HTTP response.

This is the canonical Hexagonal direction: adapters (HTTP) -> application services -> domain (core) -> application services -> adapters (HTTP response).

## Decisions

I decided to use an hexagonal architecture for this project as it provides a clear separation of concerns between the core business logic and the external interfaces. This example projects doesn't contain interfaces to databases or other external systems, but the architecture allows for easy extension in the future if needed.

The password string is treated as a `Domain Entity` to make it portable and encapsulate all related validation and strength logic within a single cohesive unit. I could make the validations at the contract/schema levels, but placing them in a domain entity ensures that any future use-cases (beyond just HTTP requests) will consistently apply the same business rules.

The `AuthService` acts as a use-case orchestrator, coordinating between the HTTP layer and the domain entity without embedding business logic itself, adhering to the single responsibility principle. It keeps a `__init__` method to initialize the service with necessary dependencies.
