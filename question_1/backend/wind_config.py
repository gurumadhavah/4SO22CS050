windowSize: int = 10
max_res_time: int = 500 # milliseconds

BASE_URL = "http://20.244.56.144/evaluation-service" # Keep this if it's still the base
API_URL = {
    "p": f"{BASE_URL}/primes",
    "f": f"{BASE_URL}/fibo",
    "e": f"{BASE_URL}/even",
    "r": f"{BASE_URL}/rand"
}
valid_num_id = ['p', 'f', 'e', 'r']

#barriertocken
BEARER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzQ2ODc3NDM0LCJpYXQiOjE3NDY4NzcxMzQsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjczYzczNTE3LWQ3N2ItNGY1ZC04YzgwLWY2YzRlMjViMWE3NyIsInN1YiI6IjIyYTUwLmd1cnVtYWRoYXZhQHNqZWMuYWMuaW4ifSwiZW1haWwiOiIyMmE1MC5ndXJ1bWFkaGF2YUBzamVjLmFjLmluIiwibmFtZSI6Imd1cnVtYWRoYXZhIGgiLCJyb2xsTm8iOiI0c28yMmNzMDUwIiwiYWNjZXNzQ29kZSI6IktqSkF4UCIsImNsaWVudElEIjoiNzNjNzM1MTctZDc3Yi00ZjVkLThjODAtZjZjNGUyNWIxYTc3IiwiY2xpZW50U2VjcmV0IjoiV0VCcXZaZkpoalNRbVRQUSJ9.kdyE2CllVHxGTX-xGiFHnlyFdHUeIdnvoT5STrmTFjA"