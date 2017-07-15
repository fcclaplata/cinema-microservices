from datetime import timedelta, date
from bson.objectid import ObjectId
from project.db import db


class MoiveRepository():

    def __init__(self, db):
        self.db = db

    def cinemas(self, filter={}):
        return list(self.db.cinemas.find(filter))

    def cinema(self, id):
        return self.db.cinemas.find_one(id)

    def schedules(self, city, movie):
        match = {
            '$match': {
                'city_id': city,
                'cinemaRooms.schedules.movie_id': movie
            }
        }
        project = {
            '$project': {
                'name': 1,
                'cinemaRooms.schedules.time': 1,
                'cinemaRooms.name': 1,
                'cinemaRooms.format': 1
            }
        }

        unwind = [{'$unwind': '$cinemaRooms'}, {
            '$unwind': '$cinemaRooms.schedules'}]

        group = [
            {
                '$group': {
                    '_id': {
                        'name': '$name',
                        'room': '$cinemaRooms.name'
                    },
                    'schedules': {'$addToSet': '$cinemaRooms.schedules.time'}
                }
            },
            {
                '$group': {
                    '_id': '$_id.name',
                    'schedules': {'$addToSet': {
                        'room': '$_id.room',
                        'schedules': '$schedules'
                    }
                    }
                }
            }
        ]

        pipeline = [match, project, *unwind, *group]
        return list(self.db.cinemas.aggregate(pipeline))

movie_repo = MoiveRepository(db)
