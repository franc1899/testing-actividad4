from src.todo_list import TodoList
from src.todo_list import Task

import unittest

class TestTodoList(unittest.TestCase):

    def test_list_empty_tasks(self):
        todo = TodoList()
        list = todo.list_tasks()
        self.assertEquals([],list)

    def test_add_task(self):
        todo = TodoList()
        todo.add_task("t1")
        t1 = todo.tasks[0]
        self.assertEquals(t1.__str__(),"Task 1: t1 (Priority: 1, Not Done)")
    
    def test_remove_task_found(self):
        todo = TodoList()
        todo.add_task("t1")
        todo.add_task("t2")
        result = todo.remove_task(1)
        self.assertEquals(result,"Task 1 removed.")
        self.assertEquals(todo.list_tasks(),["Task 2: t2 (Priority: 1, Not Done)"])

    def test_remove_task_not_found(self):
        todo = TodoList()
        todo.add_task("t1")
        todo.add_task("t2")
        self.assertEquals(todo.remove_task(3),"Task 3 not found.")
    
    def test_complete_task_found(self):
        todo = TodoList()
        todo.add_task("t1")
        result = todo.complete_task(1)
        self.assertEquals(result,"Task 1 marked as done.")
    
    def test_complete_task_not_found(self):
        todo = TodoList()
        todo.add_task("t1")
        result = todo.complete_task(3)
        self.assertEquals(result,"Task 3 not found.")


    def test_find_high_priority_tasks_geater(self):
        todo = TodoList()
        todo.add_task("t1")
        todo.add_task("t2")
        todo.tasks[0].priority = 2
        todo.tasks[1].priority = 5
        self.assertEquals(todo.find_high_priority_tasks(3),[todo.tasks[1]])

    def test_find_high_priority_tasks_less(self):
        todo = TodoList()
        todo.add_task("t1")
        todo.add_task("t2")
        todo.tasks[0].priority = 2
        todo.tasks[1].priority = 5
        self.assertEquals(todo.find_high_priority_tasks(6),[])

    def test_find_high_priority_tasks_equal(self):
        todo = TodoList()
        todo.add_task("t1")
        todo.add_task("t2")
        todo.tasks[0].priority = 2
        todo.tasks[1].priority = 5
        self.assertEquals(todo.find_high_priority_tasks(5),[])
    
    def test_list_tasks(self):
        todo = TodoList()
        todo.add_task("t1")
        todo.add_task("t2")
        self.assertEquals(todo.list_tasks(),["Task 1: t1 (Priority: 1, Not Done)","Task 2: t2 (Priority: 1, Not Done)"])
