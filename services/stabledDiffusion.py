from requests import ReadTimeout
from flask import send_file
from io import BytesIO
from aihub.stableDiffusion import stableDiffusion
# from db.storage import imageToStore


def stable_diffusion_request(text):
    response = stableDiffusion(text)
    try:
        return response.content
        # return {"image_url": imageToStore(response.content)}
    except ReadTimeout:
        return "stable diffusion doesn't return image"


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=75)
    img_io.seek(0)
    # imageToStore(pil_img)
    return send_file(img_io, mimetype='image/jpeg')



