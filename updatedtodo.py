import requests
import json


def bikeList():
    response=requests.get("http://localhost:8090/api/collections/bike/records")
    if response.status_code == 200:
        response_content = response.content.decode('utf-8')
        data = json.loads(response_content)
        length = data["totalItems"]
        print(length)
        
        for x in range(length):
            name = data['items'][x]['name']
            brand = data['items'][x]['brand']
            cc = data['items'][x]['cc']
            price = data['items'][x]['price']
            id = data ['items'][x]['id']


            list ={
                "id" : id,
                "name" : name,
                "brand" : brand,
                "cc" : cc,
                "price" : price,
            }
            
            list_json = json.dumps(list,indent = 3 )
            print(list_json)
    else:
        print(f"Error in HTTPS while retriving bikes : {response.status_code}")
      
        
        
def creatBike():
    name = input("Enter the bike name: ")
    brand = input("Enter the bike brand: ")
    cc = input("Enter the bike cc: ")
    price = input("Enter the bike price: ")


    new_bike ={
        "name": name,
        "brand": brand,
        "cc": cc,
        "price": price
    }


    response = requests.post("http://localhost:8090/api/collections/bike/records", json=new_bike)

    if response.status_code == 200:
        print("Bike cretaed successfully ")   
        print(json.dumps(response.json(), indent=3))
    else:
        print(f"Error in the HTTP requests{response.status_code}")



def deleteBike():
    ename=input("Enter the name of bike you want to delete :")
    response_list=requests.get("http://localhost:8090/api/collections/bike/records")

    if response_list.status_code == 200:
        response_content = response_list.content.decode('utf-8')
        data = json.loads(response_content)
        length = data["totalItems"]
        
        for x in range(length):
            name = data['items'][x]['name']
            id = data['items'][x]['id']

            if ename == name:
                response = requests.delete(f"http://localhost:8090/api/collections/bike/records/{id}", json=name)
                if response.status_code == 204:
                    print("Bike deleted successfully ")   
                else:
                    print(f"Error in the HTTP requests{response.status_code}")
                break
            else:
                print("bike not found")
    else:
        print("Error in HTTPS while retriving bike ")
        

def updateBike():
    ename=input("Enter the name of bike you want to update :")
    response_list=requests.get("http://localhost:8090/api/collections/bike/records")

    if response_list.status_code == 200:
        response_content = response_list.content.decode('utf-8')
        data = json.loads(response_content)
        length = data["totalItems"]
    
        for x in range(length):
            name = data['items'][x]['name']
            id = data['items'][x]['id']

            if ename == name:
                name = input("Enter the bike name : ")
                brand = input("Enter the bike brand : ")
                cc = input("Enter the bike cc  : ")
                price = input("Enter the bike : ")

                list ={
                "name" : name,
                "brand" : brand,
                "cc" : cc,
                "price" : price,
            }
                
                response = requests.patch(f"http://localhost:8090/api/collections/bike/records/{id}", json=list)

                if response.status_code == 200:
                    print("Bike  successfully updated ")   
                else:
                    print(f"Error in the HTTP requests{response.status_code}")
                break
            else:
                print("Bike not found ")
    else:
        (f"Error in HTTPS while retriving bikes : {response.status_code}")


def menu():
    while True:
        print("\nMenu: ")
        print("1. List all bikes")
        print("2. Create a new bike")
        print("3. Update an existing bike")
        print("4. Delete a bike")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        switch = {
            '1': bikeList,
            '2': creatBike,
            '3': updateBike,
            '4': deleteBike,
            '5': exit
        }
        
        func = switch.get(choice, lambda: print("Invalid choice. Please select a valid option."))
        
        func()




if __name__ == "__main__":
    menu()
    
