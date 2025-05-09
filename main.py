import cv2
import mediapipe as mp
import pygame

# MediaPipe başlat
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Ses sistemi başlat
pygame.mixer.init()
pygame.mixer.music.load("uyari.wav")

# Kamera başlat
cap = cv2.VideoCapture(0)

def goz_odakta_mi(landmarks, w, h):
    try:
        # Sol göz iris ve kenarlar
        lix = int(landmarks[468].x * w)
        liy = int(landmarks[468].y * h)
        lo = int(landmarks[33].x * w)
        li = int(landmarks[133].x * w)
        lt = int(landmarks[159].y * h)
        lb = int(landmarks[145].y * h)

        # Sağ göz iris ve kenarlar
        rix = int(landmarks[473].x * w)
        riy = int(landmarks[473].y * h)
        ro = int(landmarks[362].x * w)
        ri = int(landmarks[263].x * w)
        rt = int(landmarks[386].y * h)
        rb = int(landmarks[374].y * h)

        # Merkezler
        lxc = (lo + li) // 2
        lyc = (lt + lb) // 2
        rxc = (ro + ri) // 2
        ryc = (rt + rb) // 2

        # Yatay tolerans
        tol_x = 7
        if abs(lix - lxc) > tol_x or abs(rix - rxc) > tol_x:
            return False

        # Dikey tolerans — oran bazlı kontrol
        l_ratio = (liy - lt) / (lb - lt + 1e-6)
        r_ratio = (riy - rt) / (rb - rt + 1e-6)

        if not (0.35 <= l_ratio <= 0.65) or not (0.35 <= r_ratio <= 0.65):
            return False

        return True

    except:
        return False  # Göz algılanamıyorsa da odakta değil say

while True:
    success, frame = cap.read()
    if not success:
        break

    h, w = frame.shape[:2]
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    odakta = False

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            odakta = goz_odakta_mi(face_landmarks.landmark, w, h)

    if not odakta:
        cv2.putText(frame, "Dikkatin dagildi!", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)  # döngüde çalsın
    else:
        cv2.putText(frame, "Odakta", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

    cv2.imshow("Goz Takibi - Final Sürüm", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
