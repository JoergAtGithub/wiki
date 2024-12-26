import os
import re
import subprocess

def rename_files_with_git(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if ' ' in file:
                old_file_path = os.path.join(root, file)
                new_file = file.replace(' ', '-')
                new_file_path = os.path.join(root, new_file)
                subprocess.run(['git', 'mv', old_file_path, new_file_path])

def update_links(file_path, lookup_list, repo_root):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    updated_content = []
    for line_num, line in enumerate(content, start=1):
        original_line = line

        # Define regex patterns and their replacements
        regex_patterns = [
            # Update links of type (file%20name#anchor) or (file name#anchor) to (file-name.md#anchor)
            (r'\(([^)]+)(?:%20| )([^)]+)#([^)]+)\)', lambda m: f'({m.group(1).replace("%20", "-").replace(" ", "-")}-{m.group(2).replace("%20", "-").replace(" ", "-")}.md#{m.group(3)})'),
            # Update links of type [text](file%20name) or [text](file name) to [text](file-name.md)
            (r'\[([^\]]+)\]\(([^)]+)(?:%20| )([^)]+)\)', lambda m: f'[{m.group(1)}]({m.group(2).replace("%20", "-").replace(" ", "-")}-{m.group(3).replace("%20", "-").replace(" ", "-")}.md)')
        ]

        # Apply regex patterns in order and break if a match is found
        for pattern, repl in regex_patterns:
            new_line = re.sub(pattern, repl, line)
            if new_line != line:
                line = new_line
                break

        updated_content.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_content)

    # Check for dead links to .md files in the local repo after conversion
    for line_num, line in enumerate(updated_content, start=1):
        dead_links = re.findall(r'\[([^\]]+)\]\(([^)]+\.md)(#[^)]+)?\)', line)
        for link_text, link_path, link_anchor in dead_links:
            # Exclude local anchors within the same file
            if not link_path.startswith('#'):
                full_link_path = os.path.join(repo_root, link_path)
                if not os.path.exists(full_link_path):
                    lookup_list.append(f"Dead link in file {file_path}, line {line_num}: {line.strip()}")

def update_all_links(directory):
    # Rename files first using git
    rename_files_with_git(directory)

    lookup_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                update_links(file_path, lookup_list, directory)
    
    # Print the lookup list with dead links
    if lookup_list:
        print("Dead links found:")
        for entry in lookup_list:
            print(entry)
    else:
        print("No dead links found.")

# Replace 'path_to_your_wiki_directory' with the path to your cloned wiki directory
update_all_links(r'D:\mixxx.wiki')

