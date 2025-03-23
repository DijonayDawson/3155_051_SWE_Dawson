#Import TestClient to simulate API requests
from fastapi.testclient import testclient

#Import the FastAPI app istance from the controller module
from main import app

#Create a TestClient instamce for the FastAPI app
client = TestClient(app)

#Define a test function for  reading a specific sheep
def test_read_sheep():
    #Send a GET request to the endpoint "/sheep/1"
    response = client.get("/sheep/1")

    #Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    #Assert that the response JSON matches the expected data
    assert response.json () == {
        #Expected JSOn structure
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }