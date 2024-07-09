from prova.models import Film
import datetime
def run():
    film = Film.objects.filter(release_date__lt=datetime.date(year=2020, month=1, day=1)).delete()
    print("DELETE COMPLETED")
