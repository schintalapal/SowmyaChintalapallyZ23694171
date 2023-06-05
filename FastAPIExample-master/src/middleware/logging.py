from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from fastapi.requests import Request
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Middlewares are based on Starlette middlewares, which is the
# framework that fastAPI runs on top of.
class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> JSONResponse:
        logging.info(f"Request at {str(request.url.path)}")
        response = await call_next(request)
        return response
