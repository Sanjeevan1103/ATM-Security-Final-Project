import cv2

# Initialize the camera (use 0 for the default camera, or specify the camera's index)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not access the camera.")
else:
    # Capture a single frame from the camera
    ret, frame = camera.read()

    if ret:
        # Save the captured frame to a file (you can change the file format and filename)
        image_filename = "captured_image.jpg"
        cv2.imwrite(image_filename, frame)
        print(f"Image saved as {image_filename}")

        # Release the camera
        camera.release()

    else:
        print("Error: Failed to capture a frame.")

# Close all OpenCV windows
cv2.destroyAllWindows()