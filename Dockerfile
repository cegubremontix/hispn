# Use the official Ruby 3.x image as the base image
FROM ruby:3

# Set the working directory within the container
WORKDIR /app

# Install Jekyll and other required gems
RUN gem install jekyll bundler

# Install the gems specified in your Gemfile
# RUN bundle install

# Expose the default Jekyll port (4000)
EXPOSE 4000

# bundle exec jekyll build
# bundle exec jekyll serve  --host 0.0.0.0 --incremental

# Start Jekyll with a command
CMD ["/bin/sh"]
