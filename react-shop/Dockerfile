FROM node:14.9

WORKDIR /app/front

COPY package*.json ./
COPY entrypoint.sh ./

RUN npm install

COPY . ./

ENTRYPOINT ["sh", "/app/front/entrypoint.sh"]