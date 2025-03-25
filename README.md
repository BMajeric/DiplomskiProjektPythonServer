# DiplomskiProjektPythonServer
A simple Python server meant to act as an intermediary between the two apps in the [DigitalTween](https://github.com/BMajeric/DigitalTweenNreal) project.
## Description
A simple Python Flask server meant to receive data (GPS coordinates) from one app and enable another app to read it.
## Instalation and Setup
- Clone the repository containing the Flask server code
- Install dependencies
  ```
  pip install -r requirements.txt
  ```
- Run the server locally to check if it works (optional)
  ```
  python server.py
  ```
- Deploy server to Render (or any other hosting service) following their deployment instructions
## API Endpoints
1. POST /send
   - Receives data (GPS coordinates form a mobile app)
   - Request Body example (JSON):
     ```
     {
        "X": 45.812,
        "Z": 15.956
     }
     ```
   - Response example:
     ```
     {"message": "Location received!"}
     ```
2. GET /get
   - Gets last stored instance of data (NReal app pulls the GPS coordinates)
   - Response example:
     ```
     {
        "X": 45.812,
        "Z": 15.956
     }
     ```
