def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)

        if denom == 0:
            return "Error: Division by zero is undefined."

        return f"Result: {num / denom:.2f}"

    except ValueError:
        return "Error: Both inputs must be numeric values."