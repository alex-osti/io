# Stage 1: Runtime
FROM nginx:alpine

# Copy all the static HTML files, images, etc. to Nginx's HTML directory
COPY . /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# The default command is to run Nginx
CMD ["nginx", "-g", "daemon off;"]
