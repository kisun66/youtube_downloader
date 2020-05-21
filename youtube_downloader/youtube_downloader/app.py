import os
from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask import send_from_directory
import pytube
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def main(): 
    return render_template('index.html', url=None)

@app.route("/scan", methods=['GET'])
def scan():
    try:
        now = datetime.now()
        year = now.year
        mon = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second
        filename = f"{year}-{mon}-{day}-{hour}-{minute}-{second}"

        url = request.args.get('url')
        youtube = pytube.YouTube(url)
        title = youtube.title
        thumbnail_url = youtube.thumbnail_url
        parent_url = "./Downloads"
        youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(parent_url, filename=filename)

        return render_template('index.html', title=title, thumbnail_url=thumbnail_url, filename=filename)
    except:
        return render_template('index.html', url=None)

@app.route("/download", methods=['GET', 'POST'])
def download():
    filename = request.form['filename']
    uploads = os.path.join("../", "Downloads")
    return send_from_directory(directory=uploads, filename=f"{filename}.mp4", as_attachment=True)
    # as_attachment : 바로 다운로드 하기, 이거 없으면 mp4 스트리밍 하는것처럼 웹에서 띄워짐

if __name__ == "__main__":
    app.run(debug=True,
            host='0.0.0.0')