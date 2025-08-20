from fastapi import APIRouter
import logging

router = APIRouter()
logger = logging.getLogger(__name__)
logger.propagate = True 

@router.get("/bot")
async def get_bot_information():
    logger.info("Request recieved.")
    return {"teste": "teste1"}