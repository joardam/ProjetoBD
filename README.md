# Walkthrough - Academic Monitoring System Backend

I have successfully created the initial structure for your Django backend project.

## What has been done

1.  **Infrastructure**:
    -   Created `Dockerfile` and `docker-compose.yml` for running the project with PostgreSQL.
    -   Created `.devcontainer/devcontainer.json` for GitHub Codespaces compatibility.
    -   Created `requirements.txt` with necessary dependencies.

2.  **Django Project**:
    -   Created the project configuration in `config/`.
    -   Configured `settings.py` to use PostgreSQL and the custom user model.
    -   Configured `urls.py` to include the core app APIs.

3.  **Core App**:
    -   Created the `core` app.
    -   Implemented `models.py` with all requested entities and relationships, ensuring strict table naming with `academico_` prefix.
    -   Implemented `serializers.py` for all models.
    -   Implemented `views.py` with ViewSets for all models.
    -   Implemented `urls.py` with a DefaultRouter to expose the API.
    -   Configured `admin.py` to manage models in the Django Admin.

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
