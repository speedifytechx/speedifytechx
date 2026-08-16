# Google Search Console Setup Guide for speedifytechx.in

## Step-by-Step Instructions

### 1. Access Google Search Console
1. Go to: **https://search.google.com/search-console**
2. Sign in with your Google account (use speedifytechx@gmail.com if you have one)

### 2. Add Your New Domain

#### Option A: Domain Property (Recommended)
This verifies all versions of your site (http, https, www, non-www)

1. Click **"Add Property"**
2. Select **"Domain"** (not URL prefix)
3. Enter: `speedifytechx.in`
4. Click **"Continue"**

#### Verification via DNS:
1. Google will show you a TXT record
2. Copy the TXT record value (looks like: `google-site-verification=xxxxxxxxxxxxx`)
3. Go to your domain registrar (where you bought speedifytechx.in)
4. Access DNS settings
5. Add new TXT record:
   - **Type:** TXT
   - **Name:** @ (or leave blank)
   - **Value:** [paste the verification code]
   - **TTL:** 3600 (or default)
6. Save changes
7. Return to Google Search Console
8. Click **"Verify"**
9. Note: DNS verification can take 24-48 hours

#### Option B: URL Prefix Property (Faster)
This verifies only the specific URL format

1. Click **"Add Property"**
2. Select **"URL prefix"**
3. Enter: `https://speedifytechx.in`
4. Click **"Continue"**

#### Verification via HTML tag:
1. Google will show you an HTML meta tag
2. Copy the entire tag (looks like: `<meta name="google-site-verification" content="xxxxx">`)
3. Open `index.html` in your code editor
4. Find the line that says:
   ```html
   <meta name="google-site-verification" content="YOUR_GOOGLE_VERIFICATION_CODE">
   ```
5. Replace it with the tag Google gave you
6. Save the file
7. Upload to your server
8. Return to Google Search Console
9. Click **"Verify"**

### 3. Setup for Old Domain (speedifytechx.com)

If you still have access to the old domain:

1. Add `speedifytechx.com` as a property in Google Search Console
2. Go to **Settings** → **Change of Address**
3. Select the new property: `speedifytechx.in`
4. Follow the prompts to notify Google of the domain change
5. Keep both properties active for at least 6 months

### 4. Submit Your Sitemap

Once verified:

1. In Google Search Console, select your property
2. Go to **Sitemaps** (in left menu)
3. Enter sitemap URL: `sitemap.xml`
4. Click **"Submit"**
5. Wait 24-48 hours for Google to process

### 5. Request Indexing for Important Pages

Speed up indexing by manually requesting:

1. Go to **URL Inspection** tool (top of page)
2. Enter each important URL:
   - `https://speedifytechx.in/`
   - `https://speedifytechx.in/services.html`
   - `https://speedifytechx.in/about.html`
   - `https://speedifytechx.in/contact.html`
   - `https://speedifytechx.in/portfolio.html`
3. Click **"Request Indexing"** for each
4. Repeat for all 15 pages

### 6. Monitor Performance

Check these sections regularly:

#### Overview
- Monitor clicks, impressions, CTR, and average position
- Track trends over time

#### Performance
- See which queries bring traffic
- Identify top-performing pages
- Track click-through rates

#### Coverage
- Check for errors or warnings
- Fix any crawl issues
- Monitor indexed pages

#### Enhancements
- Check mobile usability
- Review Core Web Vitals
- Fix any issues

### 7. Setup Email Notifications

1. Go to **Settings** → **Users and permissions**
2. Add team members who should receive alerts
3. Enable notifications for:
   - Critical crawl errors
   - Manual actions
   - Security issues

### 8. Enable All Features

#### Enable Rich Results:
1. Go to **Enhancements**
2. Check for **Rich Results** issues
3. Fix any markup errors

#### Enable Mobile Usability:
1. Go to **Mobile Usability**
2. Fix any mobile issues reported

#### Enable Core Web Vitals:
1. Go to **Core Web Vitals**
2. Monitor page experience signals
3. Improve poor-performing pages

## Common Issues & Solutions

### Issue: Verification Failed
**Solution:**
- Double-check the verification code is correct
- Ensure the meta tag is in the `<head>` section
- Clear browser cache and try again
- Wait a few hours and retry

### Issue: Sitemap Can't Be Read
**Solution:**
- Verify sitemap URL is accessible: `https://speedifytechx.in/sitemap.xml`
- Check XML syntax is valid
- Ensure file is uploaded to server root
- Check robots.txt isn't blocking sitemap

### Issue: Pages Not Indexing
**Solution:**
- Check robots.txt isn't blocking pages
- Verify no `noindex` meta tags
- Ensure 301 redirects are working
- Request indexing manually

### Issue: Old Domain Still Showing
**Solution:**
- Verify 301 redirects are working correctly
- Be patient - can take 2-4 weeks for Google to fully migrate
- Use "Change of Address" tool in Search Console
- Keep old domain redirecting for at least 6 months

## Timeline Expectations

| Timeline | What to Expect |
|----------|----------------|
| Day 1 | Verification complete, sitemap submitted |
| Week 1 | Homepage indexed, starting to appear in search |
| Week 2-4 | Most pages indexed, old domain traffic redirecting |
| Month 2-3 | Full migration complete, rankings stabilizing |
| Month 3-6 | Rankings improving, old domain fully migrated |

## Important Notes

1. **Keep Old Domain Active**: Maintain 301 redirects for at least 6 months
2. **Don't Remove Old Property**: Keep old Search Console property active during migration
3. **Monitor Both Domains**: Check analytics for both domains during transition
4. **Update All Citations**: Change domain on all online listings
5. **Be Patient**: Full migration can take 2-3 months

## Next Steps After Setup

1. ✅ Setup Google Analytics 4
2. ✅ Configure Google Tag Manager
3. ✅ Setup Bing Webmaster Tools
4. ✅ Submit to other search engines (Yandex, Baidu)
5. ✅ Update social media profiles
6. ✅ Update LinkedIn company page
7. ✅ Update Google My Business

## Support Links

- **Google Search Console Help**: https://support.google.com/webmasters
- **Verification Methods**: https://support.google.com/webmasters/answer/9008080
- **Change of Address Tool**: https://support.google.com/webmasters/answer/9370220
- **Sitemap Guidelines**: https://support.google.com/webmasters/answer/183668

---

**Need Help?**
Contact: speedifytechx@gmail.com
Phone: +91 86105 35231
