# Stepik-Academy-Selenium-Python-PageObjectModel
[Stepik Academy] Автоматизация тестирования с помощью Selenium и Python. Module "Page Object Model"

Run all tests:
  pytest -v -s --tb=line

Run page tests:
  pytest -v -s --tb=line --browser_name=chrome --language=en test_main_page.py
  pytest -v -s --tb=line --browser_name=chrome --language=en test_product_page.py

Run mark tests:
  pytest -v -s --tb=line --browser_name=chrome --language=en -m guest_login
  pytest -v -s --tb=line --browser_name=chrome --language=en -m guest_empty_basket
  pytest -v -s --tb=line --browser_name=chrome --language=en -m guest_add_to_basket
  pytest -v -s --tb=line --browser_name=chrome --language=en -m user_add_to_basket

Specially for review:
  pytest -v -s --tb=line -m need_review
