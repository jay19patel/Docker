# Build the image
docker build -t my-test1 .

# Run the container
docker run -p 8000:8000 my-test1
