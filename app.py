import streamlit as st
import cv2

st.title("SIGNAL")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    st.error("Error: Unable to open camera.")
else:
    st.info("Camera is open. Press 'q' to quit.")

    # Create a loop to continuously read frames from the camera
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Display the frame using Streamlit
        st.image(frame, channels="BGR")

        # Check if the user pressed 'q' to quit
        if st.button("Quit"):
            break

    # Release the VideoCapture object and close the Streamlit app
    cap.release()
    cv2.destroyAllWindows()
