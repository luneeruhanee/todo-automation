from playwright.sync_api import Page, expect


class TodoPage:
    URL = "https://demo.playwright.dev/todomvc/#/"

    def __init__(self, page: Page):
        self.page = page
        self.new_todo = page.locator(".new-todo")
        self.todo_items = page.locator(".todo-list li")
        self.todo_labels = page.locator(".todo-list li label")
        self.toggle_all = page.locator(".toggle-all")
        self.todo_count = page.locator(".todo-count")
        self.clear_completed = page.locator(".clear-completed")
        self.filter_all = page.get_by_role("link", name="All")
        self.filter_active = page.get_by_role("link", name="Active")
        self.filter_completed = page.get_by_role("link", name="Completed")

    def open(self):
        self.page.goto(self.URL)

    def add_todo(self, todo_text: str):
        self.new_todo.fill(todo_text)
        self.new_todo.press("Enter")

    def add_multiple_todos(self, todos: list[str]):
        for todo in todos:
            self.add_todo(todo)

    def complete_todo_by_text(self, todo_text: str):
        todo = self.page.locator(".todo-list li").filter(has_text=todo_text)
        todo.locator(".toggle").check()

    def uncomplete_todo_by_text(self, todo_text: str):
        todo = self.page.locator(".todo-list li").filter(has_text=todo_text)
        todo.locator(".toggle").uncheck()

    def delete_todo_by_text(self, todo_text: str):
        todo = self.page.locator(".todo-list li").filter(has_text=todo_text)
        todo.hover()
        todo.locator(".destroy").click()

    def edit_todo(self, old_text: str, new_text: str):
        todo = self.page.locator(".todo-list li").filter(has_text=old_text)
        todo.locator("label").dblclick()
        edit_input = todo.locator(".edit")
        edit_input.fill(new_text)
        edit_input.press("Enter")

    def filter_by_all(self):
        self.filter_all.click()

    def filter_by_active(self):
        self.filter_active.click()

    def filter_by_completed(self):
        self.filter_completed.click()

    def clear_completed_todos(self):
        self.clear_completed.click()

    def expect_todo_visible(self, todo_text: str):
        expect(self.page.get_by_text(todo_text)).to_be_visible()

    def expect_todo_not_visible(self, todo_text: str):
        expect(self.page.get_by_text(todo_text)).not_to_be_visible()

    def expect_todo_count(self, count_text: str):
        expect(self.todo_count).to_contain_text(count_text)
