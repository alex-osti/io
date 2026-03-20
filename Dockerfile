# Global Nginx build
FROM nginx:alpine

# Copy all the static HTML files to Nginx's HTML directory
COPY . /usr/share/nginx/html/

# Copy our custom nginx configuration
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

# Keep the build clean with some basic cleanup (optional)
RUN rm -rf /usr/share/nginx/html/.git /usr/share/nginx/html/node_modules /usr/share/nginx/html/web

# Expose port 80
EXPOSE 80

# The default command is to run Nginx
CMD ["nginx", "-g", "daemon off;"]
