[app]
title = FaceApp
package.name = faceapp
package.domain = org.yourdomain
source.dir = .
source.include_exts = py,png,jpg,json,xml,mp3

requirements = kivy,flask,opencv-python-headless,numpy,requests

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.entrypoint = main.py

# Ensure your OpenCV data file and other needed assets are included
source.include_patterns = haarcascade_frontalface_default.xml

# (Other fields: fill out as needed)
