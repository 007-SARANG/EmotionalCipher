# Deployment Guide for Vercel

## 🚀 Deploy to Vercel

### Prerequisites
- GitHub account
- Vercel account (free)

### Steps:

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: EmotionCipher with Web GUI"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/EmotionCipher.git
   git push -u origin main
   ```

2. **Deploy on Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will auto-detect settings
   - Click "Deploy"

3. **Get Your Live URL**
   - After deployment, you'll get a URL like: `https://emotion-cipher.vercel.app`
   - Copy this URL

4. **Update README.md**
   - Replace `https://your-app.vercel.app` with your actual Vercel URL
   - In both the badge and the "Live Demo" section

### Environment Variables (if needed)
No environment variables required for basic deployment!

### Custom Domain (Optional)
- In Vercel dashboard → Settings → Domains
- Add your custom domain

---

## 📸 Adding Screenshots

1. Take screenshots of your app:
   - Web GUI landing page
   - Encryption in action
   - Decryption result
   - CLI demo

2. Save them in the `screenshots/` folder:
   - `web-landing.png`
   - `encryption-demo.png`
   - `decryption-demo.png`
   - `cli-demo.png`

3. Commit and push:
   ```bash
   git add screenshots/
   git commit -m "Add screenshots"
   git push
   ```

---

## ✅ Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] Vercel deployment successful
- [ ] Live URL obtained
- [ ] README.md updated with live URL
- [ ] Screenshots captured
- [ ] Screenshots added to repo
- [ ] Final commit and push
- [ ] Test live site
- [ ] Share the link!

---

## 🎉 You're Live!

Once deployed, your EmotionCipher will be accessible worldwide at your Vercel URL!
