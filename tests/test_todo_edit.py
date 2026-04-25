from playwright.sync_api import expect
from pages.todo_page import TodoPage


def test_edit_todo_successfully(page):
    todo_page = TodoPage(page)
    todo_page.open()

    todo_page.add_todo("Buy milk")
    todo_page.edit_todo("Buy milk", "Buy oat milk")

    todo_page.expect_todo_visible("Buy oat milk")
    todo_page.expect_todo_not_visible("Buy milk")


def test_edit_todo_to_empty_should_delete_todo(page):
    todo_page = TodoPage(page)
    todo_page.open()

    todo_page.add_todo("Buy milk")
    todo_page.edit_todo("Buy milk", "")

    expect(todo_page.todo_items).to_have_count(0)


def test_edit_todo_to_whitespace_should_delete_todo(page):
    todo_page = TodoPage(page)
    todo_page.open()

    todo_page.add_todo("Buy milk")
    todo_page.edit_todo("Buy milk", "     ")

    expect(todo_page.todo_items).to_have_count(0)
