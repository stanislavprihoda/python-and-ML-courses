import unittest
import capitalize

class Test(unittest.TestCase):
	"""docstring for Test"""
	def test_one_word(self):
		text='python'
		result=capitalize.cap_text(text)
		self.assertEqual(result,'Python')
	
	def test_multiple_words(self):
		text='monty python'
		result=capitalize.cap_text(text)
		self.assertEqual(result,'Monty Python')

if __name__ == '__main__':
	unittest.main()