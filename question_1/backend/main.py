from fastapi import FastAPI, HTTPException, Path, Response
from typing import List, Optional, Deque, Any # Added Any
from collections import deque

from .wind_config import windowSize, API_URL, valid_num_id, max_res_time
from .utils import fetch_numbers_from_third_party

from fastapi.middleware.cors import CORSMiddleware # Added for CORS

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000", 
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"], 
    allow_headers=["*"],
)


# storing num window
store_num_window: Deque[int] = deque(maxlen=windowSize)


@app.get("/numbers/{number_id}")
async def get_num_api(
    number_id: str = Path(..., regex=f"^[{''.join(valid_num_id)}]$")
) -> dict[str, Any]:
    if number_id not in valid_num_id:
        raise HTTPException(status_code=400, detail=f"give correct number ID (Use {valid_num_id}).")

    window_prev_state: List[int] = list(store_num_window)

    fetched_numbers_list: Optional[List[int]] = await fetch_numbers_from_third_party(number_id)

    numbers_from_server: List[int] = []
    if fetched_numbers_list is not None:
        numbers_from_server = fetched_numbers_list
    
    # fecth
    for num in numbers_from_server:
        if isinstance(num, int) and num not in store_num_window:
            store_num_window.append(num)  #store num
    
    window_curr_state: List[int] = list(store_num_window)
    
    avg_display: str = "0.00"
    if window_curr_state:
        current_avg_float = sum(window_curr_state) / len(window_curr_state)
        avg_display = f"{current_avg_float:.2f}"
    
    response_data = {
        "windowPrevState": window_prev_state,
        "windowCurrState": window_curr_state,
        "numbers": numbers_from_server,
        "avg": avg_display
    }
    return response_data