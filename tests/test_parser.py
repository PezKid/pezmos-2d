import sys
import os
import pytest

# add the parent directory to the import path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import expression_parser as parser  # assumes your tokenizer is in parser.py

def test_simple_addition():
  assert parser.tokenize("3 + 2") == [
    ('NUMBER', '3'), ('PLUS', '+'), ('NUMBER', '2')
  ]

def test_variable_expression():
  assert parser.tokenize("3x + 2") == [
    ('NUMBER', '3'), ('IDENT', 'x'), ('PLUS', '+'), ('NUMBER', '2')
  ]

def test_whitespace():
  assert parser.tokenize("  4 *   y ") == [
    ('NUMBER', '4'), ('TIMES', '*'), ('IDENT', 'y')
  ]

def test_parentheses():
  assert parser.tokenize("(x + 1)") == [
    ('LPAREN', '('), ('IDENT', 'x'), ('PLUS', '+'), ('NUMBER', '1'), ('RPAREN', ')')
  ]

def test_decimal():
  assert parser.tokenize("3.14 * r") == [
    ('NUMBER', '3.14'), ('TIMES', '*'), ('IDENT', 'r')
  ]

def test_multiple_letters():
  assert parser.tokenize("foo + bar") == [
    ('IDENT', 'foo'), ('PLUS', '+'), ('IDENT', 'bar')
  ]

def test_invalid_character():
  with pytest.raises(ValueError):
    parser.tokenize("3 + $")