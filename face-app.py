import streamlit as st
import io
import requests
import json
from PIL import Image
from PIL import ImageDraw

st.title('顔認識アプリ')

with open('secret.face.json') as f:
    secret_json = json.load(f)

subscription_key = secret_json["SUBSCRIPTION_KEY"]
assert subscription_key

face_api_url = 'https://20210813spiderkame.cognitiveservices.azure.com/face/v1.0/detect'


uploaded_file = st.file_uploader("Choose an image...", type='jpg')
if uploaded_file is not None:
  img = Image.open(uploaded_file)
  with io.BytesIO() as output:
      img.save(output, format="JPEG")
      binary_img = output.getvalue()
  headers = {
      'Content-Type': 'application/octet-stream',
      'Ocp-Apim-Subscription-Key': subscription_key
  }
  params = {
      'returnFaceId': 'true',
      'returnFaceLandmarks': 'false',
      'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
  }

  res= requests.post(face_api_url, params=params, headers=headers, data=binary_img)
  results = res.json()

  for result in results:
      rect = result['faceRectangle']

      at_rect = result['faceAttributes']
      gender = at_rect['gender']
      age = at_rect['age']
      smile = at_rect['smile']

      draw = ImageDraw.Draw(img)
      draw.rectangle([(rect['left'], rect['top']), (rect['left']+rect['width'],rect['top']+rect['height'])], fill=None, outline='green', width=5)
      draw.text([(45+rect['left'], 10+rect['top']+rect['height'])],gender)
      draw.text([(rect['left'], 10+rect['top']+rect['height'])],'gender:')
      draw.text([(30+rect['left'], 20+rect['top']+rect['height'])],str(age))
      draw.text([(rect['left'], 20+rect['top']+rect['height'])],'age:')
      draw.text([(40+rect['left'], 30+rect['top']+rect['height'])],str(smile))
      draw.text([(rect['left'], 30+rect['top']+rect['height'])],'smile:')
  st.image(img, caption='Uploaded Image.', use_column_width=True)

