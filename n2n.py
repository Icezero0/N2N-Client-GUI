import os
import threading


class n2n:
    thread: threading.Thread
    N2NPID: int

    def start(self):
        print("start")

    def killN2N(self):
        os.system(f"taskkill /f /pid {self.N2NPID}")