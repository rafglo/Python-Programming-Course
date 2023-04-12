import zipfile, os, datetime, time
from pathlib import Path

def cody_mod(folders, mod_days, out_path, extension):
    date = str(datetime.date.today())
    zip_name = "copy - " + date + ".zip"
    if_exists = os.path.exists(out_path + "\\Backup")
    if if_exists:
        zip_path = out_path + "\\Backup\\" + zip_name
    else:
        backup_path = out_path + "\\Backup\\"
        os.mkdir(backup_path)
        zip_path = backup_path + "\\" + zip_name

    with zipfile.ZipFile(zip_path, "w") as zf:
        for folder in folders:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    mod = os.path.getmtime(os.path.join(root, file))
                    delta = (time.time() - mod) / (3600 * 24)
                    if Path(file).suffix == extension and delta < int(mod_days):
                        zf.write(os.path.join(root, file), os.path.basename(os.path.join(root, file)))
    zf.close()


cody_mod([r"C:\Users\Rafal\OneDrive\Pulpit\goegrafia", r"C:\Users\Rafal\OneDrive\Pulpit\informatyka"], 3, r"C:\Users\Rafal\OneDrive\Pulpit", ".txt")
