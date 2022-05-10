FROM node:lts-alpine
RUN apk add --no-cache git
WORKDIR /data
RUN git clone https://github.com/aysudeliahmetoglu/vue-calendar-project /data/app
WORKDIR /data/app
RUN npm install axios --save
RUN rm -rf ./node_modules
RUN rm -rf package-lock.json
RUN npm install