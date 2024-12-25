import os
import logging
from collections import namedtuple

logging.basicConfig(
    filename="directory_info.log",
    level=logging.INFO,
    format="%(asctime)s = %(levelname)s - %(message)s"
)

FileInfo = namedtuple("FileInfo", ["name", "extension", "is_directory", "parent_directory"])

def collect_directory_info(directory_path):
    if not os.path.isdir(directory_path):
        logging.error(f"Указанный путь не является директорией: {directory_path}")
        raise NotADirectoryError(f"{directory_path} не является директорией")

    directory_info = []

    for root, dirs, files in os.walk(directory_path):
        parent_directory = os.path.basename(root)

        for dir_name in dirs:
            info = FileInfo(
                name=dir_name,
                extension=None,
                is_directory=True,
                parent_directory=parent_directory
            )
            directory_info.append(info)
            logging.info(f"Обраюотан каталог: {info}")

        for file_name in files:
            name, extension = os.path.splitext(file_name)
            info = FileInfo(
                name=name,
                extension=extension.lstrip("."),
                is_directory=False,
                parent_directory=parent_directory
            )
            directory_info.append(info)
            logging.info(f"Обработан файл: {info}")

    return directory_info


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Сбор информации с содержимым директории")
    parser.add_argument("directory", type=str, help="Путь до директории")
    args = parser.parse_args()

    try:
        directory_info = collect_directory_info(args.directory)
        print(f"Информация о содержимом директории '{args.directory}' сохранена в лог.")
    except Exception as e:
        logging.error(f"Ошибка при обработке: {e}")
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()