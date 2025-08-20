import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

from app.api.v1.endpoints.bot_routes import router as bot_router
from fastapi import FastAPI
from app.utils import FileUtils

app = FastAPI()
app.include_router(bot_router)



if '__main__' == __name__:
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
    