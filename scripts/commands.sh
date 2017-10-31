#!/bin/bash


case $1 in
    adduser)
        docker-compose run web python manage.py adduser
        ;;
    initdb)
        docker-compose run web python manage.py initdb
        ;;
    dropdb)
        docker-compose run web python manage.py dropdb
        ;;
    *)
        echo invalid command
        ;;
esac
