from enum import Enum

class StatusExecution(Enum):
    PASS = "pass"
    FAIL = "fail"
    
class BotStatus(str, Enum):
    ACTIVATED = "activate"
    DISABLED = "disabled"