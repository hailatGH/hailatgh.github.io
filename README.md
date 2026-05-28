# Personal Website

Personal website and portfolio for Hailemichael Atrsaw Tibebu.

🌐 **Live Site:** [Your GitHub Pages URL will be here]

## 🏗️ Project Structure

```
.
├── index.html              # Main homepage
├── style.css               # Stylesheet
├── tools/                  # Tools and utilities
│   └── cv_generator/       # CV generator tool
│       ├── main.py         # PDF generation script
│       ├── src/            # HTML/CSS source for CV
│       │   ├── main.html
│       │   └── styles.css
│       └── docs/           # Generated CV PDFs
└── .github/
    └── workflows/
        └── deploy.yml      # GitHub Pages deployment
```

## 🚀 Features

- **Clean, Minimalist Design** - Simple and professional personal homepage
- **Responsive Layout** - Works perfectly on all devices
- **Featured Projects** - Showcase your best work
- **Skills Overview** - Highlight your technical expertise
- **CV Download** - Direct link to your latest CV
- **Auto-Deploy** - Automatically deploys to GitHub Pages on every push

## 📦 CV Generator Tool

The CV generator is located in `tools/cv_generator/` and allows you to:
- Generate PDF from HTML/CSS
- Auto-dated filenames (e.g., `MAY_28_2026_CV.pdf`)
- Single-page optimized layout

### Usage:

```bash
cd tools/cv_generator
poetry run python main.py
```

## 🌐 Deployment

This site automatically deploys to GitHub Pages on every push to the `main` branch.

### Setup Instructions:

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Enable GitHub Pages:**
   - Go to your repository on GitHub
   - Navigate to **Settings** → **Pages**
   - Under "Build and deployment":
     - Source: **GitHub Actions**
   - Wait a few minutes for the first deployment

3. **Access Your Site:**
   - Your site will be available at: `https://[username].github.io/[repo-name]/`
   - The URL will appear in the Actions tab after deployment

## 🛠️ Development

### Local Development:

Simply open `index.html` in your browser or use a local server:

```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve

# Then visit http://localhost:8000
```

### Updating Content:

1. Edit `index.html` to update your bio, projects, and skills
2. Modify `style.css` to change styling
3. Commit and push - it will auto-deploy!

## 📝 Customization

### Update Your Information:

1. **Personal Info:** Edit the header section in `index.html`
2. **Bio:** Update the "Hi there 👋" section
3. **Projects:** Add/remove/edit project cards
4. **Skills:** Modify the skills grid
5. **Social Links:** Update footer links

### Styling:

Colors and themes are defined in CSS variables at the top of `style.css`:

```css
:root {
    --primary-color: #2c3e50;
    --accent-color: #3498db;
    --text-color: #333;
    --text-light: #666;
    --background: #ffffff;
    --background-alt: #f8f9fa;
    --border-color: #e1e4e8;
}
```

## 📄 License

Feel free to use this template for your own personal website!

## 🤝 Contact

- **Email:** hailemichael.atrsaw@gmail.com
- **LinkedIn:** [linkedin.com/in/hailat](https://linkedin.com/in/hailat/)
- **GitHub:** [github.com/hailatGH](https://github.com/hailatGH)
