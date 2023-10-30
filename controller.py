from model import NoteBook
import text
import view

def search_note(nb):
    word = view.input_request(text.input_search_word)
    result = nb.find_note(word)
    view.show_book(result, text.not_find(word))

    if result:
        return True

def save_file(nb):
    nb.save_file()
    view.print_message(text.file_succesful(text.action_file[2]))
def save_files(nb):
    nb.save_file()

def move_note():
    try:
        c_id = int(view.input_request(text.input_edit_note_id))
        return c_id
    except:
        view.print_message(text.exception_input)
        return move_note()


def start():
    nb = NoteBook()
    
    while True:
        nb.open_file()
        save_files(nb)
        choice = view.main_menu()
        match choice:
            case 1:
                nb.create_file()
                view.print_message(text.file_succesful(text.action_file[0]))
            case 2:
                nb.open_file()
                view.print_message(text.file_succesful(text.action_file[1]))
            case 3:
                save_file(nb)
            case 4:
                nb.open_file()
                view.show_book(nb, text.empty_book_error)
            case 5:
                nb.open_file()
                new_note = view.input_note(text.input_note, nb)
                nb.add_note(new_note)
                view.print_message(text.note_action(new_note[1], text.operation[0]))
            case 6:
                nb.open_file()
                search_note(nb)
            case 7:
                if search_note(nb):
                    c_id = move_note()
                    if(c_id == 0):
                        c_id = 0
                    elif (c_id >= nb.max_len or c_id < 0):
                        view.print_message(text.exception_input)
                        c_id = move_note()
                    
                    new_note = view.input_note(text.input_edit_note)

                    name = nb.edit_note(c_id, new_note)
                    view.print_message(text.note_action(name, text.operation[1]))
            case 8:
                if search_note(nb):
                    c_id = int(view.input_request(text.input_edit_note_id))
                    name = nb.delete_note(c_id)
                    save_files(nb)
                    view.print_message(text.note_action(name, text.operation[2]))
            case 9:
                if nb.original_book != nb.note_book:
                    if view.input_request(text.confirm_changes).lower() == 'y':
                        save_file(nb)
                view.print_message(text.exit_program)
                break