import pandas as pd
from prova.models import Film

def run():
    csv_file_path = "C:\\Users\\alles\\Desktop\\movies.csv"
    df = pd.read_csv(csv_file_path)
    for index, row in df.iterrows():
        print("init")
        film = Film(
            film_id=row['id'],
            title=row['title'],
            genres=row['genres'],
            original_language=row['original_language'],
            overview=row['overview'],
            popularity=row['popularity'],
            production_companies=row['production_companies'],
            release_date=row['release_date'],
            budget=row['budget'],
            revenue=row['revenue'],
            runtime=row['runtime'],
            status=row['status'],
            tagline=row['tagline'],
            vote_average=row['vote_average'],
            vote_count=row['vote_count'],
            credits=row['credits'],
            keywords=row['keywords'],
            poster_path=row['poster_path'],
            backdrop_path=row['backdrop_path'],
            recommendations=row['recommendations']
        )
        print("try to save")
        film.save()
        print("save")
    print("CSV caricato")