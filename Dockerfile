# Builds the Instagram/Facebook agent in social-agent/ from the repository root.
# Railway (and any Docker host) picks this up when the service's Root Directory is left
# empty. With Root Directory set to social-agent, social-agent/Dockerfile is used instead.
FROM node:22-slim AS build
WORKDIR /app
COPY social-agent/package.json social-agent/package-lock.json ./
RUN npm ci
COPY social-agent/tsconfig.json ./
COPY social-agent/src ./src
RUN npm run build

FROM node:22-slim
WORKDIR /app
ENV NODE_ENV=production
COPY social-agent/package.json social-agent/package-lock.json ./
RUN npm ci --omit=dev && npm cache clean --force
COPY --from=build /app/dist ./dist
COPY social-agent/migrations ./migrations
COPY social-agent/businesses ./businesses
USER node
EXPOSE 3000
CMD ["node", "dist/index.js"]
