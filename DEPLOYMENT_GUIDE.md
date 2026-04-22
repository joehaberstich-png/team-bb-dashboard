# Dashboard Deployment Guide

## QUICK DEPLOYMENT STEPS:

### 1. CREATE GITHUB REPOSITORY
- Go to https://github.com/new
- Repository name: `team-bb-dashboard` (or your choice)
- **IMPORTANT**: Check "Add a README file"
- Click "Create repository"

### 2. UPLOAD FILES TO GITHUB
```bash
# Clone your new repository
git clone https://github.com/YOUR-USERNAME/team-bb-dashboard.git
cd team-bb-dashboard

# Copy ALL files from dashboard-deploy folder to this repository
# (Copy index.html, README.md, CNAME, .nojekyll, etc.)

# Add, commit, and push
git add .
git commit -m "Initial dashboard deployment"
git push origin main
```

### 3. ENABLE GITHUB PAGES
- Go to your repository on GitHub
- Click "Settings" → "Pages"
- Under "Source", select "Deploy from a branch"
- Branch: `main` (or `master`)
- Folder: `/` (root)
- Click "Save"

### 4. SETUP CUSTOM DOMAIN (OPTIONAL)
- In GitHub Pages settings, add your custom domain
- Update CNAME file with your actual domain
- Wait for DNS propagation (5-60 minutes)

### 5. CLOUDFLARE PROTECTION (RECOMMENDED)
1. Add your domain to Cloudflare
2. Update nameservers at your domain registrar
3. In Cloudflare, go to "Access" → "Applications"
4. Create new self-hosted application
5. Set URL to your dashboard URL
6. Add authentication (email, GitHub, Google, etc.)

## ACCESS YOUR DASHBOARD:
- GitHub Pages URL: `https://YOUR-USERNAME.github.io/team-bb-dashboard/`
- Custom Domain: `https://your-domain.com`

## TROUBLESHOOTING:
- **404 Error**: Wait 1-2 minutes after enabling Pages
- **Mixed Content**: Ensure using HTTPS
- **CNAME not working**: Check DNS settings at registrar
- **Authentication issues**: Verify Cloudflare Access rules

## SECURITY NOTES:
1. **ALWAYS** add password protection via Cloudflare Access
2. Use HTTPS only
3. Regularly update the dashboard
4. Monitor access logs