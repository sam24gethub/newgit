@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    try:
        item_name = request.form["itemName"]
        item_description = request.form["itemDescription"]

        collection.insert_one({
            "itemName": item_name,
            "itemDescription": item_description
        })

        return "To-Do Item submitted successfully!"
    except Exception as e:
        return f"Error: {str(e)}"
