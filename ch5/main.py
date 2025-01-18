import cv2
import numpy as np
import tensorflow as tf

# Load the pre-trained MobileNetV2 model
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Function to preprocess the drawn image
def preprocess_image(image):
    # Resize the image to 224x224 (required by MobileNetV2)
    image = cv2.resize(image, (224, 224))
    image = np.expand_dims(image, axis=0)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    return image

# Function to make predictions
def predict(image):
    processed_image = preprocess_image(image)
    preds = model.predict(processed_image)
    decoded_preds = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0]
    return decoded_preds[0][1]  # Return the predicted class label

# Start capturing video (for drawing with mouse)
cap = cv2.VideoCapture(0)

# Create a black canvas for drawing
canvas = np.zeros((500, 500, 3), dtype="uint8")

# Variables to store drawing status
drawing = False
ix, iy = -1, -1

# Mouse callback function for drawing on canvas
def draw(event, x, y, flags, param):
    global ix, iy, drawing, canvas
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(canvas, (ix, iy), (x, y), (255, 255, 255), 10)
            ix, iy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # After drawing, process the image and predict
        object_name = predict(canvas)
        print("Predicted Object: ", object_name)
        cv2.putText(canvas, f"Predicted: {object_name}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

# Set up OpenCV window and mouse callback
cv2.namedWindow("Drawing")
cv2.setMouseCallback("Drawing", draw)

while True:
    # Display the canvas for drawing
    cv2.imshow("Drawing", canvas)
    
    # Listen for key press to clear the canvas
    key = cv2.waitKey(1) & 0xFF
    if key == ord("c"):  # Press 'c' to clear the canvas
        canvas = np.zeros((500, 500, 3), dtype="uint8")
    
    # Press 'q' to quit
    if key == ord("q"):
        break

# Cleanup
cv2.destroyAllWindows()
