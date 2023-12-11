import argparse

import pygame

from control import alert_player, get_angle, is_angle_within, quadrant_to_angle_bounds
from controller import controller


def main(quadrant: str, time: str):
    pygame.init()
    angle_bounds = quadrant_to_angle_bounds(quadrant)
    try:
        if quadrant == "random":
            pygame.time.set_timer(pygame.USEREVENT, int(float(time) * 60 * 1000))
        while True:
            pygame.event.pump()
            angle = get_angle(controller)
            valid_angle = is_angle_within(angle, angle_bounds)

            if not valid_angle:
                alert_player()

            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    angle_bounds = quadrant_to_angle_bounds(quadrant)
    except KeyboardInterrupt:
        pass
    finally:
        pygame.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Controller angle reader with quadrant option and random time option.")
    parser.add_argument("-q", "--quadrant", default="1", metavar="",
                        help="Specify the desired quadrant (1, 2, 3, 4, or 'random'). Default is '1'.")
    parser.add_argument("-t", "--time", default="5", metavar="",
                        help="Specify the time in miutes which a random mode should be activated")

    args = parser.parse_args()
    main(args.quadrant, args.time)
