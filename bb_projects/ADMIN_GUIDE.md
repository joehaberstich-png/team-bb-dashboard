# FlyToAustralia.com — Admin Panel User Guide

## Accessing the Admin Panel

1. Visit **flytoaustralia.com/admin.html** (or locally: open `admin.html` in your browser)
2. Enter the admin password (default: `admin123`)
3. You'll see 4 tabs: Affiliate Links, Page Meta, Settings, Buyer Guide

## Affiliate Links Tab

This is where you manage all 74 affiliate links on the site.

- **Edit a link:** Click in the URL field, paste your affiliate URL, click Save
- **Add a link:** Click "Add Custom Affiliate Link" at the bottom
- **Delete a link:** Click the red trash icon
- **Categories managed:** Flights (Skyscanner, Qantas, Jetstar), Hotels (Booking.com, Airbnb), Tours (Viator), Insurance (World Nomads), Car Rental (Rentalcars.com, Thrifty)

> **Limitation:** This admin panel saves to localStorage only. The 74 hardcoded URLs in the HTML files are not automatically updated. For fully dynamic control, the HTML needs a one-time update to read from localStorage.

## Page Meta Tab

Edit SEO titles and meta descriptions for 14 key pages (Home, Destinations, Visa Guide, Itineraries, Blog, Resources, About, Contact, FAQ, Tour Visa, WHV, Student Visa, Partner Visa, Tools/Calculators).

- Changes save to localStorage
- Copy values into each page's `<title>` and `<meta name="description">` tags

## Settings Tab

- **Admin Password:** Change from default `admin123`
- **Site Name:** Update copyright footer text

## Buyer Guide Tab

Complete handover guide for the Flippa buyer, covering:
- What they get (35 pages, 12 articles, itinerary builder, full source)
- How to deploy (Netlify, Vercel, Cloudflare Pages)
- Monetization (affiliate table, display ads, digital products)
- Traffic strategy (SEO, backlinks, Pinterest, Reddit)
- Maintenance (visa updates, link checks, fresh content)
- Compliance (affiliate disclosure, privacy, email laws)

## For Full Automation (Future Upgrade)

To make the admin panel actually control the live site:
1. Replace hardcoded `href` values in each HTML page with JavaScript reading from `localStorage.getItem('flytoaustralia_affiliates')`
2. Add a serverless backend to persist changes across devices
3. Deploy on Vercel/Netlify with serverless functions
