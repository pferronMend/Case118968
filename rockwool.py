ws = wb.active

directory = os.getenv("HOME") + "/TMP/reports_out/Rockwool"
if not os.path.exists(directory):
    os.makedirs(directory)
os.chdir(directory)

EQUIPMENTS = {"20DV": EQUIPMENT_20DC, "40HC": EQUIPMENT_40HC}

thc = THC_NONE
