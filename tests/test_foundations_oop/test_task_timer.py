from foundations_oop.src.task_timer import TaskTimer

def test_timer_zero_before_start_stop():
    t = TaskTimer("demo")
    assert t.elapsed_seconds() == 0.0
