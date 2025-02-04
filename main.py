from fastapi import FastAPI
import pandas as pd

# Create API object
app = FastAPI()

# read dat
df = pd.read_csv('data.csv')

# Root Home API
@app.get("/")
def root():
    return {"message":"What to say...."}

# Endpoint greeting
@app.get("/name/{name}")

def greet(name):
    return {'message':f'Hai {name}, help me!'}

# Endpoint return data
@app.get("/data")

def get_data():
    return df.to_dict(orient='records')

# get data by id
@app.get('/data/{id}')

def search_data(id:int):
    result = df[df['id']==id]
    return {'result':result.to_dict(orient='records')}

# nambah data
'''Ceritanya ingin input data baru dimana data baru merupakan dictionary. Data baru ini ingin ditambahkan ke dictionary yang sudah ada'''
@app.post('/data/add')

def add_data(new_data:dict):
    global df
    
    new_row = pd.DataFrame([new_data])
    df = pd.concat([df, new_row], ignore_index=True)

    return {'message':df.to_dict(orient='records')}
