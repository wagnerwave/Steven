FROM node:15.2.0

WORKDIR /usr/src/app

COPY package*.json ./

COPY . .

RUN npm install
RUN npm update --save

EXPOSE 3000

CMD ["node", "server.js"]
