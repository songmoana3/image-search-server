import torchvision.transforms as transforms
import torchvision.models as models
import torch

class FeatureExtractor:
    
    def __init__(self, img):
        self.img = img
        self.model = self.load_model()
        self.preprocess = self.set_preprocess()
    
    # 모델 로드
    def load_model(self):
        model = models.resnet18(pretrained=True)
        model.eval()
        return model

    # 이미지 전처리 설정
    def set_preprocess(self):

        preprocess = transforms.Compose([
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406], 
                std=[0.229, 0.224, 0.225]
            )
        ])
        return preprocess

    # feature 추출
    def extract_feature(self):
        
        with torch.no_grad():
            image = self.preprocess(self.img)
            image = image.unsqueeze(0)
            features = self.model(image)
        return features
