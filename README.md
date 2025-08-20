# 🤖 Bot Metrics & RPA Assistant API

This is a **FastAPI-based backend** designed to assist with:

- Collecting and exposing metrics from RPA (Robotic Process Automation) bots
- Providing a standardized API structure to support bot development and integration
- Serving as a lightweight backend tool to enhance observability in bot workflows

---

## 📌 Goals

- Help developers structure their bots with consistent API interactions
- Store and expose performance data such as execution time, result status, logs, etc.
- Serve as a backend base for future extensions (e.g., orchestration, dashboards, task management)

---

## 🚀 Tech Stack

- **FastAPI** — High-performance web framework
- **SQLAlchemy** — ORM for database models
- **Alembic** — For migrations
- **Sqlite** (or any SQL database)
- **Uvicorn** — ASGI server

---

## 📁 Project Structure

```bash
├── app/
│ ├── main.py # FastAPI app entry point
│ ├── api/ # API versioning and route definitions
│ │ └── v1/
│ │ └── endpoints/
│ │ └── routes.py
│ ├── constants/ # Constant values and path configs
│ │ └── paths.py
│ ├── core/ # Core configurations (e.g., DB)
│ │ └── database.py
│ ├── models/ # SQLAlchemy models and enums
│ │ ├── bot.py
│ │ ├── enums.py
│ │ ├── history_execution.py
│ │ └── rpa_project.py
│ ├── repositories/ # Data access logic (CRUD)
│ │ └── init.py
│ ├── services/ # Business logic and services
│ │ └── tools_service.py
│ └── utils/ # Utility modules for file operations
│ ├── excel_utils.py
│ └── file_utils.py
└── venv/