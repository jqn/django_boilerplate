# Django base boilerplate

### PostgreSQL

#### Configuration

- Install PostgreSQL with homebrew
  `$ brew install`

`$ psql` - administer PostgreSQL from the command line

`$ \du` - shows your users for PostgreSQL

`$ \q` - exist PostgreSQL cli

- Download pgAdmin to manage [PostgreSQL](https://www.pgadmin.org/download/pgadmin-4-macos/)
- Launch pgAdmin and login
- From the menu options on the top bar select Object -> create -> Database
- Create a new database called supertuber
- Connect Django to PostgreSQL by going to the SuperTuber project settings.py and add the following

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'supertuber',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

- Create a new database migration `$ python manage.py makemigrations`

- Create the database tables `$ python manage.py migrate`

### Resources

[PostgreSQL Installation](https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/)

### Resources

https://dev.to/coderasha/create-advanced-user-sign-up-view-in-django-step-by-step-k9m
https://github.com/raszidzie/django-advanced-signup-tutorial
https://www.youtube.com/watch?v=FdVuKt_iuSI
https://simpleisbetterthancomplex.com/series/2017/10/09/a-complete-beginners-guide-to-django-part-6.html
https://django.cowhite.com/blog/adding-and-editing-model-objects-using-django-class-based-views-and-forms/
https://www.youtube.com/watch?v=9-ALutreCkE&list=PLLxk3TkuAYnryu1lEcFaBr358IynT7l7H&index=2
https://django-book.readthedocs.io/en/latest/index.html
