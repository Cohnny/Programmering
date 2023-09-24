import json
import time
import sys


# Function that tries to read JSON data.
def read_data(path):
    try:
        with open(path, "r") as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        return False


# Loop that tries to load JSON data. If it fails it will retry a set amount of times before telling the user
# to restart the application.
def load_data(path):
    max_retries = 3
    retry_delay = 2

    retry_count = 0

    while retry_count < max_retries:
        data = read_data(path)
        if data:
            print(f"JSON read successfully.")
            return data
        else:
            retry_count += 1
            if retry_count < max_retries:
                print(f"Failed to get JSON data, retrying in {retry_delay} seconds. Retries: {retry_count}.")
                time.sleep(retry_delay)
            else:
                print(f"Failed to load JSON data after {retry_count}. Please restart the application.")
                time.sleep(2)
                sys.exit()
