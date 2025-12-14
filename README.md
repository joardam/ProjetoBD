# Walkthrough - Academic Monitoring System Backend

## How to Run

1.  **Start the containers**:
    Open a terminal in the project root and run:
    ```bash
    docker-compose up --build
    ```

2.  **Apply Migrations**:
    Once the containers are running, open a new terminal (or use the existing one if detached) and run:
    ```bash
    docker-compose exec web python manage.py makemigrations core
    docker-compose exec web python manage.py migrate
    ```

3.  **Create a Superuser**:
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

4.  **Access the System**:
    -   **API Root**: http://localhost:8000/api/
    -   **Admin**: http://localhost:8000/admin/

## Project Structure
```
ProjetoBD/
├── .devcontainer/
│   └── devcontainer.json
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── docker-compose.yml
├── Dockerfile
├── manage.py
└── requirements.txt
```
