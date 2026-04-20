# Deployment Guide: Chanakya University Inquiry System

## Platform Recommendation: RENDER (Not Vercel)

### Why Render Over Vercel?

| Feature | Render | Vercel |
|---------|--------|--------|
| Django Support | ✅ Native support | ❌ Serverless only |
| Database | ✅ PostgreSQL included | ❌ Limited options |
| Background Tasks | ✅ Full app server | ❌ Not suitable |
| Cost | ✅ Free tier available | ✅ Free tier available |
| Ease for Django | ✅ Purpose-built | ❌ Complex workaround |

**Conclusion**: Use **Render.com** - it's built for Django/full-stack apps like yours.

---

## Step-by-Step Deployment on Render.com

### Prerequisites
- GitHub account with project pushed (✅ Done)
- Render account (create at https://render.com)
- Credit card (for database backup, free tier available)

### Step 1: Create Render Account
1. Go to https://render.com
2. Click "Get Started"
3. Sign in with GitHub
4. Authorize Render to access your repositories

### Step 2: Create Web Service
1. Dashboard → "New +"
2. Select "Web Service"
3. Search for "FSD" repository
4. Select Girisha12345/FSD
5. Click "Connect"

### Step 3: Configure Web Service
Fill in the form:
- **Name**: chanakya-university (auto-filled, can change)
- **Environment**: Python 3
- **Region**: Choose closest to you (e.g., India/Singapore)
- **Branch**: main
- **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- **Start Command**: `gunicorn chanakya_project.wsgi`

### Step 4: Add Environment Variables
Click "Advanced" → "Add Environment Variable"

Add these one by one:
```
DEBUG=False
SECRET_KEY=your-super-secret-key-generate-one-here
ALLOWED_HOSTS=yourdomain.onrender.com
```

To generate SECRET_KEY, run in terminal:
```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 5: Create PostgreSQL Database
1. Dashboard → "New +"
2. Select "PostgreSQL"
3. Name: chanakya-db
4. Region: Same as web service
5. PostgreSQL Version: 15
6. Click "Create Database"
7. Wait for creation (2-5 minutes)

### Step 6: Connect Database to Web Service
1. Go back to Web Service settings
2. Add Environment Variable:
```
DATABASE_URL=postgresql://user:password@host:5432/dbname
```
(Copy from PostgreSQL service info)

### Step 7: Create Web Service
1. Click "Create Web Service"
2. Wait for build (2-5 minutes)
3. Watch logs in "Logs" tab

### Step 8: Run Migrations
Once deployed:
1. Click "Shell" tab
2. Run:
```
python manage.py migrate
python manage.py seed_sample_data
python manage.py createsuperuser
```

### Step 9: Access Your App
- Main site: https://chanakya-university.onrender.com
- Admin: https://chanakya-university.onrender.com/admin/

---

## Deployment Checklist

- [x] Code pushed to GitHub
- [x] requirements.txt created
- [x] Procfile created
- [x] runtime.txt created
- [x] settings.py updated for production
- [ ] Create Render account
- [ ] Connect GitHub repository
- [ ] Configure web service
- [ ] Create PostgreSQL database
- [ ] Set environment variables
- [ ] Deploy and run migrations
- [ ] Load sample data
- [ ] Test all API endpoints
- [ ] Access admin panel

---

## Post-Deployment Testing

Once live on Render:

1. **Home Page**
   - Open https://yourdomain.onrender.com
   - Popup should appear
   - Fill and submit form
   - Should see success message

2. **APIs**
   - https://yourdomain.onrender.com/api/courses/
   - https://yourdomain.onrender.com/api/faculty/1/
   - https://yourdomain.onrender.com/api/hostel/
   - https://yourdomain.onrender.com/api/transport/

3. **Admin**
   - https://yourdomain.onrender.com/admin/
   - Login with superuser credentials
   - Check Inquiry table for submissions

---

## Troubleshooting

### 502 Bad Gateway Error
- Check logs in Render dashboard
- Verify environment variables are set
- Ensure SECRET_KEY is not empty

### Database Connection Error
- Verify DATABASE_URL is correct
- Check PostgreSQL service is running
- Run migrations in Shell

### Static Files Not Loading
- Run `python manage.py collectstatic --noinput` in Shell
- Check STATIC_ROOT is set (already done)

### Import Errors
- Verify all packages in requirements.txt
- Rebuild: Dashboard → Manual Deploy

---

## Custom Domain (Optional)

1. Purchase domain from registrar (GoDaddy, Namecheap, etc.)
2. In Render dashboard: Settings → Custom Domains
3. Add your domain
4. Update DNS records per Render instructions

---

## Cost Breakdown

- **Web Service**: Free tier (0.5 vCPU, 512 MB RAM) → $7/month paid
- **PostgreSQL**: Free tier (256 MB) → $15/month paid
- **Total Free**: Full hosting
- **Total Paid**: ~$22/month for production

---

## Monitoring and Logs

Access live logs:
1. Render Dashboard → your web service
2. Click "Logs" tab
3. Real-time server output visible

Monitor:
- Build errors
- Runtime exceptions
- Request latency
- Database queries

---

## Rollback

If deployment breaks:
1. Go to Dashboard
2. Click "Deploys" tab
3. Select previous working version
4. Click "Deploy"

---

## Next Steps After Deployment

1. Set up error tracking (Sentry)
2. Add CDN for static files (Cloudflare)
3. Enable SSL (auto on Render)
4. Set up email notifications (SendGrid)
5. Create backup strategy

---

## Support Links

- Render Docs: https://render.com/docs
- Django Docs: https://docs.djangoproject.com/
- PostgreSQL: https://www.postgresql.org/docs/
