import client
import unittest

class TestClient(unittest.TestCase):

    def test_getDataPoint(self):
        quote = {
            "stock": 'ABC',
            "top_bid": {
                "price": 123.45,
                "size": 1
            },
            "top_ask": {
                "price": 121.45,
                "size": 1
            }
        }
        stock, bid_price, ask_price, price = client.getDataPoint(quote)

        self.assertEqual((quote['top_bid']['price'] + quote['top_ask']['price']) / 2, price)

if __name__ == '__main__':
    unittest.main()