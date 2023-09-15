from inventory import Inventory
from database import Database
from unittest.mock import Mock, call
import pytest

@pytest.fixture
def inv(): 
    return Inventory(5)


def test_add_product_to_inventory(inv):
    # # Arrange
    # inv = Inventory(5)

    # Act
    inv.add_product("ProdA", 3)

    # Assert
    assert "ProdA" in inv.products


def test_add_product_over_max_raises_exception(inv): 
    # Arrange
    # inv = Inventory(5)
    inv.add_product('ProdA', 2)
    inv.add_product('ProdB', 4)
    inv.add_product('ProdC', 7)
    inv.add_product('ProdD', 1)
    inv.add_product('ProdE', 9)

    # Act and assert
    with pytest.raises(OverflowError): 
        inv.add_product("ProdF", 6)

    
def test_get_stock_from_existing_product(inv): 
    # Arrange
    # inv = Inventory(5)
    inv.add_product('ProdA', 2)

    # Act
    stock = inv.get_stock('ProdA')
    
    # Assert
    assert stock == 2
    

def test_add_product_modifies_existing_product(inv): 
    # Arrange
    # inv = Inventory(5)
    inv.add_product('ProdA', 2)
    
    # Act
    inv.add_product('ProdA', 4)
    modified_stock = inv.get_stock('ProdA')
    
    # Assert
    assert modified_stock == 4

# here is the moment to introduce fixture and use it upwards

def test_calculate_stock_value(inv): 
    # Arrange
    inv.add_product("ProdA", 1)
    inv.add_product("ProdB", 2)
    database_mock = Mock(spec=Database)
    database_mock.get.side_effect = lambda x: {"ProdA": 2.0, "ProdB": 3.0}.get(x)
    
    # Act
    value = inv.calculate_stock_value(database_mock)
    
    # Assert
    assert value == 8.0
    database_mock.get.assert_has_calls(calls=[call("ProdA"), call("ProdB")])
    
# here we mock the database.get method

    



    



    






