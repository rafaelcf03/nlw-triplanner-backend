import uuid
from datetime import datetime, timedelta
from src.models.repositories.emails_to_invite_repo import EmailsToInviteRepo
from src.models.repositories.trips_repo import TripsRepo
from src.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect()
email_id = str(uuid.uuid4())
trip_id = "553565a6-192c-4f58-9ca2-f3cbe374d4e5"

def test_register_email():
    conn = db_connection_handler.get_connection()
    emails_repo = EmailsToInviteRepo(conn)
    trips_repo = TripsRepo(conn)
    trips_repo.find_trip_by_id(trip_id)
    
    email_infos = {
        "id": email_id,
        "trip_id": trip_id,
        "email": "rafael@email.com",
    }    
    
    emails_repo.register_email(email_infos=email_infos)
    
    
def test_find_email_by_trip_id():
    conn = db_connection_handler.get_connection()
    emails_repo = EmailsToInviteRepo(conn)
    
    emails = emails_repo.find_email_by_trip_id(trip_id)
    print(emails)
    
    
def test_find_email():
    conn = db_connection_handler.get_connection()
    emails_repo = EmailsToInviteRepo(conn)
    
    emails = emails_repo.find_email("rafael@email.com")
    print(emails)