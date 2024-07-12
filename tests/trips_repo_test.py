import uuid
from datetime import datetime, timedelta
from src.models.repositories.trips_repo import TripsRepo
from src.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect()
trip_id = str(uuid.uuid4())

def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repo = TripsRepo(conn)
    
    trips_infos = {
        "id": trip_id,
        "destination": "Goiânia - GO",
        "start_date": datetime.strptime("10-08-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("10-08-2024", "%d-%m-%Y") + timedelta(days=7),
        "owner_name": "Lucas",
        "owner_email": "lucas@email.com",
        "status": 0
    }    
    
    trips_repo.create_trip(trips_infos=trips_infos)
    
    trips_infos2 = {
        "id": str(uuid.uuid4()),
        "destination": "Fortaleza - CE",
        "start_date": datetime.strptime("11-10-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("11-10-2024", "%d-%m-%Y") + timedelta(days=15),
        "owner_name": "Amanda",
        "owner_email": "amanda@email.com",
        "status": 0
    } 
    
    trips_repo.create_trip(trips_infos=trips_infos2)
    
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    trips_repo = TripsRepo(conn)
    
    trip = trips_repo.find_trip_by_id(trip_id)
    print(trip)
    
def test_update_trip_status():
    conn = db_connection_handler.get_connection()
    trips_repo = TripsRepo(conn)
    
    trip = trips_repo.update_trip_status(trip_id)
    print(trip)