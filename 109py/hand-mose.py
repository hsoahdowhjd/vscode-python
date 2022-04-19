from ast import Global
from turtle import width
import cv2
import mediapipe as mp
from pynput.keyboard import Key, Controller
keyboard = Controller()

#cama =  1 + cv2.CAP_MSMF
cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
tipIds = [4, 8, 12, 16, 20]
global state
state=None
# Define a function to count fingers
def countFingers(image, hand_landmarks, handNo=0):
    if hand_landmarks:
        # Get all Landmarks of the FIRST Hand VISIBLE
        landmarks = hand_landmarks[handNo].landmark

        # Count Fingers        
        fingers = []

        for lm_index in tipIds:
                # Get Finger Tip and Bottom y Position Value
                finger_tip_y = landmarks[lm_index].y 
                finger_bottom_y = landmarks[lm_index - 2].y

                # Check if ANY FINGER is OPEN or CLOSED
                if lm_index !=4:
                    if finger_tip_y < finger_bottom_y:
                        fingers.append(1)
                        # print("FINGER with id ",lm_index," is Open")

                    if finger_tip_y > finger_bottom_y:
                        fingers.append(0)
                        # print("FINGER with id ",lm_index," is Closed")

        totalFingers = fingers.count(1)
        
        # PLAY or PAUSE a Video
        
        if totalFingers == 4:
            state="Play"
        if totalFingers == 0 and state == "Play":
            state="Pause"
            keyboard.press(Key.space)
        
        finger_tip_x = landmarks[8].x 
        finger_bottom_x = landmarks[5].x

         # Move Video FORWARD & BACKWARDS 
         
        if totalFingers==1:
            if finger_tip_x < finger_bottom_x:
                print("bacward")
                keyboard.press(Key.left)
            if finger_tip_x > finger_bottom_x:
                print("forward")
                keyboard.press(Key.right)
        
# Define a function to 
def drawHandLanmarks(image, hand_landmarks):

    # Darw connections between landmark points
    if hand_landmarks:

      for landmarks in hand_landmarks:
               
        mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)



while True:
    success, image = cap.read()

    image = cv2.flip(image, 1)
    
    # Detect the Hands Landmarks 
    results = hands.process(image)

    # Get landmark position from the processed result
    hand_landmarks = results.multi_hand_landmarks

    # Draw Landmarks
    drawHandLanmarks(image, hand_landmarks)

    # Get Hand Fingers Position        
    countFingers(image, hand_landmarks)

    cv2.imshow("Media Controller", image)

    # Quit the window on pressing Sapcebar key
    key = cv2.waitKey(1)
    if key == 66:
        break

cv2.destroyAllWindows()