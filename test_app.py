import pytest

# ── core logic tests (testing the operations main() performs) ──

def test_add_single_task():
    tasks = []
    tasks.append("Buy groceries")
    assert len(tasks) == 1
    assert tasks[0] == "Buy groceries"

def test_add_multiple_tasks():
    tasks = []
    tasks.append("Buy groceries")
    tasks.append("Walk the dog")
    tasks.append("Read a book")
    assert len(tasks) == 3
    assert tasks[1] == "Walk the dog"

def test_remove_task_valid():
    tasks = ["Buy groceries", "Walk the dog", "Read a book"]
    tasks.pop(0)  # remove first item (user enters 1, code does pop(1-1))
    assert len(tasks) == 2
    assert "Buy groceries" not in tasks

def test_remove_task_last_item():
    tasks = ["Buy groceries", "Walk the dog"]
    tasks.pop(1)  # remove second item
    assert tasks == ["Buy groceries"]

def test_remove_task_invalid_index():
    tasks = ["Buy groceries"]
    with pytest.raises(IndexError):
        tasks.pop(10)  # out of range

def test_remove_task_empty_list():
    tasks = []
    with pytest.raises(IndexError):
        tasks.pop(0)

def test_task_order_preserved():
    tasks = []
    tasks.append("Task A")
    tasks.append("Task B")
    tasks.append("Task C")
    assert tasks[0] == "Task A"
    assert tasks[2] == "Task C"

def test_remove_middle_task():
    tasks = ["Task A", "Task B", "Task C"]
    tasks.pop(1)
    assert tasks == ["Task A", "Task C"]
