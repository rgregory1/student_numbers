import pathlib, datetime
from file_grabber import grab_files
from getmac import get_mac_address as gma

cwd = pathlib.Path.cwd()

# home mac address is a4:83:e7:72:41:a3
print(gma())
mac_address = str(gma())

today = str(datetime.datetime.now().strftime("%Y-%m-%d"))
print(today)

file_list = [
    "student_numbers_data.csv",
]


grab_files(
    file_list,
    cwd,
)

# move files
for file in file_list:
    my_file = cwd / "data_files" / file
    if mac_address == "a4:83:e7:72:41:a3":
        to_file = "/Users/rgregory/Documents/trial/" + file
        my_file.rename(to_file)
    else:
        to_file = "/Users/admin/Documents/student_numbers/" + file
        my_file.rename(to_file)
