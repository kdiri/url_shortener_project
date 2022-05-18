"""
    ..synopsis:: Schemas file for shortener_app.
"""
from pydantic import BaseModel


class URLBase(BaseModel):
    """
    ..note::
    """

    target_url: str


class URL(URLBase):
    """
    ..note::
    """

    is_active: bool
    clicks: int

    class Config:
        """
        ..note::
        """

        orm_mode = True


class URLInfo(URL):
    url: str
    admin_url: str
