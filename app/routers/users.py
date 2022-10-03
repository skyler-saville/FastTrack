from fastapi import APIRouter

router = APIRouter()

# create routes for USERS
#  TODO add routes for users (assign chores and manage points)
#  TODO create a postgres db to persist data

@router.get('/users', tags=['users'])
async def all_users():
    return[
        {"username":"Mickey"},
        {"username":"Goofy"},
        {"username":"Donald"}
        ]

@router.get('/users/{username}', tags=['users'])
async def get_user(username: str):
    return {"username": username}


@router.get('/users/me', tags=['users'])
async def get_current_user():
    return {"username":"current user"}