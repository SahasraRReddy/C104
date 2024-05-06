import cv2
img = cv2.imread("solar-system.jpg")

#Sun
cv2.putText(img,
            "Sun",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )

#Mercury
cv2.putText(img,
            "Mercury",
            (120,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255)
            )

#Venus
cv2.putText(img,
            "Venus",
            (200,255),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255)
            )

#Earth
cv2.putText(img,
            "Earth",
            (290,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255)
            )

#Moon
cv2.putText(img,
            "Moon",
            (340,150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255)
            )

#Mars
cv2.putText(img,
            "Mars",
            (386,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255)
            )

#Jupiter
cv2.putText(img,
            "Jupiter",
            (575,370),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255)
            )

#Saturn
cv2.putText(img,
            "Saturn",
            (773,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255)
            )

#Uranus
cv2.putText(img,
            "Uranus",
            (971,287),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255)
            )

#Neptune
cv2.putText(img,
            "Neptune",
            (1120,286),
            cv2.FONT_HERSHEY_COMPLEX,
            0.35,
            (255,255,255)
            )

cv2.imshow("output",img)

cv2.waitKey(0)




