from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database, models, schemas, auth

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/")
def create_todo(
    todo: schemas.TodoCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    new_todo = models.Todo(
        title=todo.title,
        description=todo.description,
        user_id=current_user.id,
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@router.get("/")
def get_user_todos(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    return db.query(models.Todo).filter(
        models.Todo.user_id == current_user.id
    ).all()