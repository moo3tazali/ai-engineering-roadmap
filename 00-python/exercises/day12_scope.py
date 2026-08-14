REQUEST_TIMEOUT = 30
retry_count = 0


def process_request(success):
    global retry_count
    if success:
        print("Request completed")
    else:
        retry_count += 1
        print(f"Request failed - retry {retry_count}")


process_request(False)
process_request(False)
process_request(True)

if retry_count > 0:
    status = "Retries occurred"

print(status)
print(f"Timeout: {REQUEST_TIMEOUT} seconds")
print(f"Total retries: {retry_count}")
