from fastapi import APIRouter

router = APIRouter()

# create routes for USERS
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