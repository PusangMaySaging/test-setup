FROM node:14

COPY . /srv/spa

WORKDIR /srv/spa

EXPOSE 2000

RUN  npm install

RUN npm run build

CMD ["npm","run","serve"]