from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1", 0))
            num2 = float(request.form.get("num2", 0))
            operation = request.form.get("operation")
            
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: División por cero"
            else:
                result = "Operación no válida"
        except ValueError:
            result = "Error: Ingresa números válidos"
    
    return render_template("calculator.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)