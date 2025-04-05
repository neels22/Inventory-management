from fastapi import FastAPI,Path,Query,HTTPException
import uvicorn
from typing import List
from pydantic import BaseModel, Field
app = FastAPI()


# @app.get("/")
# async def root():
#    return {"message": "Hello World"}


# for path parameters
@app.get("/hello/{name}/{age}")
async def hello(*, name: str=Path(...,min_length=3 , max_length=10), age: int = Path(..., ge=1, le=100),percent:float = Query(...,ge=3,le=100)):
   return {"name": name, "age":age}
# for query parameters
@app.get("/hello")
async def root(name:str,age:int):
   return {"name":name,"age":age}


class Student(BaseModel):
   id:int
   name:str = Field(None,title="the name of student",max_length=10)
   subjects:List[str] = []

students = []

@app.post("/student/")
async def student_data(s1:Student):
    students.append(s1)

@app.get("/")
async def show_student():
   return students


@app.put("/student/{name}")
async def update_student(name:str,s2:Student):
   
   for student in students:
      if student.name == name:
         student = s2
         return student
   
   raise HTTPException(
      status_code=404,
      detail=f"student with {name} name doesnt exist"
   )
    
@app.delete("/student/{name}")
async def delete_student(name:str):
   
   for student in students:
      if student.name== name:
         return {"msg":"deleted"}
        
   raise HTTPException(
      status_code=404,
      detail=f"student with {name} name doesnt exist"
   )
    






if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)