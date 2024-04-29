# Use the base image with Python 3.9
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the entire project directory into the working directory
COPY . .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 for the application
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "main.py"]
