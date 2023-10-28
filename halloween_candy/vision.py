import cv2

class Vision:
    
    
    
    def __init__(self):
        # Load the pre-trained Haar Cascade face detector
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Open a video capture object (0 is usually the default camera)
        self.cap = cv2.VideoCapture(0)

    def awaitFace(self):
        found = False
        while not found:
            # Read a frame from the video capture
            ret, frame = self.cap.read()

            if not ret:
                break

            # Convert the frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the frame
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Draw bounding boxes around detected faces
            for (x, y, w, h) in faces:
                found = w > 240 and h > 240
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                

            # Display the frame with bounding boxes
            cv2.imshow('Face Detection', frame)

            # Exit the loop when the 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
    def teardown(self):
        # Release the video capture and close the OpenCV window
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    vis = Vision()
    vis.awaitFace()
    vis.teardown()
    print("Done")
