from media_organizer import organize_backup

# ==============================================================================
# CONFIGURATION
# Point SOURCE_BACKUP_FOLDER to the root of your messy backup. 
# The script will find all photos and videos inside any subfolder automatically.
# ==============================================================================

SOURCE_BACKUP_FOLDER = r"C:\path\to\your\messy_backup" 
DESTINATION_FOLDER = r"C:\path\to\organized_backup"

# ==============================================================================

if __name__ == "__main__":
    print("Starting the media backup organization process...")
    
    # Calls the main logic function from media_organizer.py
    organize_backup(SOURCE_BACKUP_FOLDER, DESTINATION_FOLDER)
    
    print("\nOrganization complete! Check your destination folder.")