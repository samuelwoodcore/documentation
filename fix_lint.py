#!/usr/bin/env python3

import os
import re

def fix_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove trailing whitespace
    content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)
    
    # Ensure consistent line endings (Unix style)
    content = content.replace('\r\n', '\n')
    
    # Remove multiple consecutive blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Fix inconsistent indentation (convert tabs to spaces)
    content = content.expandtabs(2)
    
    # Remove leading whitespace from empty lines
    content = re.sub(r'^\s+$', '', content, flags=re.MULTILINE)
    
    # Ensure file ends with a single newline
    content = content.rstrip() + '\n'
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # Get all MDX files
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.mdx'):
                file_path = os.path.join(root, file)
                print(f'Fixing {file_path}')
                fix_file(file_path)

if __name__ == '__main__':
    main() 