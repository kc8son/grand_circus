from fastapi import FastAPI   #   a python class providing all API functionality
app = FastAPI()

#  Using a decorator...
#  Tell FastAPI that the function
@app.get("/")
async def root():

