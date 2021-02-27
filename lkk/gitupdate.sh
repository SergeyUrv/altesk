#!/bin/bash
function pull {
  source /var/www/pyapps/venv-altesk-deploy/bin/activate
  cd /var/www/pyapps/altesk-deploy
  git pull origin dev
  python3 manage.py makemigrations
  python3 manage.py migrate
  supervisorctl restart altesk-deploy
}
pull;