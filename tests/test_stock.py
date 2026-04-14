print("KÖR RÄTT TESTFIL")
from stock import Stock, StockItem

def test_add_product():
    #Given
    stock = Stock()

    # When
    product = StockItem("Äpple", 10)
    stock.add_product(product)

    # Then
    assert len(stock.items) == 1
    assert stock.items[0].name == "Äpple"
    assert stock.items[0].amount == 10

def test_decrease_product():
    # Given
    stock = Stock()
    stock.add_product(StockItem("Äpple", 10))

    # When
    stock.decrease_product("Äpple", 3)

    # Then
    assert stock.items[0].amount == 7

def test_decrease_produkt_too_much():
    # Given
    stock = Stock()
    stock.add_product(StockItem("Äpple", 5))

    # When
    result = stock.decrease_product("Äpple", 10)

    # Then
    assert result is False
    assert stock.items[0].amount == 5

def test_decrease_non_existing_product():
        # Given
        stock = Stock()
        stock.add_product(StockItem("Äpple", 10))

        # When
        result = stock.decrease_product("Päron", 3)

        # Then
        assert result is False

def test_decrease_one_of_multiple_products():
    # Given
    stock = Stock()
    stock.add_product(StockItem("Äpple", 10))
    stock.add_product(StockItem("Päron", 20))

    # When
    stock.decrease_product("Päron", 5)

    # Then
    assert stock.items[0].amount == 10
    assert stock.items[1].amount == 15
