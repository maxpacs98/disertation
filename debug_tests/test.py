def test_build_error_handler(app):
    # Test base case, a URL which results in a BuildError.
    with app.test_request_context():
        pytest.raises(BuildError, flask.url_for, "spam")

    # Verify the error is re-raised if not the current exception.
    try:
        with app.test_request_context():
            flask.url_for("spam")
    except BuildError as err:
        error = err
    try:
        raise RuntimeError("Test case where BuildError is not current.")
    except RuntimeError:
        pytest.raises(BuildError, app.handle_url_build_error, error, "spam", {})

    # Test a custom handler.
    def handler(error, endpoint, values):
        # Just a test.
        return "/test_handler/"

    app.url_build_error_handlers.append(handler)
    with app.test_request_context():
        assert flask.url_for("spam") == "/test_handler/"
