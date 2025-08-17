from datetime import date
from app.models.enums import StatusExecution

class HistoryExecution:
    uuid: str
    status: StatusExecution
    execute_at: date