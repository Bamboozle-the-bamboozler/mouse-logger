from pynput import mouse
import threading

class MouseLogger:
    def __init__(self, log_file="mouselog.txt"):
        self.log = ""
        self.log_file = log_file

    def append_to_log(self, entry):
        self.log += entry + "\n"

    def on_move(self, x, y):
        self.append_to_log(f"Mouse moved to ({x}, {y})")

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.append_to_log(f"Mouse clicked at ({x}, {y}) with {button}")
        else:
            self.append_to_log(f"Mouse released at ({x}, {y}) with {button}")

    def on_scroll(self, x, y, dx, dy):
        self.append_to_log(f"Mouse scrolled at ({x}, {y}) by ({dx}, {dy})")

    def report(self):
        with open(self.log_file, "a") as f:
            f.write(self.log)
        self.log = ""
        timer = threading.Timer(10, self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        print("Mouse logger started.")
        mouse_listener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
            on_scroll=self.on_scroll
        )
        with mouse_listener:
            self.report()
            mouse_listener.join()

if __name__ == "__main__":
    logger = MouseLogger()
    logger.start()
