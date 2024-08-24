def OddEven(num):
    match num%2:
        case 0:
            print("Num is even.")
        case _: #If doesn't match any value above then this is executed.
            print("Num is odd.")

OddEven(0)


def http_status(status): 
    match status: 
        case 200: 
            return "OK" 
        case 404: 
            return "Not Found" 
        case 500: 
            return "Internal Server Error" 
        case _: 
            return "Unknown status" 

print(http_status(200))  # Output: OK 
print(http_status(404))  # Output: Not Found 
print(http_status(500))  # Output: Internal Server Error 
print(http_status(403))  # Output: Unknown status   