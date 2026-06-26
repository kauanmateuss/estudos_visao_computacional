import torch

from torchvision import models, transforms
from PIL import Image

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# carregando a imagem 
image = Image.open("./pytorch/pretrained_models_for_image_classification/dog.jpg")

# aplicando transformações na imagem e adicionando uma dimensão no batch
image_t = transform(image)

batch_t = torch.unsqueeze(image_t, 0)

# Carregando o modelo pre treinado resnet
resnet = models.resnet101(pretrained=True) # 101 é o número de camadas do modelo resnet

print(resnet)

# Colocando o modelo em modo de avaliação
resnet.eval()

