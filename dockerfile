# Use a small nginx image
FROM nginx:alpine

# Set the working directory to Nginx's web root
WORKDIR /usr/share/nginx/html

# Metadata (optional)
LABEL maintainer="you@example.com"
LABEL description="Simple one-page static site served with nginx"

# Remove default nginx content and copy your site in
RUN rm -rf /usr/share/nginx/html/*
COPY index.html .

# Expose the standard HTTP port
EXPOSE 80

# Start nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
