"""

"""

from fastapi import HTTPException


def raise_bad_request(message: str):
    """
    ..note::
        This function is used to raise a bad request error.
    """
    raise HTTPException(status_code=400, detail=message)


def raise_not_found(request):
    message = f"URL '{request.url}' doesn't exist"
    raise HTTPException(status_code=404, detail=message)
