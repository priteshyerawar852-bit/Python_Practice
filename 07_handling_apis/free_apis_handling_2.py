import requests

def user_freeapi():
    url = https//jsonplaceholder.typicode.com/users
    
    responce = requests.get(url)
    data = responce.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        email = user_data["verify"]["email"]
        address = user_data["location"]["address"]
        
        return username,email,address
    else:
        raise Exception("failed to fetch user data")
    
    def main():
        try:
            username, email, address = user_freeapi()
            print(f"Username:{username}\nemail:{email}\naddress:{address}")
        except Exception as e:
            print(str(e))

    if __name__ == "__main__":
        main()

