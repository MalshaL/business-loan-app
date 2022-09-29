FROM node:alpine
WORKDIR /app
COPY package.json ./
COPY package-lock.json ./
RUN npm i
COPY . /app
EXPOSE 3000
CMD ["npm", "run", "start"]