# Build image
FROM python:3.9 as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    wget

COPY requirements.txt .
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install -r requirements.txt

RUN wget -O eng.traineddata https://github.com/tesseract-ocr/tessdata_best/blob/main/eng.traineddata?raw=true
RUN wget -O fra.traineddata https://github.com/tesseract-ocr/tessdata_best/blob/main/fra.traineddata?raw=true

# Final image
FROM python:3.9-slim

WORKDIR /project

COPY --from=builder /opt/venv /opt/venv

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ghostscript \
    imagemagick \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder eng.traineddata /usr/share/tesseract-ocr/4.00/tessdata/eng.traineddata
COPY --from=builder fra.traineddata /usr/share/tesseract-ocr/4.00/tessdata/fra.traineddata

# Give ImageMagick permission to read and write PDFs on Linux
RUN sed -i 's/rights="none" pattern="PDF"/rights="read|write" pattern="PDF"/g' /etc/ImageMagick-6/policy.xml

RUN mkdir /root/.streamlit
COPY .streamlit/config.toml /root/.streamlit/config.toml

COPY 0_🦃_Digital_HTC_Architecture.py /project
COPY pages/ /project/pages
COPY src/ /project/src

EXPOSE 8501

ENV PATH="/opt/venv/bin:$PATH"
CMD ["streamlit", "run", "0_🦃_Digital_HTC_Architecture.py"]
