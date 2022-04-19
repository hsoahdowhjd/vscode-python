# import the opencv library
import cv2
import numpy as np
import tensorflow as tf
model = tf.keras.models.load_model('keras_model.h5')

cama =  1 + cv2.CAP_MSMF

# define a video capture object
vid = cv2.VideoCapture(cama)
  
while(True):
      
    # Capture the video frame by frame
    ret, frame = vid.read()
    
    img=cv2.resize(frame,(224,224))
    
    test_image = np.array(img, dtype=np.float32) 
    test_image = np.expand_dims(test_image, axis=0) 
    
    # 3. Normalizing the image 
    normalised_image = test_image/255.0 
    
    # Predict Result 
    prediction = model.predict(normalised_image) 
    print("Prediction : ", prediction)
    
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # Quit window with spacebar
    key = cv2.waitKey(1)
    
    if key == 32:
        break
  
# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()