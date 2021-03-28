import threading
import queue
from flask import Flask

q = queue.Queue()


def myqeue():
    def worker():
        """Computer do the work"""
        while True:
            item = q.get()
            print(f"Working on {item}")
            q.task_done()

    # turn-on the worker thread
    threading.Thread(target=worker, daemon=True).start()

    # block until all tasks are done
    q.join()


thread = threading.Thread(target=myqeue)
thread.start()

app = Flask(__name__)


@app.route("/add-task/<int:id>")
def add_task(id=0):
    q.put(id)
    return f"task {id} added"


@app.route("/")
def home():
    return "Go to /add-task/123 to add a background task"
