from daemon_worker import DaemonWorker
import pytest

def test_initial_interval():
    worker = DaemonWorker(interval=5)
    assert worker.get_interval() == 5

def test_set_interval():
    worker = DaemonWorker()
    worker.set_interval(10)
    assert worker.get_interval() == 10

def test_invalid_interval():
    worker = DaemonWorker()
    with pytest.raises(ValueError):
        worker.set_interval(0)
