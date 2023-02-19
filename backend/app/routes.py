from flask import render_template
from flask import request
from app import app
from wordcloud import WordCloud
import io
import base64


# Use wordcloud to generate picture
def get_word_cloud(text):
    # font = "./SimHei.ttf"
    # pil_img = WordCloud(width=500, height=500, font_path=font).generate(text=text).to_image()

    pil_img = WordCloud(width=800, height=300, background_color="white").generate(text=text).to_image()
    img = io.BytesIO()
    pil_img.save(img, "PNG")
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode()
    return img_base64


# Main page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# Generate picture API, return base64 format
@app.route('/word/cloud/generate', methods=["POST"])
def cloud():
    text = request.json.get("word")
    res = get_word_cloud(text)
    return res
