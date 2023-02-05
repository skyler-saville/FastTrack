from fastapi import APIRouter, Response, Query, Path, Body, HTTPException
# pull in the _DB_ENGINE and the get_db_session from dbConnection
# each route should have a self-contained session() that gets closed after the query
from ..dbConnection import _DB_ENGINE, get_db_session
from ..models import User, user_punishments, user_chores, user_rewards

router = APIRouter(prefix="/users")

# create routes for USERS
#  TODO add routes for users (assign chores and manage points)
#  TODO create a postgres db to persist data


@router.get('/', tags=['users'])
async def all_users(res: Response):
    session = get_db_session(_DB_ENGINE)
    try:
        users = session.query(User).all()
        if users:
            res.status_code = 200
            return users
        else:
            res.status_code = 404
            return {'message': 'No users were found.'}
    finally:
        session.close()

@router.get('/{user_id}', tags=['users'])
async def getOneUser(res: Response, user_id: int = Path(..., title='the id of the user you looked for')):
    session = get_db_session(_DB_ENGINE)
    try:
        user = session.query(User).filter(User.user_id == user_id).first()
        if user:
            res.status_code = 200
            return user
        else:
            res.status_code = 404
            return {'message': f'No user with user_id={user_id} could be found.'}
    finally:
        session.close()

#  Update a User
@router.put("/{user_id}", tags=['users'])
async def update_user(
    user_id: int = Path(..., title="The ID of the user to update"),
    username: str = Body(..., title="The new username for the user"),
    email: str = Body(..., title="The new email for the user"),
    user_role: str = Body(..., title="The new role for the user")
):
    # Create a new session
    session = get_db_session(_DB_ENGINE)
    try:
        # Retrieve the user with the specified ID from the database
        user = session.query(User).filter(User.user_id == user_id).first()
        if user:
            # Update the user's information
            user.username = username
            user.email = email
            user.user_role = user_role
            session.commit()
            return {"message": "User updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    finally:
        # Close the session
        session.close()