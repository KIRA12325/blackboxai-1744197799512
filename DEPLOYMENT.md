# MeditAI Deployment Checklist

## Pre-Deployment
- [ ] Set DEBUG = False in settings.py
- [ ] Generate new SECRET_KEY
- [ ] Configure production database
- [ ] Set up email backend
- [ ] Add domain to ALLOWED_HOSTS

## Static Files
- [ ] Run `python manage.py collectstatic`
- [ ] Configure web server (Nginx/Apache) to serve static files
- [ ] Set up media file storage (S3 or local)

## Web Server
- [ ] Install and configure Gunicorn
- [ ] Set up process manager (systemd/supervisor)
- [ ] Configure reverse proxy (Nginx)

## Security
- [ ] Set up HTTPS/SSL
- [ ] Configure security headers
- [ ] Set up proper file permissions

## Monitoring
- [ ] Configure error logging
- [ ] Set up monitoring/alerting
- [ ] Create backup strategy

## Post-Deployment
- [ ] Test all functionality
- [ ] Verify cron jobs
- [ ] Set up CI/CD pipeline
