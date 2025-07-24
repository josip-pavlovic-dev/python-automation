import os
from ssl import VerifyMode
from tarfile import data_filter

from day04_datetime import timestamp_generator

def create_file(file_path):
    """Create a file at the specified path with some sample content."""
    # Ensure the directory exists
    with open(file_path, 'w') as file:
        file.write("Ovo je prva linija.\n")
        file.write("Ovo je druga linija.\n")
        file.write("Ovo je treća linija.\n")    


        
