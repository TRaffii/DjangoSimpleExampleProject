#!/bin/bash
python manage.py migrate                  # Apply database migrations
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'password12345')" | python manage.py shell
python manage.py runserver 0.0.0.0:8080