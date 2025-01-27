from typing import Dict, List, Tuple
from sqlite3 import Connection

class ParticipantsRepository:
    def __init__(self, conn : Connection) -> None:
        self.__conn = conn

    def registryParticipants(self, participants_infos : Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
             '''
                INSERT INTO participants 
                    (id, trip_id, emails_to_invite_id, name)
                VALUES
                    (?, ?, ?, ?)
             ''',
             (
             participants_infos["id"],
             participants_infos["trip_id"],
             participants_infos["emails_to_invite_id"],
             participants_infos["name"]
             )
        )
        self.__conn.commit()

    def findParticipantFromTrip(self, trip_id : str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
             '''
                SELECT p.id, p.name, p.is_confirmed, e.email
                from participants as p
                JOIN emails_to_invite as e ON e.id = p.emails_to_invite_id
                WHERE p.trip_id = ?
            ''', (trip_id,)
        )
        participants = cursor.fetchall()
        return participants
        
    def updateParticipantStatus(self, participant_id : str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            UPDATE participants 
                SET is_confirmed = 1
            WHERE 
                id = ?
            ''', (participant_id,)
        )
        self.__conn.commit()