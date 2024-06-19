import os
import subprocess
import shutil

def optimize_images(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        # Create corresponding output directory
        relative_path = os.path.relpath(root, input_dir)
        output_root = os.path.join(output_dir, relative_path)
        os.makedirs(output_root, exist_ok=True)

        for file in files:
            file_path = os.path.join(root, file)
            output_path = os.path.join(output_root, file)

            if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg'):
                # Copy original file to output directory
                shutil.copy(file_path, output_path)
                # Optimize the image in the output directory
                subprocess.run(['jpegoptim', '--strip-all', output_path])
            elif file.lower().endswith('.png'):
                # Copy original file to output directory
                shutil.copy(file_path, output_path)
                # Optimize the image in the output directory
                subprocess.run(['optipng', output_path])
            else:
                # For non-image files, just copy them to the output directory
                shutil.copy(file_path, output_path)

input_directory = './public/images-pre/'
output_directory = './public/images/'

optimize_images(input_directory, output_directory)
