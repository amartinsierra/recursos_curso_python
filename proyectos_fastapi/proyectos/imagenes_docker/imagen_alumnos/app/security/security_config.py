from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from security.modelo_user import User
import datetime
from jose import jwt,JWTError
from repository.usuarios_repository import UsuarioRepository
SECRET_KEY = "12345678ABCDEFGHIJK123456789KLMASWTDDDDDD"
ALGORITHM = "HS256"

#Este objeto permite a otras funciones, a través de Depends, extraer y validar el token
#enviado por el cliente en la petición dentro de Authorization
#La definición del parámetro tokenUrl solo tiene utilidad a la hora de documentar con swagger
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Usuarios simulados (BD real en producción)
"""
LIST_USERS = {
    "user1": {"password": "$2b$12$QrnDTUarKE/tUr1bA67erOTrMSQf0zB3Uzcbyg88pvxjjTKPrpp3y", "role": "USER"},
    "admin": {"password": "$2b$12$dpkBgI7clgMNeMyXsdZ06.UAO15HWQ5Vd1KztYlfXjJWLnOkIw/ge", "role": "ADMIN"}
}
"""
usuario_repository=UsuarioRepository()
#Utilizado para validar contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
#autentica al usuario a partir de sus credenciales, devolviendo 
#el usuario identificado
def autenticar(username: str, password: str):
    user = usuario_repository.find_by_username(username)
    if not user:
        return None
    if not verify_password(password, user["password"]):
        return None
    return User(username=username, role=user["rol"])
#crea el token a partir de los datos del usuario
def crear_token(user: User):
    payload = {
        "sub": user.username,
        "role": user.role,
        "exp": datetime.datetime.now() + datetime.timedelta(minutes=30) #30 minutos de vida para el token
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
#extrae el token de la petición y lo decodifica
def get_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return User(
            username=payload["sub"],
            role=payload["role"]
        )
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
#obtiene el usuario y si no es admin genera un 403
def require_admin(user: User = Depends(get_user)):
    if user.role != "ADMIN":
        raise HTTPException(status_code=403, detail="Permiso denegado")
    return user