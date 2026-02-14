#!/usr/bin/env python3
"""
Script to package the Next.js SEO Optimizer skill
"""

import os
import zipfile
import sys
from pathlib import Path

def validate_skill(skill_dir):
    """Validate the skill structure and content"""
    skill_path = Path(skill_dir)

    # Check if SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f"Error: {skill_md} not found")
        return False

    # Read and validate frontmatter
    content = skill_md.read_text(encoding='utf-8')

    if not content.strip().startswith("---"):
        print("Error: SKILL.md must start with YAML frontmatter (---)")
        return False

    # Find the end of frontmatter
    parts = content.split("---", 2)
    if len(parts) < 3:
        print("Error: Invalid YAML frontmatter in SKILL.md")
        return False

    frontmatter = parts[1]

    # Check for required fields
    if 'name:' not in frontmatter:
        print("Error: 'name' field missing in YAML frontmatter")
        return False

    if 'description:' not in frontmatter:
        print("Error: 'description' field missing in YAML frontmatter")
        return False

    print("[SUCCESS] Skill validation passed")
    return True

def package_skill(skill_dir, output_dir=None):
    """Package the skill into a .skill file"""
    skill_path = Path(skill_dir)
    skill_name = skill_path.name

    if output_dir is None:
        output_dir = skill_path.parent
    else:
        output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    # Create the .skill file (which is just a zip file)
    skill_file = output_dir / f"{skill_name}.skill"

    with zipfile.ZipFile(skill_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(skill_path):
            for file in files:
                file_path = Path(root) / file
                arc_path = file_path.relative_to(skill_path.parent)
                zf.write(file_path, arc_path)

    print(f"[SUCCESS] Skill packaged successfully: {skill_file}")
    return skill_file

def main():
    skill_dir = sys.argv[1] if len(sys.argv) > 1 else "."

    print(f"Validating skill in: {skill_dir}")

    if not validate_skill(skill_dir):
        sys.exit(1)

    print(f"Packaging skill from: {skill_dir}")
    package_skill(skill_dir)

    print("\nNext.js SEO Optimizer skill is ready!")
    print("You can now distribute the .skill file or install it in Claude Code.")

if __name__ == "__main__":
    main()