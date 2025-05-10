from fastapi import FastAPI, HTTPException, Path
from typing import List, Dict, Union, Any
import time 
from .wind_config import windowSize,API_URL,valid_num_id

app = FastAPI()

#storage of data with window
store_num_window: List[int] = []



@app.get("/numbers/{number_id}")
async def get_num_api(
    number_id: str = Path(..., regex=f"^[{''.join(valid_num_id)}]$") #giving the req num regex
):
    #validation of got num id
    if number_id not in valid_num_id:
        raise HTTPException(status_code=400, detail="give correct number ID (Use {valid_num_id}).")

#set and sstore num
    return {
        "windowPrevState": [],
        "windowCurrState": [],
        "numbers": [],
        "avg": 0.0
    }
