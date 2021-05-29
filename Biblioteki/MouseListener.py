from pynput.mouse import Listener
from pynput.mouse import Button


def myszka() -> list:
    punkty = list()

    def on_click(x, y, button, pressed):
        if pressed:
            punkty.append([x, y])
        if button == Button.right:
            listener.stop()

    with Listener(on_click=on_click) as listener:
        listener.join()

    return punkty

