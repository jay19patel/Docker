FROM python

WORKDIR /main_app
COPY . .


RUN pip install -r requirements.txt
EXPOSE 5000 
CMD gunicorn --bind 0.0.0.0:5000 wsgi:mainapp

## try another way 

# COPY wsgi.py .
# CMD ["gunicorn", "-b", "0.0.0.0:8000"]

