from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_token_header

from ..dbConnection import _DB_ENGINE, get_db_session
from ..models import Chore, user_punishments, user_chores, user_rewards

router = APIRouter(
    prefix='/chores',
    tags=['items'],
    dependencies=[Depends(get_token_header)],  # Requires 'fake-token' in the header, before providing access
    responses={404: {"description": "Not Found"}}
)

fake_chores_db = {
    "somerandomeid": {"name":"dishes", "description":"wash dishes", "value":5, "updated_on":None},
    "anotherrandomeid": {"name":"laundry", "description":"fold laundry", "value":5, "updated_on":None},
    "norandomid": {"name":"room", "description":"clean room", "value":5, "updated_on":None},
    "yetanotherid": {"name":"vacuum", "description":"vacuum house", "value":5, "updated_on":None}
}

# create routes for CHORES
#  TODO make routes for chores (earn points)

# /chores/
@router.get('/')
async def get_chores():
    session = get_db_session(_DB_ENGINE)
    chores = session.query(Chore).all()
    session.close()
    return chores

@router.get('/{item_id}')
async def get_chore(item_id: str):
    if item_id not in fake_chores_db:
        raise HTTPException(status_code=404, detail='Item not found')
    return fake_chores_db[item_id]

@router.put('/{item_id}', tags=['custom'], responses={403: {"description": "Operation Forbidden"}})
async def update_chore(item_id: str):
    if item_id not in fake_chores_db:
        raise HTTPException(status_code=404, detail="Cannot update item that does not exist")
    # update the timestamp for the specific id
    fake_chores_db[item_id].update({"updated_on": datetime.now()})
    return {"message": "updated item successfully", "item":fake_chores_db[item_id]}