import pytest
import uuid
from .links_repository import LinkRepository
from src.main.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_registryLink():
    conn = db_connection_handler.get_connection()
    links_repository = LinkRepository(conn)

    link_infos = {
        "id" : link_id,
        "trip_id" : trip_id,
        "link" : "somelink.com",
        "title" : "Hotel"
    }

    links_repository.registryLink(link_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_findLinksFromTrip():
    conn = db_connection_handler.get_connection()
    links_repository = LinkRepository(conn)

    response = links_repository.findLinksFromTrip(trip_id)

    assert isinstance(response, list)
    assert isinstance(response[0], tuple)
