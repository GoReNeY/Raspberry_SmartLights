from fastapi import APIRouter, Body
from typing import Annotated, Any


led_control_router = APIRouter(prefix="/led_control", tags=["LED_CONTROL_ROUTER"])


@led_control_router.post("/on")
async def led_turn_on(body: Annotated[Any, Body()]) -> str | None:
    print(body)


@led_control_router.post("/off")
async def led_turn_off(body: Annotated[Any, Body()]) -> str | None:
    print(body)
