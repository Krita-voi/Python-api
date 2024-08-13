import  requests
import json

city=input("What city: ")
key='0aa1ca9dfd5b4cd7ba031329240808'
response =requests.get(f'http://api.weatherapi.com/v1/current.json?key={key}&q={city}')
if response.status_code == 200:
    response_content = response.content.decode('utf-8')
    
    # Load the string content as JSON
    data = json.loads(response_content)
    # Extract relevant information
    main = data['location']
    weather = data['current']['condition']['text']
    temperature = data['current']['temp_c']

    # Create a dictionary to hold the relevant weather information
    weather_data = {
        "city": city,
        "weather":weather,
        "temperature": temperature,
        
    }

    # Convert the dictionary to a JSON string with formatting
    weather_json = json.dumps(weather_data, indent=2)
    print(weather_json)
else:
    print(f"Error in the HTTP request: {response.status_code}")