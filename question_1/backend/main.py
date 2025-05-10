from fastapi import FastAPI, HTTPException, Path
from typing import List, Optional 
import time 

from .wind_config import windowSize, API_URL, valid_num_id, max_res_time
from .utils import fetch_numbers_from_third_party

app = FastAPI()

store_num_window: List[int] = []

@app.get("/numbers/{number_id}")
async def get_num_api(
    number_id: str = Path(..., regex=f"^[{''.join(valid_num_id)}]$")
):
    if number_id not in valid_num_id:
        raise HTTPException(status_code=400, detail=f"give correct number ID (Use {valid_num_id}).")

    window_prev_state: List[int] = list(store_num_window)

    fetched_numbers_list: Optional[List[int]] = await fetch_numbers_from_third_party(number_id)

    numbers_from_server: List[int] = []
    if fetched_numbers_list is not None:
        numbers_from_server = fetched_numbers_list
    
    
    window_curr_state: List[int] = list(store_num_window)
    current_avg: float = 0.0
    

    return {
        "windowPrevState": window_prev_state,
        "windowCurrState": window_curr_state, # Will be updated in Step 5
        "numbers": numbers_from_server,       # <<< CORRECTED: Use numbers_from_server
        "avg": round(current_avg, 2) if current_avg else 0.0
    }