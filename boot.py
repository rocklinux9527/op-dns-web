from __init__ import create_app
app = create_app()


def runserver():
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )


if __name__ == '__main__':
    runserver()
