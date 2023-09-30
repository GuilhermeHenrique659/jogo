import threading
from typing import Callable


def concurrancy_for_each(fucntion: Callable, array , *agrs):
        chunk_size = len(array) // 10
        threads = []
        for i in range(0, len(array), chunk_size):
            chunk = array[i:i+chunk_size]
            thread = threading.Thread(target=fucntion, args=(*agrs, chunk))
            thread.daemon = True
            thread.start()
            threads.append(thread)
