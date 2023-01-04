
def generate_image(size_in_mb):
    # Calculate the number of pixels needed to generate an image of the desired size
    num_pixels = int(size_in_mb * 1024 * 1024 / 3)

    # Create a list of random pixel values
    pixels = [random.randint(0, 255) for _ in range(num_pixels)]
    

    # Create an image file with the random pixel values
    with open(f'{args.size}mb.jpg', 'wb') as f:
        f.write(bytearray(pixels))

parser = argparse.ArgumentParser()
parser.add_argument('--size', type=int, required=True, help='Size of the image in megabytes')
args = parser.parse_args()

# Generate an image with a file size of 1 MB
generate_image((3.2)*(args.size))

# Check the file size of the generated image
print(f'File size: {os.path.getsize(f"{args.size}mb.jpg") / 1024 / 1024} MB')
