from celery import shared_task
import requests
import zipfile
import csv

from .models import Website


@shared_task
def load_alexa_rank():
    data = requests.get('http://s3.amazonaws.com/alexa-static/top-1m.csv.zip')
    zf = zipfile.ZipFile(data)

    rows = []
    for file in zf.filelist:
        csv_data = zf.read(file)
        for row in csv.reader(csv_data):
            Website.objects.filter(url=row[1]).update(alexa_rank=row[0])

