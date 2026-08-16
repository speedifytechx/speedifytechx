# ⚡ Quick Start Guide - Domain Migration

## 🎯 5 Critical Steps (Do These Now!)

### Step 1: Upload All Files (10 minutes)
Upload these updated files to your web server:
```
✓ All HTML files (index.html, about.html, services.html, etc.)
✓ sitemap.xml
✓ robots.txt
✓ .htaccess (if using Apache/cPanel)
```

### Step 2: Get Google Verification Code (5 minutes)
1. Visit: https://search.google.com/search-console
2. Click "Add Property"
3. Enter: `speedifytechx.in`
4. Choose "HTML tag" verification
5. Copy the code (looks like: `content="abc123xyz..."`)
6. **Save this code** - you'll need it in Step 4

### Step 3: Get Bing Verification Code (5 minutes)
1. Visit: https://www.bing.com/webmasters
2. Click "Add a site"
3. Enter: `speedifytechx.in`
4. Choose "Meta tag" verification
5. Copy the code (looks like: `content="def456uvw..."`)
6. **Save this code** - you'll need it in Step 4

### Step 4: Update Verification Codes (10 minutes)
In **EVERY HTML file**, find and replace:

**Find:**
```html
<meta name="google-site-verification" content="YOUR_GOOGLE_VERIFICATION_CODE">
```

**Replace with:**
```html
<meta name="google-site-verification" content="[YOUR ACTUAL GOOGLE CODE]">
```

**Find:**
```html
<meta name="msvalidate.01" content="YOUR_BING_VERIFICATION_CODE">
```

**Replace with:**
```html
<meta name="msvalidate.01" content="[YOUR ACTUAL BING CODE]">
```

💡 **Tip:** Use Find & Replace (Ctrl+H) in your code editor to update all files at once.

### Step 5: Complete Verification & Submit Sitemaps (10 minutes)

**Google:**
1. Return to Google Search Console
2. Click "Verify"
3. Go to Sitemaps
4. Enter: `sitemap.xml`
5. Click "Submit"

**Bing:**
1. Return to Bing Webmaster Tools
2. Click "Verify"
3. Go to Sitemaps
4. Enter: `sitemap.xml`
5. Click "Submit"

## ✅ Done!

Your website is now properly configured with:
- ✅ New domain (speedifytechx.in)
- ✅ Search engine verification
- ✅ Sitemap submitted
- ✅ 301 redirects from old domain
- ✅ Enhanced SEO meta tags
- ✅ Local SEO for Chennai, India

## 🔔 Don't Forget

1. **Update LinkedIn:** http://linkedin.com/company/speedifytechx/
   - Edit page → Update website to `speedifytechx.in`

2. **Monitor Progress:**
   - Check Google Search Console weekly
   - Check Bing Webmaster Tools weekly
   - Track rankings and traffic

3. **Keep Old Domain Active:**
   - Don't cancel speedifytechx.com hosting
   - Keep 301 redirects active for 6-12 months

## 📚 Full Documentation

- `DOMAIN_MIGRATION_COMPLETE.md` - Complete overview
- `SEO_CHECKLIST.md` - Detailed SEO tasks
- `GOOGLE_SEARCH_CONSOLE_SETUP.md` - Google setup guide
- `BING_WEBMASTER_SETUP.md` - Bing setup guide

## 🆘 Need Help?

**Email:** speedifytechx@gmail.com  
**Phone:** +91 86105 35231

---

**Estimated Time:** 40 minutes total  
**Difficulty:** Easy (just follow the steps!)  
**Impact:** High (proper SEO indexing for your new domain)
