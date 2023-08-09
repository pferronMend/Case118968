output_dir = os.getenv("HOME") + "/TMP/reports_out/mintec"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
os.chdir(output_dir)
filename = "mintec.csv"
with open(filename, "w") as outfile:
    c = csv.writer(outfile)
    for orig, dest in CORRIDORS:
