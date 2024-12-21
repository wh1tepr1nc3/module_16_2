# uvicorn module_16_2:app --reload
# http://127.0.0.1:8000/docs
from fastapi import FastAPI, Path
from typing import Annotated
import anyio

app = FastAPI()


@app.get("/")
async def main_page() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def welcome_admin() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def get_main_page(
        user_id: Annotated[int, Path(gt=1,
                                     le=100,
                                     examples='1',
                                     title='User ID',
                                     description="Enter User ID")]) -> str:
    return f'Вы вошли как пользователь №: {user_id}'


@app.get("/user/{username}/{age}")
async def user_info(
        username: Annotated[str, Path(min_length=5,
                                      max_length=20,
                                      description='Enter username',
                                      examples='UrbanUser')],
        age: Annotated[int, Path(gt=18,
                                 le=120,
                                 description='Enter age',
                                 examples='24')]) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
