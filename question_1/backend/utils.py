# backend/app/utils.py

import httpx
import asyncio
from typing import List, Optional, Dict

from .wind_config import API_URL,max_res_time,BEARER_TOKEN


async def fetch_numbers_from_third_party(number_id: str) -> Optional[List[int]]:
  
    url = API_URL.get(number_id)
    if not url:
        print(f"Error: Invalid number_id '{number_id}' provided to fetch function.")
        return None

    timeout_seconds = max_res_time / 1000.0

    #header
    headers = {}
    if BEARER_TOKEN:
        headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    else:
        print("Warning: Third-party API Bearer Token is not set in config.")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=timeout_seconds, headers=headers)

            response.raise_for_status() # responce status

            data = response.json()
            if "numbers" in data and isinstance(data["numbers"], list):
                return [num for num in data["numbers"] if isinstance(num, int)]
            else:
                print(f"Warning: 'numbers' key not found or not a list in response from {url}. Data: {data}")
                return None

    except httpx.TimeoutException:
        print(f"Warning: Timeout occurred while fetching numbers from {url} for id '{number_id}'.")
        return None
    except httpx.HTTPStatusError as e:
        # Specifically log if it's an auth error
        if e.response.status_code == 401:
            print(f"Critical: Authentication failed {url}. The Bearer Token  invalid, expired, or missing.")
        elif e.response.status_code == 403:
            print(f"Critical: Forbidden {url}. The Bearer Token not  permissions.")
        else:
            print(f"Warning: HTTP error {e.response.status_code}fetching numbers from {url} for id '{number_id}'. Response: {e.response.text}")
        return None
    except httpx.RequestError as e:
        print(f"Warning: An error occurred while requesting {url}: {e}")
        return None
    except Exception as e:
        print(f"Warning: An unexpected error occurred while fetching numbers for id '{number_id}': {e}")
        return None