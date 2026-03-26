-- Media Backup Organizer --

A fast and reliable Python script that acts like a vacuum: it dives into a messy, nested mobile backup folder, extracts all media files, and automatically organizes them into a clean, chronological folder structure of `Photos` and `Videos` categorized by Year and Month.


- **Chaos to Order:** Ignores messy original folder structures. It recursively searches your entire backup and neatly categorizes everything into `Photos` or `Videos`.
- **Chronological Sorting:** Automatically sorts files into `YYYY / MM` folders for perfect chronological viewing.
- **EXIF Date Extraction:** Reads metadata from images to find the exact original creation date, avoiding errors caused by OS modification dates.
- **Smart Renaming:** Renames files to a standard `YYYYMMDD_HHMMSS.ext` format to prevent naming collisions (e.g., multiple files named `IMG_0001.jpg` from different folders).
- **Non-Destructive:** Uses `shutil.copy2` to duplicate files safely without altering the original backup or losing system metadata.

-- How to Use

- 1. Prerequisites
Make sure you have Python 3 installed on your machine. 

- 2. Installation
Clone this repository and install the required external dependency (Pillow, used for reading EXIF data):

```bash
pip install -r requirements.txt


# ===============================================================
# CONFIGURATION
# ===============================================================

SOURCE_BACKUP_FOLDER = r"C:\path\to\your\messy_backup" 
DESTINATION_FOLDER = r"C:\path\to\organized_backup"


python main_monitor.py



-- OUTPUT RESULT: 

organized_backup/
├── Photos/
│   ├── 2023/
│   │   ├── 08/
│   │   │   ├── 20230815_143000.jpg
│   │   │   └── 20230816_091530.png
│   │   └── 12/
│   │       └── 20231225_204510.jpg
│   └── 2026/
│       └── 03/
│           └── 20260326_100500.jpg
│
└── Videos/
    ├── 2024/
    │   └── 05/
    │       └── 20240520_112000.mp4
    └── 2026/
        └── 02/
            └── 20260212_180000.mov
