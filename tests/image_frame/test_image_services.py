import pytest
from src.models.image_frame import ImageFrame
from src.services.image_frame_service import ImageService
from ..constants import Constants

def test_process_csv(db):
    with open("data/book1.csv") as file:
        image_service = ImageService()
        csv_data = file.readlines()
        file_id = image_service.process_csv(csv_data[0])
        assert isinstance(file_id, str)

def test_get_image_frames():
    image_service = ImageService()
    depth_min = 9000.1
    depth_max = 9000.2
    frames = image_service.get_image_frames(depth_min, depth_max,file_id=Constants.csv_file_id)
    assert isinstance(frames, list)
