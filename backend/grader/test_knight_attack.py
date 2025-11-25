import importlib

# Load student's submission dynamically
submission = importlib.import_module("grader.student_submission")
knight_attack = submission.knight_attack

def test_01():
    assert knight_attack(8, 1, 1, 2, 2) == 2

def test_02():
    assert knight_attack(8, 1, 1, 2, 3) == 1

def test_03():
    assert knight_attack(8, 0, 3, 4, 2) == 3

def test_04():
    assert knight_attack(8, 0, 3, 5, 2) == 4

def test_05():
    assert knight_attack(24, 4, 7, 19, 20) == 10

def test_06():
    assert knight_attack(100, 21, 10, 0, 0) == 11

def test_07():
    assert knight_attack(3, 0, 0, 1, 2) == 1

def test_08():
    assert knight_attack(3, 0, 0, 1, 1) is None
