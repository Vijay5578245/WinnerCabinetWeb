from fastapi import Request, HTTPException
from httpx import request
from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime, timezone
from collections import defaultdict
from app.config import Settings

settings = Settings()

class RateLimitMiddleware(BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)
        self.requests = defaultdict(list)  # {ip: [timestamps]}

    async def dispatch(self, request, call_next):
        if request.method != "POST":
            return await call_next(request)

        client_ip = request.client.host
        now = datetime.now(timezone.utc)

        self.requests[client_ip] = [timestamp for timestamp in self.requests[client_ip]
                                    if (now - timestamp).total_seconds() < 60]

        if len(self.requests[client_ip]) >= settings.RATE_LIMIT_PER_MINUTE:
            raise HTTPException(status_code=429, detail="Too many requests. Please try again later.")

        self.requests[client_ip].append(now)
        return await call_next(request)
