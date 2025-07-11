#!/bin/bash

echo "🔍 Verifying AdventureTimeClone game files..."

REQUIRED_FILES=(
  "main.py"
  "core/engine.py"
  "scenes/title_screen.py"
  "scenes/treehouse.py"
  "maps/treehouse.tmx"
  "maps/candy_kingdom.tmx"
  "maps/ice_kingdom.tmx"
  "maps/lich_dungeon.tmx"
  "maps/grasslands.tmx"
  "assets/tilesets/basic_tiles.png"
  "assets/sprites/finn.png"
  "data/warps.json"
  "data/dialog.json"
  "data/quest_log.json"
  "save/save1.json"
)

ALL_PRESENT=true

for file in "${REQUIRED_FILES[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "❌ Missing: $file"
    ALL_PRESENT=false
  else
    echo "✅ Found:  $file"
  fi
done

if [ "$ALL_PRESENT" = true ]; then
  echo "✅ All required files are present!"
else
  echo "⚠️  One or more files are missing. Please re-extract the ZIP or copy them into place."
fi