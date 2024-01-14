import os
import sys
from PIL import Image

def create_gif(input_folder, output_folder, gif_name, duration):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get all image files from the input folder
    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    image_files.sort()  # Sort files if needed

    # Temporary list to store converted images
    converted_images = []

    for image_file in image_files:
        try:
            with Image.open(os.path.join(input_folder, image_file)) as img:
                # Convert image to PNG and store in memory
                img_converted = img.convert('RGBA')
                converted_images.append(img_converted)
        except IOError as e:
            print(f"Skipping file {image_file} due to error: {e}")

    # Check if any images were loaded and converted
    if not converted_images:
        print("No valid images found to create GIF.")
        return

    # Save as GIF
    gif_path = os.path.join(output_folder, gif_name)
    converted_images[0].save(gif_path, save_all=True, append_images=converted_images[1:], duration=duration, loop=0)
    print(f"GIF saved at {gif_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_folder> <output_folder> <duration_ms>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    duration = int(sys.argv[3])

    gif_name = "output.gif"
    create_gif(input_folder, output_folder, gif_name, duration)
