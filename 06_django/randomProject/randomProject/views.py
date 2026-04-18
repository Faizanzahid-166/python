# Create your views here.
from django.shortcuts import render
from datetime import datetime
import random

# 1. home view
def home(request):
    return render(request, "home.html")

# 2 clock view
def clock_view(request):
    current_time = datetime.now().strftime("%H:%M:%S")
    return render(request, "clock.html", {"time": current_time})

# 3. greet view
def greet(request):
    name = ""

    if request.method == "POST":
        name = request.POST.get("name")

    return render(request, "greet.html", {"name": name})

# 4. Calculator view
def calculator(request):
    result = None

    if request.method == "POST":
        num1 = float(request.POST.get("num1", 0))
        num2 = float(request.POST.get("num2", 0))
        operation = request.POST.get("operation")

        # if operation == "add":
        #     result = num1 + num2
        # elif operation == "subtract":
        #     result = num1 - num2
        # elif operation == "multiply":
        #     result = num1 * num2
        # elif operation == "divide":
        #     result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        
        try:   
            num1 = float(num1)
            num2 = float(num2)

            if operation == "add":
                result = num1 + num2
            elif operation == "sub":
                result = num1 - num2
            elif operation == "mul":
                result = num1 * num2
            elif operation == "div":
                result = num1 / num2

        except:
            result = "Error"

    return render(request, "calculator.html", {"result": result})

# 5. Random quote view
def quote(request):
    quotes = [
        "Believe in yourself.",
        "Never give up.",
        "Success is not final.",
        "Dream big and dare to fail.",
        "Stay positive, work hard."
    ]

    random_quote = random.choice(quotes)

    return render(request, "quote.html", {"quote": random_quote})

# 6. 