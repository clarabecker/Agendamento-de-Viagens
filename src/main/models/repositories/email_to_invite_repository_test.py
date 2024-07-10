import pytest
import uuid
from .email_to_invite_repository import EmailsToInviteRepository
from src.main.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_registryEmail():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    email_trip_infos = {
        "id" : str(uuid.uuid4()),
        "trip_id" : trip_id,
        "email" : "olaMundo@email.com"
    }

    emails_to_invite_repository.registryEmail(email_trip_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_findEmailsFromTrip():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    emails = emails_to_invite_repository.findEmailsFromTrip(trip_id)
    print()
    print(emails)

