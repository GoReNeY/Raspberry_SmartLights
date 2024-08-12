from fastapi import APIRouter, Body
from typing import Annotated, Any
from app.services.data_transfer import built_in_led_controller, strip_color_controller



led_control_router = APIRouter(prefix="/led_control", tags=["LED_CONTROL_ROUTER"])


@led_control_router.post("/on")
async def led_turn_on(body: Annotated[Any, Body()]) -> str | None:
    built_in_led_controller(body["data"])


@led_control_router.post("/off")
async def led_turn_off(body: Annotated[Any, Body()]) -> str | None:
    built_in_led_controller(body["data"])


@led_control_router.post("/strip_status")
async def control_color(body: Annotated[Any, Body()]) -> str | None:
    strip_color_controller(body)
