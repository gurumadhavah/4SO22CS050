#define window_size
windowSize: int = 10
max_res_time: int = 500 #responce time

valid_num_id = ['p', 'f', 'e', 'r']

#api url
BASE_URL = "http://20.244.56.144/evaluation-service"

API_URL = {
    "p": f"{BASE_URL}/primes",    # prime
    "f": f"{BASE_URL}/fibo",      # fibonacci
    "e": f"{BASE_URL}/even",      # even
    "r": f"{BASE_URL}/rand"       # random
}
