import requests

#56

ENDPOINT = "http://localhost:5000/api/v1/resources/output_php?model=m1"

def test_data_model_1():
	response = requests.get(ENDPOINT)
	data = response.json()

	assert len(data) == 489
	assert data[0][2] == ""
	assert response.status_code == 200

	pass