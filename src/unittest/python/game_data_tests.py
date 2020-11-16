import unittest
from game_data import is_string, Question, MCQ

class QuestionTest(unittest.TestCase):
   def test_is_string(self):
      self.assertIsNone(is_string('string', 'var_name'))
   def test_class_question(self):
      # test constructor
      with self.assertRaises(TypeError):
         q = Question(2,'answer')
      with self.assertRaises(TypeError):
         q = Question('text',('s',1))
      q = Question('text', 'answer')
      # get_type
      self.assertEqual(q.get_type(), 'QandA')
      # get_text
      self.assertEqual(q.get_text(), 'text')
      # get_answer
      self.assertEqual(q.get_answer(), 'answer')
      # verify
      self.assertEqual(q.verify(),-1)
      # set_text
      q.set_text('new text')
      self.assertEqual(q.get_text(), 'new text')
      # set_answer
      q.set_answer('new answer')
      self.assertEqual(q.get_answer(), 'new answer')
      # set_user_answer & get_user_answer
      q.set_user_answer('new answer')
      self.assertEqual(q.get_user_answer(), 'new answer')
      # verify
      self.assertTrue(q.verify())

class MCQTest(unittest.TestCase):
   def test_class_mcq(self):
      # test constructor
      with self.assertRaises(TypeError):
         q = MCQ(2,'answer')
      with self.assertRaises(TypeError):
         q = MCQ('text',('s',1))
      q = MCQ('text', 'answer')
      # get_type
      self.assertEqual(q.get_type(), 'MCQ')
      # get_text
      self.assertEqual(q.get_text(), 'text')
      # get_answer
      self.assertEqual(q.get_answer(), 'answer')
      # verify
      self.assertEqual(q.verify(),-1)
      # set_text       
      q.set_text('new text')
      self.assertEqual(q.get_text(), 'new text')
      # set_answer
      q.set_answer('new answer')
      self.assertEqual(q.get_answer(), 'new answer')
      # set_user_answer & get_user_answer
      q.set_user_answer('new answer')
      self.assertEqual(q.get_user_answer(), 'new answer')
      # set_wrong
      with self.assertRaises(TypeError):
         q.set_wrong((1, 'string'), 'string')
      # get_wrong
      q.set_wrong('wrong1', 'wrong2')
      self.assertEqual(q.get_wrong(), ('wrong1', 'wrong2'))
