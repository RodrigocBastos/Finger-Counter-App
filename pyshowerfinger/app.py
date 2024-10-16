import cv2
import mediapipe as mp

# Initialize MediaPipe Hands.
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Open a connection to the webcam.
cap = cv2.VideoCapture(0)

# Finger tip landmarks as per MediaPipe documentation.
finger_tips = [8, 12, 16, 20]
thumb_tip = 4

while True:
    success, img = cap.read()
    if not success:
        break

    # Flip the image horizontally for a mirror-like effect.
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the image and detect hand landmarks.
    results = hands.process(img_rgb)

    finger_count = 0  # Initialize finger count.

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm_list = []  # List to hold all landmark positions.

            # Extract landmark positions.
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = img.shape
                lm_list.append((id, int(lm.x * w), int(lm.y * h)))

            # Check if hand is facing palm side.
            if lm_list[0][1] < lm_list[9][1]:
                # Thumb.
                if lm_list[thumb_tip][1] > lm_list[thumb_tip - 2][1]:
                    finger_count += 1
                # Other fingers.
                for tip in finger_tips:
                    if lm_list[tip][2] < lm_list[tip - 2][2]:
                        finger_count += 1
            else:
                # Thumb.
                if lm_list[thumb_tip][1] < lm_list[thumb_tip - 2][1]:
                    finger_count += 1
                # Other fingers.
                for tip in finger_tips:
                    if lm_list[tip][2] < lm_list[tip - 2][2]:
                        finger_count += 1

            # Draw hand landmarks.
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the finger count.
    cv2.putText(img, f'Fingers Up: {finger_count}', (20, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)

    # Show the image.
    cv2.imshow("Finger Counter", img)

    # Exit on pressing 'q'.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources.
cap.release()
cv2.destroyAllWindows()
