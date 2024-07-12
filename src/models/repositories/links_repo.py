from sqlite3 import Connection


class LinksRepo:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
        
    def register_link(self, link_infos: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO links
                    (id, trip_id, link) 
                VALUES
                    (?, ?, ?)
            ''', (
                link_infos["id"],
                link_infos["trip_id"],
                link_infos["email"]
            )
        )
        self.__conn.commit()
        
    def find_trip_by_trip_id(self, trip_id: str) -> list[tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM links WHERE trip_id = ?
            ''', 
            (trip_id,)
        )
        
        return cursor.fetchall()
    