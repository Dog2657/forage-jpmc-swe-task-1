import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_get_ratio(self):
    tests = [
      {"exp": 10, "arg1": 100, "arg2": 10},
      {"exp": 20, "arg1": 100, "arg2": 5},
      {"exp": 100, "arg1": 200, "arg2": 2},
      {"exp": 100, "arg1": 1000, "arg2": 10},
    ]
    
    for test in tests:
      self.assertEqual(test["exp"], getRatio(test["arg1"], test["arg2"]))

  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      top_price: float = quote["top_bid"]["price"]
      top_ask: float = quote["top_ask"]["price"]

      self.assertEqual( getDataPoint(quote), (quote.get("stock"), top_price, top_ask, (top_price + top_ask) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    for quote in quotes:
      top_price: float = quote["top_bid"]["price"]
      top_ask: float = quote["top_ask"]["price"]

      self.assertEqual( getDataPoint(quote), (quote.get("stock"), top_price, top_ask, (top_price + top_ask) / 2))

  



if __name__ == '__main__':
    unittest.main()
