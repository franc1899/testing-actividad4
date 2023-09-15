from src.todo_list import TodoList
from src.task import Task

import unittest

class TestTodoList(unittest.TestCase):

    def test_init(self):
        t1 = Task(2,"t2", 1, False)
        self.assertEqual(t1.task_id,2)
        self.assertEqual(t1.description,"t2")
        self.assertEqual(t1.priority,1)
        self.assertEqual(t1.completed,False)

    def test_str(self):
        t1 = Task(1,"t1",False)
        self.assertEqual(t1.__str__(),"Task 1: t1 (Priority: False, Not Done)")

    def test_is_completed_false(self):
        t1 = Task(1,"t1", 3, False)
        isCompleted = t1.is_completed()
        self.assertEqual(isCompleted,False)
    
    def test_is_completed_true(self):
        t1 = Task(1,"t1", 1, True)
        isCompleted = t1.is_completed()
        self.assertEqual(isCompleted,True)

    def test_complete_task(self):
        t1 = Task(1,"t1",False)
        t1.complete_task()
        self.assertEqual(t1.completed,True)
