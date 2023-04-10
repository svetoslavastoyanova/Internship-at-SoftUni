def shopping_cart(*args):
    is_stopped = False
    result = ''
    cart_with_products = {}
    product_limits = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2
    }
    for i in range(0, len(args), 2):
        key = args[i]
        if key == "Stop":
            is_stopped = True
            break
        else:
            value = args[i + 1].lower()
            if key not in cart_with_products:
                cart_with_products[key] = []
            if value in cart_with_products[key]:
                continue
            cart_with_products[key].append(value)

            if len(cart_with_products[key]) >= product_limits[key]:
                break

    if is_stopped and not cart_with_products:
        return f'No products in the cart!'
    else:
        sorted_products = sorted(cart_with_products.items(), key=lambda x: (-len(x[1]), x[0]))
        for pairs in sorted_products:
            meal_type = pairs[0]
            meal_products = pairs[1]
            sorted_list_of_products = sorted(meal_products)
            result += f"{meal_type}:\n"
            for product in sorted_list_of_products:
                result += f" - {product}\n"
        return result.strip()

