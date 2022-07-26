def app(environ, start_response):
    data = b"Hello, World at " + environ['PATH_INFO'].encode()
    print(environ)
    print(environ['PATH_INFO'])
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])