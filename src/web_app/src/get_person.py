import utils 
import os
import time
from color_utils import find_person_images
from color_catergory import COLOR

# Get person by color: DONE 
# Get person by default (show all): DONE
if __name__ == "__main__":
    scene = "S003"
    cfg, images, cam_person_infor, unique_person_id = utils._initialize("src/web_app/configs/app.yaml", scene)

    s = time.time()
    print("Finding person images...")
    find_person_images(unique_person_id, COLOR['GREEN'], 60, 3)
    e = time.time() 
    print("Done finding person images. Time:", e - s, "s")