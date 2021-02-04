FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN apk --no-cache add --virtual native-deps \
  g++ gcc libgcc libstdc++ linux-headers make python && \
  pip install -r requirements.txt

EXPOSE 5000
CMD python ./runner.py