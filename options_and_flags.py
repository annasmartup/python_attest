import argparse

def main():
    parser = argparse.ArgumentParser(description="Обработка числа и строки с дополнительными опциями")

    parser.add_argument("number", type=int, help="Число для обработки")
    parser.add_argument("text", type=str, help="Строка для обработки")

    parser.add_argument("--verbose", action="store_true", help="Выводить доп информацию")
    parser.add_argument("--repeat", type=int, default=1, help="Количество повторений строки в выводу")

    args = parser.parse_args()

    if args.verbose:
        print(f"Получено число: {args.number}")
        print(f"Получена строка: {args.text}")
        print(f"Количество повторений: {args.repeat}")

    for _ in range(args.repeat):
        print(args.text)

if __name__ == "__main__":
    main()

