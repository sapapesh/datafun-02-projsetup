''' This module provides functions for creating a series of project folders. '''

import math
import statistics
import pathlib
import time
import sarahhoward_utils


#Create folders for a given price range range
def create_folders_for_range(start, end, interval):
    start = 100
    end = 500
    interval = 50
    for i in range(start, end, interval):
        pathlib.Path(f"{i}").mkdir(exist_ok=True)

#Create folders for a given list
def create_folders_from_list(folder_list):
    for folder in folder_list:
        pathlib.Path(folder).mkdir(exist_ok=True)

#Create prefixed folders from a list of names and combining with a prefix$
def create_prefixed_folders(folder_list, prefix):
    for folder in folder_list:
        pathlib.Path(f"{prefix}-{folder}").mkdir(exist_ok=True)

#Create files periodically
def create_folders_periodically(duration, period):
    start_time = time.time()
    while(time.time()-start_time < duration): #continue running while the time elapsed from start is less than the given duration
        current_time = time.time()-start_time
        pathlib.Path(f"Folder created at {round(current_time)} seconds").mkdir(exist_ok=True)
        time.sleep(period) #wait specified amount of seconds before beginning next iteration

#Create a path object
project_path = pathlib.Path.cwd()

#Define the new subfolder path
data_path = project_path.joinpath('data')

#Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

def create_project_directory(dir_name: str):
    #creates a project sub-directory
    pathlib.Path(dir_name).mkdir(exist_ok=True)

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Pring byline from imported module
    print(f"byline:{sarahhoward_utils.byline}")

    # Call function 1 to create folders for a range (e.g.price)
    create_folders_for_range(start=100, end=500, interval=50) 

    # Call function 2 to create folders given a list
    folder_names = ['Northeast', 'South', "Midwest", 'Southwest', 'Mountain', 'West']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders with a prefix
    create_prefixed_folders(folder_list=['cost', 'work', 'time'], prefix=["data-"])

    # Call function 4 to create folders every 5 seconds
    create_folders_periodically(duration=15,period=5)

if __name__ == "__main__":
    main()

