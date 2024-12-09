# written using Windsurf and Claude 3.5 Sonnet
import os
import shutil
import subprocess
from datetime import datetime
import sys
from pathlib import Path

def main():
    # Get the current year and day from arguments or defaults
    current_year = datetime.now().year
    current_day = int(sys.argv[1]) if len(sys.argv) > 1 else datetime.now().day

    # Define the base directory path
    base_dir = os.path.join(os.path.dirname(__file__), str(current_year))

    # Define the new directory path for the current day
    new_day_dir = os.path.join(base_dir, f'{current_day:02}')

    # Create the directory for the current day if it doesn't exist
    os.makedirs(new_day_dir, exist_ok=True)

    # Copy template if it exists
    template_file = os.path.join(os.path.dirname(__file__), 'templates', 'solution_template.py')
    target_file = os.path.join(new_day_dir, 'solution.py')
    
    if os.path.exists(template_file):
        shutil.copyfile(template_file, target_file)
        print(f"Created solution.py from template")
    else:
        # Create empty solution.py if template doesn't exist
        Path(target_file).touch()
        print(f"Created empty solution.py")

    # Download puzzle and input using aoc CLI
    try:
        subprocess.run(['aoc', '-y', str(current_year), '-d', str(current_day), 'download'], check=True)
        print(f"Downloaded puzzle and input files for day {current_day}")
        
        # Move puzzle.md and input.txt to the day directory
        root_dir = os.path.dirname(__file__)
        puzzle_file = os.path.join(root_dir, 'puzzle.md')
        input_file = os.path.join(root_dir, 'input')
        
        if os.path.exists(puzzle_file):
            shutil.move(puzzle_file, os.path.join(new_day_dir, 'puzzle.md'))
            print(f"Moved puzzle.md to day {current_day} directory")
            
        if os.path.exists(input_file):
            shutil.move(input_file, os.path.join(new_day_dir, 'input.txt'))
            print(f"Moved input to day {current_day} directory")
            
    except subprocess.CalledProcessError as e:
        print(f"Error downloading files: {e}")
        return
    except shutil.Error as e:
        print(f"Error moving files: {e}")
        return

    print(f'Setup completed for day {current_day:02} in {current_year}.')

if __name__ == '__main__':
    main()
