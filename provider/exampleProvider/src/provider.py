from flask import Flask, abort, jsonify

fakedb = {"id": "123", "todo": ["Cheese"]}  # Use a simple dict to represent a database
app = Flask(__name__)


@app.route("/todo/<id>")
def get_todo_for_id(id: str):
    """Handle requests to retrieve a single user from the simulated database.
    :param id: ID of the list to "search for"
    :return: The list data if found, None (HTTP 404) if not
    """
    user_data = fakedb.get('todo')
    if not user_data:
        app.logger.debug(f"GET todo list for: '{id}', HTTP 404 not found")
        abort(404)
    print(user_data)
    response = jsonify(user_data)
    app.logger.debug(f"GET todo list for: '{id}', returning: {response.data}")
    return response


if __name__ == "__main__":
    app.run(debug=True, port=5001)