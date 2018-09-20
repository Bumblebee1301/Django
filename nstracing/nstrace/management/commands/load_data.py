from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from nstrace.models import nstracing
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'



ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the nstracing data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from nstrace_data.csv into our nstracing model"

    def handle(self, *args, **options):
        if nstracing.objects.exists():
            print('nstrace data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Creating nstrace data")
        print("Loading nstrace data")
        for row in DictReader(open('./nstrace_data.csv')):
            nst = nstracing()
            nst.Request_Type = row['Request Type']
            nst.Path = row['  Path']
            nst.Pin = row['  Pin']
            nst.Prog = row['  Prog']
            nst.Open_Id = row['  Open Id']
            nst.ZYQ_FileName = row['  ZYQ FileName']
            nst.save()
