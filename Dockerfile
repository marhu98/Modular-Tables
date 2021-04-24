#FROM alpine:3.7
FROM python:3.6.4-alpine3.7

RUN apk add --no-cache bash

RUN apk add --no-cache \
    build-base cairo-dev cairo cairo-tools \
    # pillow dependencies
    jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev


RUN pip install "CairoSVG==2.1.3"

#ADD frames/ /frames

#CMD ["ls","frames"]
