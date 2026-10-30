
import time
import pyautogui as pg


class PaintbrushController:
    def __init__(self, pause=0.3):
        pg.FAILSAFE = True
        pg.PAUSE = pause

    def click(self, x, y):
        pg.click(x, y)

    def drag(self, start, end, duration=1):
        pg.moveTo(*start)
        pg.dragTo(*end, duration=duration, button="left")

    def wait(self, seconds=1):
        time.sleep(seconds)

    def open(self):
        pg.hotkey("command", "space")
        self.wait()
        pg.write("paintbrush")
        self.wait()
        pg.press("enter")
        self.wait(2)

        self.click(575, 563)
        self.wait()
        self.click(711, 474)
        self.wait()
        pg.doubleClick(588, 106)


class HousePainter:
    def __init__(self, controller):
        self.paint = controller

    def draw_walls(self):
        self.paint.click(68, 254)
        self.paint.drag((509, 381), (809, 581))

    def draw_roof(self):
        self.paint.click(72, 219)
        self.paint.drag((479, 381), (659, 231))
        self.paint.drag((659, 231), (839, 381))
        self.paint.drag((479, 381), (839, 381))

    def draw_windows(self):
        self.paint.click(68, 254)
        self.paint.drag((539, 431), (599, 491))
        self.paint.drag((719, 431), (779, 491))

    def draw_door(self):
        self.paint.drag((629, 471), (689, 581))

    def draw_floor(self):
        self.paint.click(72, 219)
        self.paint.click(92, 409)
        self.paint.click(81, 622)
        self.paint.drag((409, 581), (959, 581))

    def color_house(self):
        actions = [
            (73, 189), (84, 189), (63, 612),
            (638, 428), (27, 610), (688, 300),
            (46, 575), (140, 624), (579, 468),
            (754, 466), (43, 569), (664, 533),
        ]

        for x, y in actions:
            self.paint.click(x, y)

    def draw(self):
        self.draw_walls()
        self.draw_roof()
        self.draw_windows()
        self.draw_door()
        self.draw_floor()
        self.color_house()


if __name__ == "__main__":
    controller = PaintbrushController()
    controller.open()

    house = HousePainter(controller)
    house.draw()
