import os
import shutil
import subprocess
from datetime import datetime
import sys

# Get the current year and day from arguments or defaults
current_year = datetime.now().year
current_day = int(sys.argv[1]) if len(sys.argv) > 1 else datetime.now().day

# Define the base directory path
base_dir = os.path.join(os.path.dirname(__file__), str(current_year))

# Define the new directory path for the current day
new_day_dir = os.path.join(base_dir, f'{current_day:02}')

# Define the template and target file paths
template_file = os.path.join(os.path.dirname(__file__), 'templates', 'solution_template.py')
target_file = os.path.join(new_day_dir, 'solution.py')

# Create the directory for the current day if it doesn't exist
os.makedirs(new_day_dir, exist_ok=True)

# Copy the template to the new solution.py file
shutil.copyfile(template_file, target_file)

# Define the puzzle file path
puzzle_file = os.path.join(new_day_dir, 'puzzle.md')

# Remove the existing puzzle.md file if it exists
if os.path.exists(puzzle_file):
    os.remove(puzzle_file)

# Define the command to download the day's puzzle and input
aoc_command = ['aoc', '-y', str(current_year), '-d', str(current_day), 'download']

# Run the aoc command
subprocess.run(aoc_command)

print(f'Directory and solution.py created for day {current_day:02} in {current_year}.')
