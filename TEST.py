from main_page import SearchHelper


def test_todo(browser):
    todomainpage = SearchHelper(browser)
    todomainpage.go_to_site()
    todomainpage.enter_word('Test')
    todomainpage.create_todo()
    todo = todomainpage.check_created_todo()
    assert "Test" in todo

