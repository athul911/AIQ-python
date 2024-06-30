from ..constants import Constants

def test_upload_and_resize(client):
    with open("data/book1.csv", "rb") as file:
        response = client.post("/upload/", files={"file": file})
        response_json = response.json()
        file_id = response_json["file_id"]
    assert response.status_code == 200
    assert response.json() == {"status":"Images uploaded and resized successfully.","file_id":file_id}

def test_read_image_frames(client, db):
    depth_min = 9000.0
    depth_max = 9000.1
    response = client.get(f"/image_frames/?file_id={Constants.csv_file_id}&depth_min={depth_min}&depth_max={depth_max}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    colored_response = client.get(f"/image_frames/?file_id={Constants.csv_file_id}&depth_min={depth_min}&depth_max={depth_max}&colored=true")
    assert colored_response.status_code == 200
    assert isinstance(colored_response.json(), list)
