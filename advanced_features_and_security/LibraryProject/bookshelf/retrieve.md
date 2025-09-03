>>book = Book.objects.get(title = "1984")
>>book.__dict__
{'_state': <django.db.models.base.ModelState object at 0x00000195BE405480>, 'id': 1, 'title': '1984', 'author': 'Ge
orge Orwell', 'publication_year': 1949}