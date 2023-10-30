from copy import deepcopy

class Note: 
    def __init__(self, ID: int, name: str, note: str, comment: str):
        self.ID = ID
        self.name = name
        self.note = note
        self.comment = comment
    
    def full(self):
        return f'{self.ID}: {self.name} {self.note} {self.comment}'
        

class NoteBook:
    
    def __init__(self, note_book: dict = None, PATH: str = 'notes.cvs') -> None:
        self.PATH = PATH
        if note_book is None:
            self.note_book: dict[int, Note] = {}
        else:
            self.note_book = note_book
        self.original_book = {}


    def create_file(self):
        with open(self.PATH, 'w', encoding='UTF-8') as file:
            file.write('')

    def open_file(self):
        try:
            with open(self.PATH, 'r', encoding='UTF-8') as file:
                data = file.readlines()
            for i, note in enumerate(data, 1):
                note = note.strip().split(';')
                self.note_book[i] = Note(*note)
        except:
            with open(self.PATH, 'w', encoding='UTF-8') as file:
                file.write('')
        self.original_book = deepcopy(self.note_book)

    def save_file(self):
        data = []
        for notef in self.note_book.values():
            try:
                notes = ';'.join(map(str, notef))
            except:
                notes = notef.ID + ";" + notef.name + ';' + notef.note + ';' + notef.comment
            data.append(notes)
        data = '\n'.join(data)
        with open(self.PATH, 'w', encoding='UTF-8') as file:
            file.write(data)
    def maxID(self):
        if self.note_book:
            return max(self.note_book)
        return 0
    def add_note(self, new_note: list[str]):
        if not self.note_book:
            c_id = 1
        else:
            c_id = max(self.note_book) + 1
        self.note_book[c_id] = new_note
        print("Успешно")
        print(new_note[0])

    def find_note(self, word: str):
        result = {}
        
        for c_id, note in self.note_book.items():
            if word.lower() in note.full():
                result[c_id] = note
                break
        return NoteBook(result)

    def edit_note(self, c_id: int, new_note: list[str]):
        current_note = self.note_book.get(c_id)
        note = []
        for i in range(len(new_note)):
            if new_note[i]:
                note.append(new_note[i])
            else:
                note.append(current_note[i])
        self.note_book[c_id] = note
        return note[0]

    def delete_note(self, c_id: int) -> str:
        return self.note_book.pop(c_id)
    
    def max_len(self, option: str) -> int:
        result = []
        for notes in self.note_book.values():
            if option == 'name':
                item = notes.name
            elif option == 'note':
                item = notes.note
            else:
                item = notes.comment
            result.append(item)
        if(len(result) == 0):
            return 0
        else:
            return len(max(result, key=len))