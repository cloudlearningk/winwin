import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        num1 = float(body.get("num1"))
        num2 = float(body.get("num2"))
        operation = body.get("operation")

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return func.HttpResponse("Division by zero not allowed", status_code=400)
            result = num1 / num2
        else:
            return func.HttpResponse("Invalid operation", status_code=400)

        return func.HttpResponse(json.dumps({"result": result}), mimetype="application/json")

    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=400)
