import time
from typing import Dict, List
from fastapi import HTTPException, status, Request
from app.config import settings


class InMemoryRateLimiter:
    """In-memory rate limiter implementation"""
    
    def __init__(self):
        self.requests: Dict[str, List[float]] = {}
    
    def is_allowed(self, key: str, max_requests: int, window_seconds: int) -> bool:
        """Check if request is allowed based on rate limit"""
        current_time = time.time()
        
        # Initialize if not exists
        if key not in self.requests:
            self.requests[key] = []
        
        # Clean old requests outside the window
        self.requests[key] = [
            req_time for req_time in self.requests[key]
            if current_time - req_time < window_seconds
        ]
        
        # Check if under limit
        if len(self.requests[key]) < max_requests:
            self.requests[key].append(current_time)
            return True
        
        return False


# Global rate limiter instance
rate_limiter = InMemoryRateLimiter()


class RateLimiter:
    """Rate limiter dependency for FastAPI"""
    
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
    
    def __call__(self, request: Request):
        """Rate limiter dependency"""
        # Use user IP as key (in production, you might want to use user ID)
        client_ip = request.client.host
        key = f"booking_{client_ip}"
        
        if not rate_limiter.is_allowed(key, self.max_requests, self.window_seconds):
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail=f"Rate limit exceeded. Maximum {self.max_requests} requests per {self.window_seconds} seconds."
            )
        
        return True


# Rate limiter for bookings: 5 requests per minute
booking_rate_limiter = RateLimiter(max_requests=5, window_seconds=60)