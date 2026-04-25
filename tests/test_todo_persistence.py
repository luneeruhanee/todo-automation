from pages.todo_page import TodoPage


def test_todo_persist_after_reload(page):
    todo_page = TodoPage(page)
    todo_page.open()

    todo_page.add_todo("Buy milk")
    page.reload()

    todo_page.expect_todo_visible("Buy milk")


def test_completed_status_persist_after_reload(page):
    todo_page = TodoPage(page)
    todo_page.open()

    todo_page.add_todo("Buy milk")
    todo_page.complete_todo_by_text("Buy milk")
    page.reload()

    todo = page.locator(".todo-list li").filter(has_text="Buy milk")
    assert "completed" in todo.get_attribute("class")
