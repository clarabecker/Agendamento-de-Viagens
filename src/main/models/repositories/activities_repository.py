from typing import Dict, List, Tuple
from sqlite3 import Connection

class ActivitiesRepository:
    def __init__(self, conn : Connection) -> None:
        self.__conn = conn

    
    def registryActivities(self, activities_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO activities
                (id, trip_id, title, occurs_at)
            VALUES 
                (?, ?, ?, )
            ''',
                (
                activities_infos["id"],
                activities_infos["trip_id"],
                activities_infos["title"],
                activities_infos["occurs_at"]
            )
        )
        self.__conn.commit()

    def findActivitiesFromTrip(self, trip_id : str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM activities WHERE trip_id = ?
            ''',
            (trip_id,)
        )
        activities = cursor.fetchall()
        return activities