menu = ['Главное меню',
        'Создать файл записей',
        'Открыть файл',
        'Сохранить файл',
        'Показать записи',
        'Создать запись',
        'Найти записи',
        'Изменить запись',
        'Удалить запись',
        'Выход']

input_menu = 'Выберите пункт меню: '
input_menu_error = f'Ввести нужно ЧИСЛО (от 1 до {len(menu) - 1})'

empty_book_error = 'Записей нет'

input_note = ['Введите название новой записи: ', 
                 'Текст: ', 
                 'Комментарий: ']

input_edit_note = ['Введите новое название записи или ENTER, чтобы оставить без изменений: ',
                      'Новый текст или ENTER, чтобы оставить без изменений: ', 
                      'Новый комментарий или ENTER, чтобы оставить без изменений: ']

input_search_word = 'Введите ключевое слово для поиска: '

input_edit_note_id = 'Введите ID записи, который хотите изменить: '
input_del_note_id = 'Введите ID записи, который хотите удалить: '

operation = ['создана', 'изменена', 'удалена']
action_file = ['создана', 'загружена', 'сохранена']

confirm_changes = 'У вас есть несохраненные изменения! Сохранить? (y/n) '
exit_program = 'До свидания! До новых встреч!'
exception_input = 'Вы ввели некорректные данные!'
def not_find(word):
    return f'Запись, содержащая {word}, не найден'

def note_action(name: str, action: str) -> str:
    return f'Запись {name} успешно {action}!'


def file_succesful(action_file: str) -> str:
    return f'Записи успешно {action_file}'

