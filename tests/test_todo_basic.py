from playwright.sync_api import expect
from pages.todo_page import TodoPage
from data.test_data import TODO_ITEMS


def test_page_load_successfully(page):
    todo_page = TodoPage(page)
    todo_page.open()

    expect(page).to_have_title("React • TodoMVC")
    expect(todo_page.new_todo).to_be_visible()


def test_add_new_todo(page):
    todo_page = TodoPage(page)
    todo_page.open()

    todo_page.add_todo("Buy milk")

    todo_page.expect_todo_visible("Buy milk")
    todo_page.expect_todo_count("1 item left")


def test_add_multiple_todos(page):
    todo_page = TodoPage(page)
    todo_page.open()

    todo_page.add_multiple_todos(TODO_ITEMS)

    for item in TODO_ITEMS:
        todo_page.expect_todo_visible(item)

    todo_page.expect_todo_count("3 items left")


def test_empty_todo_cannot_be_added(page):
    todo_page = TodoPage(page)
    todo_page.open()

    todo_page.add_todo("")

    expect(todo_page.todo_items).to_have_count(0)


def test_whitespace_todo_cannot_be_added(page):
    todo_page = TodoPage(page)
    todo_page.open()

    todo_page.add_todo("     ")

    expect(todo_page.todo_items).to_have_count(0)
