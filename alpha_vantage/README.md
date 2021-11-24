## ALPHA VANTAGE

### Introduction
This project fetches the latest currency exchange rate from Alpha vantage

### System requirements
1. Unix based OS
2. Docker and docker-compose installed

### Installation
1. Clone the repo
2. cd into ```alpha-vantage/alpha_vantage/```
3. To run the app, try:
```docker-compose up --build```

### How to use
You need an API Key to fetch the exchange rate from the app. To get the API Key, do a 
POST request to ,
```http://0.0.0.0:8000/api/v1/key```

The payload is,
```
{
    "email":"youremail"
}
```
To get the exchange rate, try a GET Or POST request to ,
```http://0.0.0.0:8000/api/v1/quotes```

Note: You need to pass the API Key to the quotes API in the header as,
```Api-Key <your-api-key>```
