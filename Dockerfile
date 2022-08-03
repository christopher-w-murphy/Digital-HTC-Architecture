FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
  imagemagick \
  tesseract-ocr \
  wget

# Give ImageMagick permission to read and write PDFs on Linux
RUN sed -i 's/rights="none" pattern="PDF"/rights="read|write" pattern="PDF"/g' /etc/ImageMagick-6/policy.xml

RUN wget -O /usr/share/tesseract-ocr/4.00/tessdata/eng.traineddata https://github.com/tesseract-ocr/tessdata_best/blob/main/eng.traineddata?raw=true
RUN wget -O /usr/share/tesseract-ocr/4.00/tessdata/fra.traineddata https://github.com/tesseract-ocr/tessdata_best/blob/main/fra.traineddata?raw=true

RUN mkdir root/.streamlit
COPY .streamlit/config.toml /root/.streamlit/config.toml

RUN mkdir /project
WORKDIR /project

COPY requirements.txt /project
RUN pip install -r requirements.txt

COPY 0_🦃_Digital_HTC_Architecture.py /project
COPY pages/ /project/pages
COPY src/ /project/src

EXPOSE 8501

CMD ["streamlit", "run", "0_🦃_Digital_HTC_Architecture.py"]
