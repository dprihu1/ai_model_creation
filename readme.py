import os
import re


def create_files_from_tree(tree_structure_text, base_output_dir):
    """
    Parses a text representation of a directory tree, creates directories, and creates empty files.

    Args:
        tree_structure_text (str): A string containing the directory tree structure
                                   using "├──" and "└──" delimiters.
        base_output_dir (str): The base directory where the parsed tree structure
                               should be recreated.
    """
def get_directory_listings(text_tree: list):
    """
    Follow tree to last layer
    """
    delimit = '├──'
    for level, item in  enumerate(text_tree):
        if delimit in item[:3] and level != 1:
            break
        else:
            print(level,item) 

def extract_clean_path(line: str) -> str:
    # Remove comment (anything after #)
    line = re.sub(r'#.*', '', line)
    
    # Extract the last "word" that looks like a path (ending in / or a filename)
    match = re.search(r'([^\s\\/]+/?)$', line.strip())
    
    return match.group(1) if match else ''

def create_empty_file(filename):
    """Creates an empty file at the specified filename."""
    with open(filename, "w") as f:
        pass  # Create an empty file


# Example Usage (unchanged)
with open("test_tree.md", "r") as f:
    text_tree = f.readlines()

output_directory = "created_project_structure"
create_files_from_tree(text_tree, output_directory)
