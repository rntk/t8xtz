from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import jwt

SECRET_KEY = "your_secret_key"

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if "Authorization" not in request.headers:
            raise HTTPException(status_code=401, detail="Authorization header missing")

        auth_header = request.headers["Authorization"]
        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.state.user = payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")

        response = await call_next(request)
        return response
