FROM python:3.9.13-slim-buster
WORKDIR /python-docker
COPY requirements.txt ./

# Installed required tools
# https://stackoverflow.com/questions/39455741/gcc-error-trying-to-exec-cc1plus-execvp-no-such-file-or-directory
#RUN apk add --no-cache --allow-untrusted --repository http://dl-3.alpinelinux.org/alpine/edge/testing hdf5 hdf5-dev
#RUN apk add --no-cache openssh gcc musl-dev git g++
# RUN apk add --no-cache postgresql-dev

# add credentials on build
#ARG SSH_DEPLOY_KEYs
#RUN mkdir /root/.ssh/
#RUN echo "${SSH_DEPLOY_KEY}" > /root/.ssh/id_rsa
#RUN touch /root/.ssh/known_hosts
#RUN ssh-keyscan gitlab.git.jasmine.network >> /root/.ssh/known_hosts
#RUN chmod 400 ~/.ssh/id_rsa

#RUN python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.13.1-cp37-cp37m-linux_x86_64.whl
#RUN pip3 --proxy http://172.23.4.18:8080 install -r requirements.txt
#ENV HTTP_PROXY=http://172.23.4.18:8080
RUN pip install --upgrade pip
RUN pip install --no-cache -r requirements.txt
#RUN apk del gcc musl-dev git g++ openssh hdf5 hdf5-dev
ENV FLASK_DEBUG=1
#VOLUME ["/usr/src/app/extracted"]
#COPY ./ ./
#RUN mkdir extracted
#COPY config/ ./
#RUN ["chmod", "+x", "/usr/src/app/extract.sh"]
#RUN ["chmod", "+x", "/usr/src/app/generate.sh"]
CMD ["python","-m", "flask","run","--host=0.0.0.0"]
#RUN python3 ./extract.py
#RUN python3 ./generate.py
