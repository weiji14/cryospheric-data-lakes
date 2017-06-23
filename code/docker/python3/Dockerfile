FROM debian:buster-slim
LABEL maintainer "https://github.com/weiji14"
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get -qq update && apt-get install -y --no-install-recommends \
  # Install python, pip, git
   python3 \
   python3-dev \
   python3-pip \
   git

# Initiate python
CMD ["python3"]
