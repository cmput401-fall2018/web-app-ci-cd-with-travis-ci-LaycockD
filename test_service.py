from service import *
from unittest.mock import patch

@patch('service.Service.bad_random', return_value=3)
def test_bad_random(bad_random):
	service = Service()

	assert service.bad_random() == 3

@patch('service.Service.bad_random', return_value=10)
def test_divide(bad_random):
	service = Service()

	assert service.divide(1) == 10
	assert service.divide(2) == 5
	assert service.divide(10) == 1
	assert service.divide(-2) == -5

def test_abs_plus():
	service = Service()

	assert service.abs_plus(1) == 2
	assert service.abs_plus(-1) == 2
	assert service.abs_plus(0) == 1
	assert service.abs_plus(-100.5) == 101.5

@patch('service.Service.bad_random', return_value=5)
def test_complicated_function(bad_random):
	service = Service()

	assert service.complicated_function(10) == (0.5, 1)
	assert service.complicated_function(2.5) == (2, 1)
	assert service.complicated_function(-1) == (-5, 1)

test_divide()
test_abs_plus()
test_complicated_function()
test_bad_random()
