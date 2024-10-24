from ultralytics import YOLO
def classify(image):
    model = YOLO("best.pt")
    results = model(source=image, save=False)
    for i in results:
        print(i.probs.top1) #класс обнаружения
        return i.probs.top1

classify('land.jpg')
