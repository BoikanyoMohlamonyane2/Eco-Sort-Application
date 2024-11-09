import cv2
import numpy as np
from model import preprocess_image, model, labels

def capture_until_object_detected(target_label, details_label):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    center_x, center_y = frame_width // 2, frame_height // 2

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            cap.release()
            return None

        input_image = preprocess_image(frame)
        predictions = model(input_image)
        predicted_class = np.argmax(predictions[0])
        predicted_label = labels[predicted_class]

        if target_label.lower() in predicted_label.lower():
            details_label.config(text=f"{predicted_label} detected. Please dispose in Bin 1.")
            details_label.after(8000, lambda: details_label.config(text=""))  # Clear after 8 seconds

            cap.release()
            cv2.destroyAllWindows()
            return

        cv2.imshow('Object Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
