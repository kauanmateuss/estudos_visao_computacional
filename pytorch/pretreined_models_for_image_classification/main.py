import torch

from torchvision import models, transforms
from PIL import Image

# print all available pretrained models in torchvision
#print(dir(models))

# Step 1: Load a pretrained model
alexnet = models.alexnet(pretrained=True)   # alexnet with pretrained weights

# details of the model
#print(alexnet)

# Step 2: Specify image transformations
transform = transforms.Compose([
    transforms.Resize(265),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Step 3: Load the input image and pre-process it
image = Image.open("./pytorch/pretreined_models_for_image_classification/dog.jpg")

image_t = transform(image) # Apply the transformations
batch_t = torch.unsqueeze(image_t, 0) # add a batch dimension

# Step 4: Model inference
alexnet.eval() # Set the model to evaluation mode
out = alexnet(batch_t) 

#print(out.shape) # Output shape: [1, 1000] (batch size, number of classes)

# Pegando as classes da imageNet 
with open("./pytorch/pretreined_models_for_image_classification/imagenet_classes.txt") as f:
    classes = [line.strip() for line in f.readlines()]

_, indeces = torch.sort(out, descending=True)

percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100 # Obtendo a porcentagem de confiança para cada classe

print(classes[indeces[0]], percentage[indeces[0]].item())