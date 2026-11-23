from config.db_config import get_connection
class UsuarioRepository:
    def find_by_username(self,username:str):
        con=get_connection()
        cursor=con.cursor(dictionary=True)
        cursor.execute("select * from users where user=%s",(username,))
        row=cursor.fetchone()
        con.close()
        return row