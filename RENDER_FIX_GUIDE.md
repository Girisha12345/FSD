# Render Deployment Fix Guide

## Problem Encountered ❌

Render deployment failed with:
```
ModuleNotFoundError: No module named 'app'
==> Running 'gunicorn app:app'
```

**Root Cause**: Render ignored the Procfile and used its default start command `gunicorn app:app` instead of your Django WSGI module.

---

## Solution ✅

### Step 1: Update Render Web Service Settings

**Go to your Render Dashboard:**

1. Click on your "chanakya-university" Web Service
2. Go to **Settings** tab (bottom left)
3. Scroll to **Start Command**
4. **REPLACE** the current command with:

```
gunicorn chanakya_project.wsgi:application --bind 0.0.0.0:$PORT
```

5. Click **Save**

### Step 2: Verify Build Command

Still in Settings, check **Build Command**:

Should be:
```
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

If different, update it.

### Step 3: Deploy

1. Go to **Deploys** tab
2. Click **Manual Deploy** → **Deploy latest commit**
3. Watch the logs for success

---

## What Changed ✅

### Procfile (Updated)
```
web: gunicorn chanakya_project.wsgi:application --bind 0.0.0.0:$PORT
release: python manage.py migrate
```

**Key Changes:**
- Added `:application` (explicit WSGI app reference)
- Added `--bind 0.0.0.0:$PORT` (Render uses $PORT environment variable)
- Removed `--log-file -` (Render handles logs automatically)

---

## Files Updated on GitHub ✅

- ✅ Procfile (corrected)
- ✅ build.sh (build script for better transparency)

New commits will be pushed automatically. You can then trigger a rebuild on Render.

---

## Troubleshooting Checklist

- [ ] Start Command is: `gunicorn chanakya_project.wsgi:application --bind 0.0.0.0:$PORT`
- [ ] Build Command includes: `collectstatic --noinput`
- [ ] Environment variables set (DEBUG, SECRET_KEY, DATABASE_URL, ALLOWED_HOSTS)
- [ ] PostgreSQL database created and DATABASE_URL updated
- [ ] Clicked "Manual Deploy"

---

## Expected Success Indicators

After deploy completes:
1. Logs show: `Listening at: http://0.0.0.0:xxxxx`
2. No `ModuleNotFoundError`
3. Service is marked as "Live"
4. You can access https://yourdomain.onrender.com

---

## If Still Failing

1. Check logs for any Python import errors
2. Verify `chanakya_project/wsgi.py` exists and has `application` defined
3. Ensure `settings.py` can be imported (check for syntax errors)
4. Run locally: `gunicorn chanakya_project.wsgi:application` to verify it works

---

## Quick Recovery Steps

1. **In Render Dashboard:**
   - Go to Web Service → Settings
   - Set Start Command to: `gunicorn chanakya_project.wsgi:application --bind 0.0.0.0:$PORT`
   - Click Save
   - Go to Deploys → Manual Deploy

2. **Wait 3-5 minutes** for rebuild

3. **Check logs** - should say "Listening at..."

That's it! 🚀
