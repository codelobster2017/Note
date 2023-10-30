import text
from model import NoteBook

def main_menu():
    for i, item in enumerate(text.menu):
        if i == 0:
            print(item)
        else:
            print(f'\t{i}. {item}')
    while True:
        choice = input(text.input_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.menu):
            return int(choice)
        else:
            print(text.input_menu_error)



def print_message(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')


def show_book(book: NoteBook, msg: str):
    if book:
        if(len(book.note_book) == 0):
            print_message("Ничего не найдено!")
        else:
            print('\n' + '*' * (book.max_len("name") + book.max_len("note") + book.max_len("comment")  + 8))
            for i, note in book.note_book.items():
                print(f'{i:>3}. {note.name:<{book.max_len("name")}} {note.note:<{book.max_len("note")}} {note.comment:<{book.max_len("comment")}}')
            print('*' * (book.max_len("name") + book.max_len("note") + book.max_len("comment") + 8) + '\n')
    else:
        print_message(msg)


def input_note(msg: str, nb: NoteBook) -> list[str]:
    note = []
    note.append(nb.maxID()+1)
    for input_text in msg:
        note.append(input(input_text))
    return note

def input_request(msg: str) -> str:
    return input(msg)
