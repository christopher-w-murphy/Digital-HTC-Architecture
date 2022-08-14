FROM python:3.9-slim

WORKDIR /project

COPY requirements.txt /project
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    imagemagick \
    tesseract-ocr \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN wget -O /usr/share/tesseract-ocr/4.00/tessdata/eng.traineddata https://github.com/tesseract-ocr/tessdata_best/blob/main/eng.traineddata?raw=true
RUN wget -O /usr/share/tesseract-ocr/4.00/tessdata/fra.traineddata https://github.com/tesseract-ocr/tessdata_best/blob/main/fra.traineddata?raw=true

# Give ImageMagick permission to read and write PDFs on Linux
RUN sed -i 's/rights="none" pattern="PDF"/rights="read|write" pattern="PDF"/g' /etc/ImageMagick-6/policy.xml

# run container processes with a non-root user
RUN addgroup --system app && adduser --system --group app

RUN mkdir ~/.streamlit
COPY .streamlit/config.toml ~/.streamlit/config.toml

COPY 0_🦃_Digital_HTC_Architecture.py /project
COPY pages/ /project/pages
COPY src/ /project/src

USER app
EXPOSE 8501

ENTRYPOINT ["streamlit"]
CMD ["run", "0_🦃_Digital_HTC_Architecture.py"]
