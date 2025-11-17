# Push Instructions for TextbookBiasDetection Repository

## Current Status

✅ **Local repository initialized and committed**
- Location: `/home/user/TextbookBiasDetection/`
- Branch: `master`
- Commit: `10c5b30` - Initial commit with complete project

---

## Option 1: Push to GitHub (Recommended)

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `TextbookBiasDetection`
3. Description: `Detecting Publisher Bias in Academic Textbooks Using Bayesian Ensemble Methods and LLMs`
4. Visibility: Choose Public or Private
5. **Do NOT initialize with README** (we already have one)
6. Click "Create repository"

### Step 2: Add Remote and Push

```bash
cd /home/user/TextbookBiasDetection

# Add GitHub as remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/TextbookBiasDetection.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Verify

Visit your repository at:
```
https://github.com/YOUR_USERNAME/TextbookBiasDetection
```

---

## Option 2: Push to Existing Repository

If you already have a repository URL:

```bash
cd /home/user/TextbookBiasDetection

# Add remote
git remote add origin <YOUR_REPOSITORY_URL>

# Push
git push -u origin master
```

---

## Option 3: Push to GitLab

### Create GitLab Repository

1. Go to https://gitlab.com/projects/new
2. Create blank project: `TextbookBiasDetection`
3. Set visibility level
4. Click "Create project"

### Push to GitLab

```bash
cd /home/user/TextbookBiasDetection

# Add GitLab remote
git remote add origin https://gitlab.com/YOUR_USERNAME/TextbookBiasDetection.git

# Push
git push -u origin master
```

---

## Option 4: Push to Bitbucket

### Create Bitbucket Repository

1. Go to https://bitbucket.org/repo/create
2. Repository name: `TextbookBiasDetection`
3. Access level: Choose public or private
4. Click "Create repository"

### Push to Bitbucket

```bash
cd /home/user/TextbookBiasDetection

# Add Bitbucket remote
git remote add origin https://bitbucket.org/YOUR_USERNAME/textbookbiasdetection.git

# Push
git push -u origin master
```

---

## Troubleshooting

### Authentication Required

If you get authentication errors:

#### HTTPS (recommended)
```bash
# GitHub will prompt for credentials
# Or use a Personal Access Token as password
```

#### SSH (alternative)
```bash
# First, set up SSH key with GitHub/GitLab/Bitbucket
# Then use SSH URL instead of HTTPS
git remote set-url origin git@github.com:YOUR_USERNAME/TextbookBiasDetection.git
```

### Already Exists Error

If repository already exists remotely:

```bash
# Option 1: Force push (⚠️  overwrites remote)
git push -f origin master

# Option 2: Pull first, then push
git pull origin master --allow-unrelated-histories
git push origin master
```

### Branch Name Issues

If you need to rename branch:

```bash
# Rename master to main
git branch -M main
git push -u origin main
```

---

## Verify Push Success

After pushing, verify:

1. ✅ All files appear in remote repository
2. ✅ README.md displays correctly
3. ✅ Notebook opens in GitHub (may take a moment)
4. ✅ Commit message shows properly

---

## Quick Commands Reference

```bash
# Check current remotes
git remote -v

# Add remote
git remote add origin <URL>

# Remove remote
git remote remove origin

# Check status
git status

# View commit history
git log --oneline

# Push to remote
git push -u origin master
```

---

## Repository URL Format Examples

### GitHub
```
HTTPS: https://github.com/username/TextbookBiasDetection.git
SSH:   git@github.com:username/TextbookBiasDetection.git
```

### GitLab
```
HTTPS: https://gitlab.com/username/TextbookBiasDetection.git
SSH:   git@gitlab.com:username/TextbookBiasDetection.git
```

### Bitbucket
```
HTTPS: https://bitbucket.org/username/textbookbiasdetection.git
SSH:   git@bitbucket.org:username/textbookbiasdetection.git
```

---

## After Pushing

### Update README with Repository URL

Add a link to the repository in README.md:

```markdown
## 🔗 Repository

GitHub: https://github.com/YOUR_USERNAME/TextbookBiasDetection
```

### Enable GitHub Features

Consider enabling:
- **Issues**: For bug reports and feature requests
- **Wiki**: For extended documentation
- **Discussions**: For Q&A and community
- **Actions**: For automated testing (CI/CD)

### Add Repository Badges

Add status badges to README:

```markdown
![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/TextbookBiasDetection)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
```

---

## Making Repository Public

If you want to share publicly:

1. Go to repository Settings
2. Scroll to "Danger Zone"
3. Click "Change visibility"
4. Select "Public"
5. Confirm

---

## Need Help?

If you encounter issues:

1. Check GitHub/GitLab/Bitbucket documentation
2. Verify your git configuration: `git config --list`
3. Ensure you have network access
4. Check authentication credentials
5. Verify repository URL format

---

**Note:** Replace `YOUR_USERNAME` with your actual username on the platform you choose.
