from playwright.sync_api import expect
from pages.todo_page import TodoPage
from data.test_data import SPECIAL_TODO, LONG_TODO


def test_special_character_todo_can_be_added(page):
    todo_page = TodoPage(page)
    todo_page.open()

    todo_page.add_todo(SPECIAL_TODO)

    todo_page.expect_todo_visible(SPECIAL_TODO)


def test_long_todo_text_can_be_added(page):
    todo_page = TodoPage(page)
    todo_page.open()

    todo_page.add_todo(LONG_TODO)

    todo_page.expect_todo_visible(LONG_TODO)


def test_delete_todo(page):
    todo_page = TodoPage(page)
    todo_page.open()

    todo_page.add_todo("Buy milk")
    todo_page.delete_todo_by_text("Buy milk")

    expect(todo_page.todo_items).to_have_count(0)
