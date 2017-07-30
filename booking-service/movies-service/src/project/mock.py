from time import mktime
from datetime import date

movies = [{
    'id': '1',
    'title': 'Assasins Creed',
    'runtime': 115,
    'format': 'IMAX',
    'plot': 'Lorem ipsum dolor sit amet',
    'releaseDate': mktime(date(2017, 1, 6).timetuple())
}, {
    'id': '2',
    'title': 'Aliados',
    'runtime': 124,
    'format': 'IMAX',
    'plot': 'Lorem ipsum dolor sit amet',
    'releaseDate': mktime(date(2017, 1, 13).timetuple())
}, {
    'id': '3',
    'title': 'xXx: Reactivado',
    'runtime': 107,
    'format': 'IMAX',
    'plot': 'Lorem ipsum dolor sit amet',
    'releaseDate': mktime(date(2017, 1, 20).timetuple())
}, {
    'id': '4',
    'title': 'Resident Evil: Capitulo Final',
    'runtime': 107,
    'format': 'IMAX',
    'plot': 'Lorem ipsum dolor sit amet',
    'releaseDate': mktime(date(2017, 1, 27).timetuple())
}, {
    'id': '5',
    'title': 'Moana: Un Mar de Aventuras',
    'runtime': 114,
    'format': 'IMAX',
    'plot': 'Lorem ipsum dolor sit amet',
    'releaseDate': mktime(date(2016, 12, 2).timetuple())
}]

