FROM python:3.10

WORKDIR /dida

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install --default-timeout=1000 -r requirements.txt

# Copy the rest of the files
COPY . .

# Set executable permissions for entrypoint script
RUN chmod +x entrypoint.sh

# Expose port and define entrypoint
EXPOSE 8002
ENTRYPOINT ["./entrypoint.sh"]
CMD []
