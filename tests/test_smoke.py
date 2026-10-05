import pytest
from assistant.rules import reply

def test_greeting():
    assert "Hello!" in reply("hi")
    assert "Hello!" in reply("hello")

def test_training_office():
    res = reply("where is the training office?")
    assert "I.101" in res
    assert "Training Office" in res

def test_it_helpdesk():
    res = reply("where is the IT helpdesk?")
    assert "E.005" in res
    assert "IT Helpdesk" in res

def test_unknown_query():
    res = reply("random gibberish question 12345")
    assert "I'm sorry" in res

def test_medical_station():
    res = reply("where is the medical station?")
    assert "A.105" in res
    assert "Medical Station" in res

