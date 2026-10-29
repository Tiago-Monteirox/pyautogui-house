import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3


def open_paintbrush():
    pyautogui.hotkey('command', 'space')
    time.sleep(1)
    pyautogui.write('paintbrush')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)  # Wait for Paintbrush to open
    pyautogui.click(575, 563)  # New document button
    time.sleep(1)
    pyautogui.click(711, 474)  # Select 800x600 resolution
    time.sleep(1)
    pyautogui.doubleClick(588, 106)  # Maximize window


def draw_walls():
    pyautogui.click(68, 254)
    pyautogui.moveTo(509, 381)
    pyautogui.dragTo(809, 581, duration=1, button='left')  # Drag to draw wall


def draw_roof():
    pyautogui.click(72, 219)
    pyautogui.moveTo(479, 381)
    pyautogui.dragTo(659, 231, duration=1, button='left')
    pyautogui.dragTo(839, 381, duration=1, button='left')  # Drag to draw roof
    pyautogui.moveTo(479, 381)
    pyautogui.dragTo(839, 381, duration=1, button='left')  # Drag to draw roof


def draw_windows():
    pyautogui.click(68, 254)
    pyautogui.moveTo(539, 431)
    pyautogui.dragTo(599, 491, duration=1, button='left')  # Drag to draw window
    pyautogui.moveTo(719, 431)
    pyautogui.dragTo(779, 491, duration=1, button='left')  # Drag to draw window


def draw_door():
    pyautogui.moveTo(629, 471)
    pyautogui.dragTo(689, 581, duration=1, button='left')  # Drag to draw door


def draw_floor():
    pyautogui.click(72, 219)
    pyautogui.click(92, 409)
    pyautogui.click(81, 622)
    pyautogui.moveTo(409, 581)
    pyautogui.dragTo(959, 581, duration=1, button='left')  # Drag to draw floor


def paint_house():
    pyautogui.click(73, 189)
    pyautogui.click(84, 189)
    pyautogui.click(63, 612)
    pyautogui.click(638, 428)
    pyautogui.click(27, 610)
    pyautogui.click(688, 300)
    pyautogui.click(46, 575)
    pyautogui.click(140, 624)
    pyautogui.click(579, 468)
    pyautogui.click(754, 466)
    pyautogui.click(43, 569)
    pyautogui.click(664, 533)


open_paintbrush()
draw_walls()
draw_roof()
draw_windows()
draw_door()
draw_floor()
paint_house()