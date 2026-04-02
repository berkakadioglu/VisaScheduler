"""FastAPI entrypoint for the Visa Scheduler application."""

from contextlib import asynccontextmanager

from app.database.session import create_db_tables
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import UserService
from fastapi import APIRouter, FastAPI, Request
from fastapi.templating import Jinja2Templates
from scalar_fastapi import get_scalar_api_reference
from app.utils import TEMPLATE_DIR
from .services.announcement_service import get_announcement_by_id, get_all_announcements, join_queue_service
from fastapi import HTTPException, status
from .services.queue_service import queue_store_init

@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    """Prepare shared infrastructure before the application starts serving requests."""
    await queue_store_init()
    await create_db_tables()
    yield

master_router = APIRouter()

app = FastAPI(lifespan= lifespan_handler)

templates = Jinja2Templates(TEMPLATE_DIR)

app.include_router(master_router)

@app.get("/", include_in_schema= False)
def get_base_html(request: Request):
    """Render the landing page with the current announcement list."""
    announcements = get_all_announcements()
    return templates.TemplateResponse(
        request= request,
        name = "home.html",
        context= {"announcements": announcements}
    )

@app.get("/announcement/{id}", include_in_schema= False)
def get_announcement(id: int, request: Request):
    """Render a single announcement detail page by its identifier."""
    context = get_announcement_by_id(id)
    if context:
        return templates.TemplateResponse(
            request=request,
            name= "announcement.html",
            context= context
        )
    raise HTTPException(status.HTTP_404_NOT_FOUND, "Announcement not found.")

@app.post("/announcement/{id}/join", include_in_schema= True)
def join_queue(id: int, request: Request):
    """Submit a user into the selected announcement queue and re-render the page."""
    context = join_queue_service(id)
    return templates.TemplateResponse(
        request= request,
        name = "announcement.html",
        context= context
    )

@app.post("/register", response_model= UserRead ,include_in_schema= True)
async def register_user(user_data: UserCreate, service: UserService, request: Request,):
    """Create a user account from the posted registration payload."""
    return await service._add_user(user_data)

@app.get("/scalar", include_in_schema= False)
def get_scalar_docs():
    """Expose a developer-friendly API reference UI."""
    return get_scalar_api_reference(
        openapi_url= app.openapi_url,
        title = "Visa Scheduler API"
    )
