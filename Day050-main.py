################################################################################
#
#   Date Written: 06/26/2023        By: Jose    ph P. Merten
#   This script is for the first API assignment:
#       https://lms.grandcircus.co/mod/assign/view.php?id=25417
#       https://docs.google.com/document/d/1Cn8NDfvAPV8ZVxwiagm2Je21SqvZDI8Pjfc_bxDVPQc/preview
#
#   This is a good tutorial:
#       https://fastapi.tiangolo.com/tutorial/first-steps/
#
#   Youtube videos:
#       https://youtu.be/F43rgxq4CKw
#
#   This is the random fact API service.
#   It uses facts.csv
#
#   To start the service run this command:
#       uvicorn Day051-API:app --reload
#       uvicorn main:app --reload
#                ^    ^--- Variable name of the FastApi() instance.
#                +--- Name of the python file to run.
#
#   Standard docs with FastApi:
#       http://127.0.0.1:8000/docs
#       http://127.0.0.1:8000/redoc
#       http://127.0.0.1:8000/openapi.json
#
# Build Specifications
#   ✓ Successfully able to launch backend server from main.py file (1 Point)
#   ✓ Users can successfully make a GET request to the specified endpoint (1 Point)
#   ✓ Each API call returns a random fact from your list of facts (1 Point)
#   ✓ Name the endpoint something that is representative of its task (1 Point)
#   ✓ List of facts are stored in a text file in your server directory (1 Point)
#   ✓ Correctly reading data from text file into Python (1 Point)
#   ✓ Index query parameter that allows the user to denote the specific fact they want returned by the index location of the fact (2 Points)
#   ✓ Logical naming of variables and endpoints and code legibility (2 Points)
# Extra Challenges:
#   ✓ Extend your API with a new endpoint to allow users to add new facts (i.e. /add). The new fact should be appended to the text file storing each fact. (2 Points)
#
################################################################################
#   imports...
import random
import csv
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

################################################################################
#   Load up our random facts...
csv_file = "./facts.csv"
fact_list = []
with open(csv_file, 'r') as in_file:
    reader = csv.reader(in_file, delimiter=',', quotechar='"')
    for row in reader:
        fact_list.append(row[0])
print(fact_list)

################################################################################
#   create an API instance.
app = FastAPI() # create an instance of FastApi

################################################################################
#   Structure to add a fact...
class Fact(BaseModel):
    new_fact: str

################################################################################
#  ROOT GET...
@app.get("/")   # Create a decorator for the root with a GET request
async def root():
    return {"message": "Hello World"}

################################################################################
#  fact GET
@app.get("/fact/")  #   Send the requester a joke
async def fact():
    idx = random.randint(0, len(fact_list)-1)
    return {"random_fact": f"Index:{idx} - {fact_list[idx]}"}

################################################################################
#  idx GET
@app.get("/fact/{idx}")  #   Send the requester a specific joke
async def fact(idx):
    return {"random_fact": f"Index:{idx} - {fact_list[int(idx)]}"}

################################################################################
#  fact POST
#  Remember that the new_fact property is part of the new_fact object.
@app.post("/add/")  #   Add a new fact
async def add(new_fact: Fact):
    fact_list.append(new_fact.new_fact)
    # Write CSV file
    with open(csv_file, "w", newline='\n') as out_file:
        writer = csv.writer(out_file, delimiter=',', lineterminator='\n', quotechar='\"')
        for fact in fact_list:
            # print(fact)
            writer.writerows([[fact]])
    return {"random_fact": f"Index: {len(fact_list)} - {new_fact}"}


