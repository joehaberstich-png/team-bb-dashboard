# Team BB Workflow Dashboard

## 🎯 Overview
A local workflow management dashboard for tracking agent work, approval processes, and automation triggers.

## ✨ Features

### 1. **Agent Work Tracking**
- Separate sections for each agent/team
- Individual progress tracking
- Task completion status
- Time estimates

### 2. **Approval Workflow**
- **Draft** → **Review** → **Approve/Edit** → **Publish**
- Interactive review interface
- Comment/feedback system
- Version control simulation

### 3. **Automation Triggers**
- Approve → Auto-execute workflow
- Marketing approval → Start promotion
- Email approval → Setup campaigns
- Website approval → Continue development
- System approval → Begin implementation

### 4. **Dashboard Views**
- **Pending Review** - Items awaiting approval
- **Agent Work** - Individual agent progress
- **Workflow Status** - Overall system status
- **Automation Triggers** - Configured automations

## 🚀 Quick Start

### Option 1: Python Server (Recommended)
```bash
# Make server executable
chmod +x server.py

# Start server
python3 server.py
```

### Option 2: Direct File Access
```bash
# Open directly in browser
open index.html  # Mac
xdg-open index.html  # Linux
start index.html  # Windows
```

### Option 3: Simple HTTP Server
```bash
# Python 3
python3 -m http.server 8080

# Then open: http://localhost:8080/
```

## 🖥️ Using the Dashboard

### Reviewing Work:
1. Click **"Review"** on any work item
2. View the complete work content
3. Add comments/feedback
4. Choose:
   - **Approve** - Triggers automation
   - **Request Edit** - Sends back for revisions
   - **Reject** - Returns with feedback

### Agent Sections:
- **Marketing Boss** - Promotion strategies, email campaigns
- **Web Developer** - Website designs, dashboards
- **Operations Boss** - System designs, automation plans

### Automation Triggers:
- Approved work shows **"Trigger Automation"** button
- Click to simulate automation execution
- Shows success/failure messages

## 📁 File Structure
```
workflow-dashboard/
├── index.html          # Main dashboard (complete)
├── server.py           # Python HTTP server
├── README.md           # This file
└── (future files)
```

## 🔧 Customization

### Adding New Work Items:
Edit the `works` object in the JavaScript section of `index.html`:

```javascript
const works = {
    6: {
        title: "New Project",
        agent: "Agent Name",
        status: "review",  // draft, review, approved, published
        progress: 50,
        description: "Brief description",
        content: "Detailed content here...",
        automation: "What happens when approved"
    }
};
```

### Modifying Agents:
Edit the agent sections in the HTML or add new ones in the "Agent Work" tab.

## 🔒 Security Notes (For Production)

### Current (Local):
- No authentication
- No data persistence (in-memory only)
- Demo/simulation mode

### For Production Deployment:
1. **Add Authentication** (GitHub OAuth, Google Auth, etc.)
2. **Database Integration** (SQLite, PostgreSQL, etc.)
3. **Real API Integration** (OpenClaw, social media APIs, etc.)
4. **Password Protection** (Cloudflare Access, .htpasswd, etc.)
5. **HTTPS** (SSL certificate)

## 🚀 Deployment Options

### 1. **GitHub Pages + Cloudflare Access** (Recommended)
- Free private dashboard
- Password protection
- Easy updates

### 2. **Netlify/Vercel**
- Built-in authentication
- Serverless functions
- Easy CI/CD

### 3. **Self-hosted**
- Full control
- Custom integrations
- Requires maintenance

## 📊 Sample Data Included

### Active Projects:
1. **TheDealWizard.com Promotion Strategy** (Marketing Boss)
2. **Small Business Financing Email Templates** (Content Writer)
3. **DrugDoctors.com Home Page Design** (Web Developer)
4. **AllAboutMD.com Automation System Design** (Operations Boss)
5. **Project Dashboard MVP** (Web Developer)

### Workflow Status:
- **3 items** awaiting review
- **2 items** approved (ready for automation)
- **5 agents** active
- **85%** approval rate

## 🐛 Troubleshooting

### Server Won't Start:
```bash
# Check if port is in use
sudo lsof -i :8080

# Kill process using port
sudo kill -9 $(sudo lsof -t -i:8080)

# Try different port
python3 server.py --port 8081
```

### Browser Issues:
- Clear browser cache
- Try different browser
- Check JavaScript console for errors

### File Permissions:
```bash
# Make server executable
chmod +x server.py

# Check Python version
python3 --version
```

## 📈 Next Steps

### Short-term:
1. Test dashboard locally
2. Customize with your projects
3. Add real agent data

### Medium-term:
1. Deploy to GitHub Pages
2. Add password protection
3. Integrate with OpenClaw API

### Long-term:
1. Real-time updates
2. Database backend
3. Advanced analytics
4. Mobile app

## 🤝 Support
For issues or feature requests:
1. Check the JavaScript console for errors
2. Review the README for setup instructions
3. Contact the development team

---

**Happy workflow management!** 🚀