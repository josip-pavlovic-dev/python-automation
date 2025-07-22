#!/bin/bash

echo "📤 Git Auto Push Script"
echo "------------------------"
read -p "🔤 Commit message: " msg

if [ -z "$msg" ]; then
  echo "❌ Commit message is required!"
  exit 1
fi

git add .
git commit -m "$msg"
git push

echo "✅ Push completed!"
read -n 1 -s -r -p "🔚 Press any key to exit..."
echo
echo "Goodbye! 👋"