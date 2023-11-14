import cv2
import numpy as np

class FeatureExtractor:
    
    def __init__(self, img):
        self.img = img
    
    def extract_feature(self):
        # SIFT 객체 생성
        sift = cv2.SIFT_create()
        
        # numpy 객체로 변경
        self.img = np.array(self.img)
        
        # 특징점 추출
        keypoints, _ = sift.detectAndCompute(self.img, None)

        return keypoints