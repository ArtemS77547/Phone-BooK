main_menu = [
    "Главное меню",
    "Открыть справочник",
    "Сохранить справочник",
    "Показать контакты",
    "Создать контакт",
    "Найти контакт",
    "Изменить контакт",
    "Удалить контакт",
    "Выход"
]

choice_main_menu = f"Выберете пункт меню ({1}={len(main_menu)-1}):"
choice_main_menu_error = f"Нужно ввести число от 1 до 1 {len(main_menu)-1}!"

phone_book_opened_successful = "телефонная книга открыта успешно!"
phone_book_saved_successful = "телефонная книга сохранина успешно!"


empti_phone_book_error = "Телефонная книга пуста или не открыта!"


input_new_contact = [
    "Введите имя контакта:",
    "Ввидите номер контакта:",
    "Ввидите коммент для контакта:",
]

no_changes = "Или ENTER, что бы оставить без измененний"

edit_contact = [
    f"Ввидите новое имя ({no_changes}): ",
    f"Ввидите новый телефон ({no_changes}): ",
    f"Ввидите новый комментарий ({no_changes}): ",
]


input_search_word = "Ввидите слово для поиска: "
input_search_word_for_edit = "Ввидите слово для поиска который хотите изменить: "
input_search_word_for_delete = "Ввидите слово для поиска который хотите удалить: "
input_id_for_edit = "Ввидите ID контакта, который хотите изменить: "
input_id_for_delete = "Ввидите ID  контакта который хотите удалить: "


def new_contact_added_successful(name: str) -> str:
    return f'Контакт "{name}" успешно добавлен!'


def faind_contact_no_result(word: str) -> str:
    return f'Контакты содержащие "{word}" не найдины!'


def edit_contact_succesful(name) -> str:
    return f'Контакт "{name}" успешно обновлен!'


def delete_contact_succesful(name) -> str:
    return f'Контакт "{name}" успешно удвлён!'
