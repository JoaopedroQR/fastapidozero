from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.routers import auth, todos, users
from fast_zero.schemas import Message

app = FastAPI(title='API JP')

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(todos.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
async def read_root():
    return {'message': 'Olá Mundo!'}


# @app.get('/', status_code=200)
# def read_root():
#     return {'message': 'Olá Mundo!'}
# @app.get('/', response_class=HTMLResponse)
# def read_root():
#     return """
#     <html>
#       <head>
#         <title> Nosso olá mundo!</title>
#       </head>
#       <body>
#         <h1> Olá Mundo </h1>
#       </body>
#     </html>"""
