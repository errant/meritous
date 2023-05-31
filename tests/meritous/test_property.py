

import pytest

import test_data as data

import meritous.core
import meritous.exceptions

def test_property_basics():
    p = meritous.core.Property(str, data.TEST_STR)
    assert p.value ==  data.TEST_STR
    assert p._type == str
    p.value = data.TEST_STR_ALT
    assert p.value == data.TEST_STR_ALT

def test_property_required():
    p = meritous.core.Property(str)
    assert p.is_required == True
    p = meritous.core.Property(str, required=False)
    assert p.is_required == False

def test_property_init_no_default():
    p = meritous.core.Property(str)
    assert p.value == None
    p.value = data.TEST_STR
    assert p.value == data.TEST_STR

def test_property_init_incorrect_default_type():
    with pytest.raises(meritous.exceptions.PropertyException):
        meritous.core.Property(str, data.TEST_INT)

def test_property_validate():
    p = meritous.core.Property(str, data.TEST_STR)
    assert p.validate() == True
    p.value = data.TEST_STR_ALT
    assert p.validate() == True

def test_property_init_without_validation():
    p = meritous.core.Property(str, data.TEST_INT,validate_on_set=False)
    assert p.validate() == False
    assert p.value == data.TEST_INT
    p.value = data.TEST_STR
    assert p.validate() == True
    assert p.value == data.TEST_STR
    p.value = data.TEST_INT
    assert p.validate() == False
    assert p.value == data.TEST_INT
