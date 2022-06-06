from celery import shared_task
import requests
import zipfile
import csv
from io import TextIOWrapper, BytesIO

from .models import Website


@shared_task
def load_alexa_rank():
    data = requests.get('http://s3.amazonaws.com/alexa-static/top-1m.csv.zip')
    zf = zipfile.ZipFile(BytesIO(data.content))

    for file in zf.filelist:
        with zf.open(file, 'r') as f:
            reader = csv.reader(TextIOWrapper(f, 'utf-8'))
            for row in reader:
                Website.objects.filter(url=row[1]).update(alexa_rank=row[0])

