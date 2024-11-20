import os
from PIL import Image


def crop_images(input_dir, output_dir):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get a list of all image files in the input directory
    image_files = [
        f
        for f in os.listdir(input_dir)
        if f.endswith((".jpg", ".jpeg", ".png", ".gif"))
    ]

    for image_file in image_files:
        input_path = os.path.join(input_dir, image_file)
        output_path = os.path.join(output_dir, image_file)

        # Open image
        with Image.open(input_path) as img:
            width, height = img.size
            # Calculate left, upper, right, lower coordinates for cropping
            # 1920 x 1080 settings
            left =  172
            upper = 55
            right = width - 126
            lower = height - 82

            # 1280 x 720 settings
            # left =  138
            # upper = 44
            # right = width - 100
            # lower = height - 65
            # Crop image
            cropped_img = img.crop((left, upper, right, lower))
            # Save cropped image
            cropped_img.save(output_path)


if __name__ == "__main__":
    # Input directory containing images
    input_directory = "images"
    # Output directory to save cropped images
    output_directory = "cropped_images"
    # Specify crop width and height
    crop_width = 1333
    crop_height = 750
    # Crop images
    crop_images(input_directory, output_directory)
    print("All images cropped successfully.")
