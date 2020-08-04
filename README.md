# movies_api

# Development environment

```shell script
pip install -r requirements_dev.txt
docker-compose  up -d 
./manage.py migrate
./manage.py collectstatic
./manage.py runserver
```
