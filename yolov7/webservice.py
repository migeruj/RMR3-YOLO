import torch
import base64
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from pydantic import BaseModel
from typing import List
from matplotlib import font_manager
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
origins = [
    "*"
    # If your frontend runs on a different port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

class Body(BaseModel):
    img: str


class Detection(BaseModel):
    class_name: str
    color: str
    prob: float

class BodyResponse(BaseModel):
    img: str
    detected: List[Detection]


model = torch.hub.load('E:/proyectos/master/TFM/Data_Converted/yolov7','custom', path_or_model='runs/train/manifestaciones-rupestres/weights/best.pt',force_reload=True,source='local')
class_names = ['Amolador','BateaMetate','Cupula','Dolmen','Esfera Litica','Geoglifo','Menhir','Micropetroglifo','Monolito','Petroglifo','Pintura Rupestre']
colors = ["red", "green", "blue", "orange", "purple", "pink", "cyan", "magenta", "yellow", "teal", "indigo"]

system_fonts = font_manager.get_font_names()

# Convert Image to Base64
def im_2_b64(image):
    buff = BytesIO()
    image.save(buff, format="JPEG")
    img_str = base64.b64encode(buff.getvalue())
    return img_str

@app.post("/")
def predict_image(data: Body) -> BodyResponse:
    """
    :param data: img should be a jpeg base64 encoded string
    :return: a jpeg base64 encoded string
    """

    if data.img!='null':

        # Load the image for inference
        base64_str: bytes = base64.b64decode(data.img)
        image = Image.open(BytesIO(base64_str))

        # Perform inference with the loaded YOLOv7 model
        results = model(image)

        # The 'results' variable contains the detected objects and their information.
        # You can access the detected bounding boxes, confidence scores, and class labels as follows:
        detected_boxes = results.pred[0][:, :4]  # Bounding boxes (x1, y1, x2, y2)
        confidence_scores = results.pred[0][:, 4]  # Confidence scores
        class_labels = results.pred[0][:, 5]  # Class labels

        # Create a drawing context
        draw = ImageDraw.Draw(image)
        draw.font = ImageFont.truetype("C:/Windows/Fonts/Georgia.ttf",35)

        # Set a threshold for confidence scores to filter out weak detections
        confidence_threshold = 0.35
        # Loop through the detected objects and draw bounding boxes
        detections = []
        for box, score, label in zip(detected_boxes, confidence_scores, class_labels):
            if score > confidence_threshold:
                x1, y1, x2, y2 = box.tolist()
                pos = int(label)
                # Draw a bounding box on the image
                draw.rectangle([x1, y1, x2, y2], outline=colors[pos], width=9)
                # Add label text
                label_text = f"{class_names[pos]}: {score:.2f}"
                detection = Detection(class_name=class_names[pos],color=colors[pos],prob=float(score))
                detections.append(detection)
                draw.text((x1, y1 - 40), label_text, fill=colors[pos], align='center')
        encoded = im_2_b64(image)

        image.close()

        response = BodyResponse(img=encoded, detected=detections)

        return response

    return JSONResponse(status_code=400,content="Image can't be null")
