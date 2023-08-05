from fastapi import APIRouter

router = APIRouter(prefix='/users')

@router.get('/{id}')
def get_user(id: int):
    return {'id': id}

@router.post('/')
async def create_user():
    pass