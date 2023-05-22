import pytest
from src.controllers.receipecontroller import ReceipeController
from src.static.diets import Diet
from unittest.mock import patch, MagicMock

@pytest.fixture
def receipe_controller():
    # Set up 
    Controller = MagicMock()
    return ReceipeController(Controller)

@patch('src.controllers.receipecontroller.calculate_readiness')
def test_get_receipe_readiness_complies_with_diet_and_readiness_greater_than_threshold(mock_calculate_readiness, receipe_controller):
    # Arrange
    receipe = { "name": "Test Receipe", "diets": ["vegan"], "ingredients": [...] }
    available_items = { "ingredient1": 2, "ingredient2": 1 }
    diet = Diet.VEGAN
    mock_calculate_readiness.return_value = 0.3

    # Act
    readiness = receipe_controller.get_receipe_readiness(receipe, available_items, diet)

    # Assert
    assert readiness > 0.1

@patch('src.controllers.receipecontroller.calculate_readiness')
def test_get_receipe_readiness_complies_with_diet_and_readiness_less_than_threshold(mock_calculate_readiness, receipe_controller):
    # Arrange
    receipe = { "name": "Test Receipe", "diets": ["vegan"], "ingredients": [...] }
    available_items = { "ingredient1": 0, "ingredient2": 1 }
    diet = Diet.VEGAN
    mock_calculate_readiness.return_value = 0.05

    # Act
    readiness = receipe_controller.get_receipe_readiness(receipe, available_items, diet)

    # Assert
    assert readiness is None

@patch('src.controllers.receipecontroller.calculate_readiness')
def test_get_receipe_readiness_does_not_comply_with_diet(mock_calculate_readiness, receipe_controller):
    # Arrange
    receipe = { "name": "Test Receipe", "diets": ["vegan"], "ingredients": [...] }
    available_items = { "ingredient1": 2, "ingredient2": 1 }
    diet = Diet.VEGETARIAN
    mock_calculate_readiness.return_value = 0.3

    # Act
    readiness = receipe_controller.get_receipe_readiness(receipe, available_items, diet)

    # Assert
    assert readiness is None
