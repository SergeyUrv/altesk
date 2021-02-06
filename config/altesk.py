[program:altesk]
command=/var/www/venv/bin/gunicorn altesksite.wsgi:application -c /var/www/altesk/altesksite/config/gunicorn.conf.py
directory=/var/www/altesk/altesksite
user=john
autorestart=true
redirect_stderr=true
stdout_logfile = /var/www/altesk/logs/debug.log