# GitHub Setup Instructions

## Current Status
Git has been initialized in this repository. However, there's a lock file preventing automatic staging. Follow these steps to complete the GitHub push:

## Step 1: Resolve Git Lock (if needed)
If you see a lock file error, close any IDEs or git clients, then:

**Option A: Close and reopen your IDE**
- Close Cursor/VS Code completely
- Reopen the project
- Try the git commands again

**Option B: Manually remove the lock file**
1. Close all programs using git (IDEs, git clients, etc.)
2. Navigate to: `D:\mitacs_blender\.git\`
3. Delete the file: `index.lock`
4. Try the git commands again

## Step 2: Stage and Commit Files

Open a terminal in the project directory and run:

```bash
# Stage all files (respecting .gitignore)
git add .

# Create initial commit
git commit -m "Initial commit: MITACS Blender Robotics Project

- Added Blender scripts for robot visualization
- Added YOLOv5 object detection notebook
- Added camera calibration tools
- Added comprehensive README and documentation
- Added .gitignore for proper file exclusions"
```

## Step 3: Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon in the top right → "New repository"
3. Name your repository (e.g., `mitacs-blender-robotics`)
4. **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click "Create repository"

## Step 4: Connect and Push

After creating the repository, GitHub will show you commands. Use these:

```bash
# Add the remote (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

If your default branch is `master` instead of `main`:
```bash
git push -u origin master
```

## Alternative: Using GitHub CLI

If you have GitHub CLI installed:

```bash
# Create repo and push in one command
gh repo create mitacs-blender-robotics --public --source=. --remote=origin --push
```

## Troubleshooting

### Authentication Issues
If you're asked for credentials:
- Use a Personal Access Token (not password)
- Generate one at: GitHub → Settings → Developer settings → Personal access tokens
- Or use GitHub Desktop or SSH keys

### Large Files Warning
If you see warnings about large files:
- The `.gitignore` should prevent most large files
- If needed, use Git LFS: `git lfs install` and track large file types

### Push Rejected
If push is rejected:
```bash
# Pull first (if repo was initialized on GitHub)
git pull origin main --allow-unrelated-histories

# Then push again
git push -u origin main
```

## Files Ready to Push

The following key files are ready:
- ✅ README.md (comprehensive documentation)
- ✅ .gitignore (excludes unnecessary files)
- ✅ requirements.txt (Python dependencies)
- ✅ All source code files
- ✅ Documentation folder
- ✅ Project image (side_and _tendons.png)

Large files and outputs are excluded via .gitignore.

