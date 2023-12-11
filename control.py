from __future__ import annotations

import random
import winsound
from typing import TYPE_CHECKING

from pygame.math import Vector2

if TYPE_CHECKING:
    from pygame.joystick import JoystickType

DEAD_ZONE = 0.1
QUADRANT_OFFSET = 20

QUADRANT_TO_ANGLES_MAP = {
    "1": [0, 90],
    "2": [90, 180],
    "3": [180, 270],
    "4": [270, 360]
}


def get_angle(controller: JoystickType) -> float:
    x_axis = controller.get_axis(0)
    y_axis = -controller.get_axis(1)

    if abs(x_axis) < DEAD_ZONE:
        x_axis = 0.0
    if abs(y_axis) < DEAD_ZONE:
        y_axis = 0.0

    vec = Vector2(x_axis, y_axis)
    if vec.length() < DEAD_ZONE:
        return 0.0

    _, angle = vec.as_polar()
    return angle % 360


def quadrant_to_angle_bounds(quadrant: str) -> list:
    local_quadrant = quadrant
    if local_quadrant == "random":
        local_quadrant = str(random.randint(1, 4))

    print(local_quadrant)

    return QUADRANT_TO_ANGLES_MAP[local_quadrant].copy()


def add_offset(angle_bounds: list):
    sign = -1 if angle_bounds[0] > angle_bounds[1] else 1
    angle_bounds[0] = (angle_bounds[0] - (QUADRANT_OFFSET * sign)) % 360
    angle_bounds[1] = (angle_bounds[1] + (QUADRANT_OFFSET * sign)) % 360


def is_angle_within(angle: float, angle_bounds: list) -> bool:
    if angle == 0:
        return True
    lower = angle_bounds[0]
    upper = angle_bounds[1]

    if lower > upper:
        return angle >= lower or angle <= upper
    return angle >= lower and angle <= upper


def alert_player():
    winsound.Beep(100, 100)
