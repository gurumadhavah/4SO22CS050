from fastapi import FastAPI, HTTPException, Path
from typing import List, Dict, Union, Any
import time 

app = FastAPI()

#storage of data with window
store_num_window: List[int] = []

#config the win
windowSize = 10

@app.get("/numbers/{number_id}")
async def get_num_api(
    number_id: str = Path(..., regex="^[pfre]$") #giving the req num regex
):
    #validation of got num id
    if number_id not in ['p', 'f', 'e', 'r']:
        raise HTTPException(status_code=400, detail="Invalid number ID. Use 'p', 'f', 'e', or 'r'.")

#set and sstore num
    return {
        "windowPrevState": [],
        "windowCurrState": [],
        "numbers": [],
        "avg": 0.0
    }
