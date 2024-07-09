import pytest
import uuid
from datetime import datetime, timedelta
from .trips_repository import TripsRepository
from src.main.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_infos = {
        "id" : trip_id,
        "destination" : "São Paulo",
        "start_date" : datetime.strptime("02-01-2024", "%d-%m-%Y"),
        "end_date" : datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name" : "Rejane",
        "owner_email" : "rejane@email.com"
    }

    trips_repository.createTrip(trips_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_findTripById():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trip = trips_repository.findTripById(trip_id)
    print(trip)

@pytest.mark.skip(reason="interacao com o banco")
def test_updateTripStatus():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_repository.updateTripStatus(trip_id)