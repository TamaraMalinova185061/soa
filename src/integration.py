import httpx
from fastapi import HTTPException, status
from pydantic import EmailStr
from src.config import Settings, get_config


class InventoryConnErr(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="There was an error integrating with the inventory service",
        )


class NotificationConnErr(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="There was an error integrating with the notification service",
        )


async def inventory_service_has_available_space() -> bool:
    settings: Settings = get_config()
    if settings.debug:
        print("using debug version - always returns true")
        return True

    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(url=settings.inventory_service_url)
            if r.is_success:
                # this should return a bool
                return r.json()
            else:
                raise InventoryConnErr
    except Exception:
        raise InventoryConnErr


async def notification_service_email_user(
    email: EmailStr, body: str, subject: str
) -> bool:
    settings: Settings = get_config()
    if settings.debug:
        print("using debug version - always returns true")
        return True

    try:
        async with httpx.AsyncClient() as client:
            r = await client.post(
                url=settings.notification_service_url,
                data={"email": email, "subject": subject, "body": body},
            )
            if not r.is_success:
                raise NotificationConnErr
            return True
    except Exception:
        raise NotificationConnErr
