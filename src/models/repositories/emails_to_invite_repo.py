from sqlite3 import Connection


class EmailsToInviteRepo:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
        
    def register_email(self, email_infos: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO emails_to_invite
                    (id, trip_id, email) 
                VALUES
                    (?, ?, ?)
            ''', (
                email_infos["id"],
                email_infos["trip_id"],
                email_infos["email"]
            )
        )
        self.__conn.commit()
        
    def find_email_by_trip_id(self, trip_id: str) -> list[tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM emails_to_invite WHERE trip_id = ?
            ''', 
            (trip_id,)
        )
        
        return cursor.fetchall()
    
    def find_email(self, email: str) -> tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM emails_to_invite WHERE email LIKE ?
            ''', 
            (email,)
        )
        
        return cursor.fetchone()