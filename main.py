def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()

    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2


def main():
    a = float(input("Введіть довжину сторони a: "))  # вводимо сторону а
    b = float(input("Введіть довжину сторони b: "))  # вводимо сторону b
    c = float(input("Введіть довжину сторони c: "))  # вводимо сторону с

    if is_triangle(a, b, c):  # перевірка if
        print(f"Трикутник зі сторонами {a}, {b}, {c} існує.")

        # логіка перевірки на прямокутність
        if is_right_triangle(a, b, c):
            print("Трикутник є прямокутним.")
            print(f"Гіпотенуза: {max(a, b, c)}")
            print(f"Катет1: {min(a, b, c)}")
            print(f"Катет2: {sorted([a, b, c])[1]}")
        else:
            print("Трикутник не є прямокутним.")
    else:
        print("Трикутник не існує.")


if __name__ == "__main__":
    main()
