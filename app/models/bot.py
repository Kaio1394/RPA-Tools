from datetime import date
from app.models.enums import BotStatus

class Bot:
    uuid: str
    description: str
    status: BotStatus
    create_at: date
    update_at: date