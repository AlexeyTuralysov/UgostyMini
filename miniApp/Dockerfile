FROM node:18.13.0-alpine

WORKDIR /app

COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json


RUN npm install

COPY . .

# Собираем проект
#RUN npm run build
CMD [ "npm" ,"run", "build" ]