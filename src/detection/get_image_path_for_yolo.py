import os

def extract_image_paths(directory):
    image_paths = []
    for file in os.listdir(directory):
        if file.lower().endswith(('.jpg', '.jpeg')):
            image_path = os.path.join(directory, file)
            image_paths.append(image_path)
    return image_paths

def save_paths_to_txt(image_paths, output_file):
    with open(output_file, 'w') as f:
        for path in image_paths:
            f.write(path + '\n')
    print(f"Image paths saved to {output_file}.")
    
# Directory to search for images
directory = '/home/hoangtv/data/Phong_Dat/aic23/detection/validation/images'

# Output file name
output_file = '/home/hoangtv/data/Phong_Dat/aic23/src/top2git/src/detection/synthetic.txt'

# Extract image paths
image_paths = extract_image_paths(directory)

# Save paths to a text file
save_paths_to_txt(image_paths, output_file)
