from app import app
import unittest 

class AppTests(unittest.TestCase): 

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_home_status_code(self):
        """Verify that homepage renders correctly."""
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        
    def test_fortune_results_default_response(self):
        """verify that default user input generates the correct fortune"""
        result = self.app.get("/fortune_results")
        self.assertIn("You will feel unusually good about your quest for the Grail, even if you never find it!", str(result.data))
        
    def test_fortune_results_default_beer(self):
        """verify that user input of "drink=Beer" generates the correct fortune"""
        result = self.app.get("/fortune_results?drink=Beer")
        self.assertIn("You will grow a beer belly and stop shaving as often!", str(result.data))
        
    def test_fortune_results_default_mead(self):
        """verify that user input of "drink=mead" generates the correct fortune"""
        result = self.app.get("/fortune_results?drink=Mead")
        self.assertIn("You will braid your hair and wield an axe with competence!", str(result.data))


# run tests
if __name__ == '__main__':
    unittest.main()