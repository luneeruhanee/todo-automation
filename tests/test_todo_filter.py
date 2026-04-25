from playwright.sync_api import expect
from pages.todo_page import TodoPage
from data.test_data import TODO_ITEMS


def test_active_filter_displays_only_active_todos(page):
    todo_page = TodoPage(page)
    todo_page.open()

    todo_page.add_multiple_todos(TODO_ITEMS)
    todo_page.complete_todo_by_text("Buy milk")
    todo_page.filter_by_active()

    todo_page.expect_todo_not_visible("Buy milk")
    todo_page.expect_todo_visible("Read book")
    todo_page.expect_todo_visible("Exercise")


def test_completed_filter_displays_only_completed_todos(page):
    todo_page = TodoPage(page)
    todo_page.open()

    todo_page.add_multiple_todos(TODO_ITEMS)
    todo_page.complete_todo_by_text("Buy milk")
    todo_page.filter_by_completed()

    todo_page.expect_todo_visible("Buy milk")
    todo_page.expect_todo_not_visible("Read book")
    todo_page.expect_todo_not_visible("Exercise")


def test_all_filter_displays_all_todos(page):
    todo_page = TodoPage(page)
    todo_page.open()

    todo_page.add_multiple_todos(TODO_ITEMS)
    todo_page.complete_todo_by_text("Buy milk")
    todo_page.filter_by_all()

    for item in TODO_ITEMS:
        todo_page.expect_todo_visible(item)


def test_clear_completed_todos(page):
    todo_page = TodoPage(page)
    todo_page.open()

    todo_page.add_multiple_todos(TODO_ITEMS)
    todo_page.complete_todo_by_text("Buy milk")
    todo_page.clear_completed_todos()

    todo_page.expect_todo_not_visible("Buy milk")
    todo_page.expect_todo_visible("Read book")
    todo_page.expect_todo_visible("Exercise")
