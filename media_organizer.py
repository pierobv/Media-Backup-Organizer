import shutil
from pathlib import Path
from datetime import datetime
from PIL import Image

def extract_metadata(file_path):
    """
    Extracts the creation date object from EXIF data.
    Falls back to file modification time if EXIF is missing.
    """
    date_obj = None

    try:
        # Check if the file is an image to attempt EXIF date extraction
        if file_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            with Image.open(file_path) as img:
                exif = img.getexif()
                if exif:
                    # Extract the date from DateTimeOriginal (Tag 36867)
                    if 36867 in exif:
                        date_str = exif[36867]
                        date_obj = datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S")

    except Exception as e:
        print(f"Error reading EXIF from {file_path.name}: {e}")

    # Fallback: if no date in EXIF (or if it's a video), use file modification time
    if not date_obj:
        timestamp = file_path.stat().st_mtime
        date_obj = datetime.fromtimestamp(timestamp)

    return date_obj

def get_unique_filename(destination_folder, original_file_path, date_obj):
    """
    Generates a unique filename based on date and time to prevent overwriting.
    Format: YYYYMMDD_HHMMSS.ext (appends _01, _02 for collisions)
    """
    time_str = date_obj.strftime("%Y%m%d_%H%M%S")
    extension = original_file_path.suffix.lower()
    
    new_name = f"{time_str}{extension}"
    final_path = destination_folder / new_name
    
    counter = 1
    while final_path.exists():
        new_name = f"{time_str}_{counter:02d}{extension}"
        final_path = destination_folder / new_name
        counter += 1
        
    return final_path

def organize_backup(source_dir, dest_dir):
    """
    Main function to traverse the messy backup and organize files by Year and Month.
    """
    source_path = Path(source_dir)
    dest_path = Path(dest_dir)

    if not source_path.exists():
        print(f"Error: Source directory '{source_dir}' not found.")
        return

    # Define what extensions belong to which category
    IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.heic', '.webp'}
    VIDEO_EXTS = {'.mp4', '.mov', '.avi', '.mkv', '.gif'}

    print("Scanning root directory for media files...")
    
    # rglob('*') searches through ALL folders and subfolders inside the root
    for file_path in source_path.rglob('*'):
        if not file_path.is_file():
            continue

        ext = file_path.suffix.lower()
        
        # Categorize the file based on its extension
        if ext in IMAGE_EXTS:
            category = "Photos"
        elif ext in VIDEO_EXTS:
            category = "Videos"
        else:
            # Skip documents, text files, and other non-media files
            continue

        # Extract date metadata
        date_obj = extract_metadata(file_path)
        year = str(date_obj.year)
        month = f"{date_obj.month:02d}" # Formats month with leading zero (e.g., '03', '11')
        
        # Structure: Destination / Category / Year / Month
        final_folder = dest_path / category / year / month

        # Create destination folder and unique filename
        final_folder.mkdir(parents=True, exist_ok=True)
        final_file_path = get_unique_filename(final_folder, file_path, date_obj)

        # Copy the file to the new organized structure
        shutil.copy2(file_path, final_file_path)
        print(f"[{category}] Copied: {file_path.name} -> {final_folder.relative_to(dest_path)}")