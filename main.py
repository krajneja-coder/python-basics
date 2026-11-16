DISCOUNT = 0.10
DELIVERY_PRICE = 50.0

print("=== КАЛЬКУЛЯТОР ПОКУПОК ===")

name: str = input("Введіть ваше ім'я: ")
product: str = input("Назва товару: ")
price: float = float(input("Ціна товару (грн): "))
quantity: int = int(input("Кількість товару: "))
has_card: bool = input("Є картка знижок? (так/ні): ").lower() == "так"

total: float = price * quantity

if price > 0 and quantity > 0:
    if has_card:
        discount: float = total * DISCOUNT
    else:
        discount: float = 0.0

    discount_status: str = "Так" if discount > 0 else "Ні"

    final_price: float = total - discount

    if final_price >= 1000:
        final_price = final_price + DELIVERY_PRICE
        delivery: str = "50 грн"
    elif final_price >= 500:
        delivery: str = "Безкоштовно"
    else:
        delivery: str = "Безкоштовно"

    print("\nОберіть спосіб оплати:")
    print("1 - Готівка")
    print("2 - Картка")
    print("3 - Онлайн")

    payment: str = input("Ваш вибір: ")

    match payment:
        case "1":
            payment_name: str = "Готівка"
        case "2":
            payment_name: str = "Банківська картка"
        case "3":
            payment_name: str = "Онлайн"
        case _:
            payment_name: str = "Не вибрано"

    customer: str = str(name)

    print("\n===== РЕЗУЛЬТАТ ПОКУПКИ =====")
    print(f"Покупець: {customer}")
    print(f"Товар: {product}")
    print(f"Кількість: {quantity}")
    print(f"Початкова сума: {total:.2f} грн")
    print(f"Знижка: {discount:.2f} грн")
    print(f"Знижку застосовано: {discount_status}")
    print(f"Доставка: {delivery}")
    print(f"Спосіб оплати: {payment_name}")
    print(f"До сплати: {final_price:.2f} грн")

else:
    print("Помилка! Ціна та кількість повинні бути більшими за 0.")
