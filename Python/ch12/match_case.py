def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Not found"
        case 500:
            return "Internal server error"
        case _:
            return "Unknown status"
        
n=int(input("Enter: "))

print(http_status(n))