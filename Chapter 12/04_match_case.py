# MATCH CASE

def https_status(status) :
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:         #default
            return "Unknown Error"
        
print(https_status(200))            #retun OK 
print(https_status(404))            #retun Not found
print(https_status(500))            #retun Internal Server Error
print(https_status(254))            #retun Unknown Error