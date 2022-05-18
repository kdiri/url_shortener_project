"""
    ..synopsis:: Main file for shortener_app.
"""

import validators
from fastapi import Depends, FastAPI, Request
from fastapi.responses import RedirectResponse

from shortener_app import crud
from shortener_app import models, schemas
from shortener_app.database import SessionLocal, engine
from shortener_app.raise_methods import *

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/url", response_model=schemas.URLInfo)
def create_url(url: schemas.URLBase, db: SessionLocal = Depends(get_db)):
    if not validators.url(url.target_url):
        raise_bad_request("Your provided URL is not valid")

    db_url = crud.create_db_url(db=db, url=url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key
    db_url.admin_url = secret_key

    return db_url


# @app.get("/")
# def read_root():
#     """
#     ..note::
#         This function is used to read the root.
#     """
#     return "Welcome to the URL shortener API :)"


@app.get("/{url_key")
def forward_to_target(
    url_key: str, request: Request, db: SessionLocal = Depends(get_db)
):
    """
    ..note::
        This function is used to forward the request to the target URL.
    """
    if db_url := crud.get_db_url_by_key(db=db, url_key=url_key):
        response = RedirectResponse(db_url.target_url)
        response.status_code = 302
        return response
    raise_not_found(request)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
