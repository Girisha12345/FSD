# Deployment Configuration for Render.com

## Environment Variables to set in Render Dashboard

Set these in Render's Environment section:

```
DEBUG=False
SECRET_KEY=your-generated-secret-key-here
ALLOWED_HOSTS=yourdomain.onrender.com,127.0.0.1
DATABASE_URL=postgresql://user:password@host/dbname
```

## Steps to Deploy on Render

1. Commit and push to GitHub
2. Go to https://render.com
3. Create new Web Service
4. Connect GitHub repository (FSD)
5. Set runtime: Python 3
6. Set build command: `pip install -r requirements.txt`
7. Set start command: `gunicorn chanakya_project.wsgi --log-file -`
8. Add environment variables as above
9. Create PostgreSQL database on Render
10. Update DATABASE_URL in environment
11. Deploy

## For Static Files

Add to settings.py for production:
- STATIC_ROOT
- STATIC_URL = '/static/'

Render auto-collects static files during build.
