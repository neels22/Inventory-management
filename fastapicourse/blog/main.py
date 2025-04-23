


from fastapi import FastAPI , status ,HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
from .schemas import Blog
from .database import engine
from . import models
from sqlalchemy.orm import Session
from .database import SessionLocal
from fastapi import Depends


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/blog",status_code=status.HTTP_201_CREATED)
def create_blog(request:Blog,db:Session = Depends(get_db)):
    new_blog = models.BlogModel(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete("/blog/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int, db:Session = Depends(get_db)):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id)
    if not blog.first():
        # return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Blog not found"})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.delete(synchronize_session=False)

    db.commit()
    return {"message": "Blog deleted successfully"}


@app.put("/blog/{id}",status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int, request:Blog, db:Session = Depends(get_db)):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id)
    if not blog.first():
        # return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Blog not found"})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.update(
        {
            "title": request.title,
            "body": request.body
        },
        synchronize_session=False
    )
    db.commit()
    return {"message": "Blog updated successfully"}






@app.get("/blog/")
def get_blogs(db:Session = Depends(get_db)):
    blogs = db.query(models.BlogModel).all()
    return blogs

@app.get("/blog/{id}",status_code=status.HTTP_200_OK)
def get_blog(id:int, db:Session = Depends(get_db)):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id).first()

    if not blog:
        # return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Blog not found"})
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")

    return blog

