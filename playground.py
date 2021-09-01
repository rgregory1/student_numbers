import csv
import pandas as pd

filename = "data_files/race_data.csv"

# create variable for totals
mvu_w = 0
mvu_i = 0
mvu_a = 0
mvu_b = 0
mvu_h = 0
mvu_p = 0

fcs_w = 0
fcs_i = 0
fcs_a = 0
fcs_b = 0
fcs_h = 0
fcs_p = 0

hes_w = 0
hes_i = 0
hes_a = 0
hes_b = 0
hes_h = 0
hes_p = 0

swa_w = 0
swa_i = 0
swa_a = 0
swa_b = 0
swa_h = 0
swa_p = 0

with open(filename, "r") as data:
    for line in csv.reader(data):
        # print(line)
        if line[0] == "PS187":
            if line[1] == "W":
                mvu_w += 1
            elif line[1] == "I":
                mvu_i += 1
            elif line[1] == "A":
                mvu_a += 1
            elif line[1] == "B":
                mvu_b += 1
            elif line[1] == "H":
                mvu_h += 1
            elif line[1] == "P":
                mvu_p += 1
        if line[0] == "PS115":
            if line[1] == "W":
                fcs_w += 1
            elif line[1] == "I":
                fcs_i += 1
            elif line[1] == "A":
                fcs_a += 1
            elif line[1] == "B":
                fcs_b += 1
            elif line[1] == "H":
                fcs_h += 1
            elif line[1] == "P":
                fcs_p += 1
        if line[0] == "PS142":
            if line[1] == "W":
                hes_w += 1
            elif line[1] == "I":
                hes_i += 1
            elif line[1] == "A":
                hes_a += 1
            elif line[1] == "B":
                hes_b += 1
            elif line[1] == "H":
                hes_h += 1
            elif line[1] == "P":
                hes_p += 1
        if line[0] == "PS295":
            if line[1] == "W":
                swa_w += 1
            elif line[1] == "I":
                swa_i += 1
            elif line[1] == "A":
                swa_a += 1
            elif line[1] == "B":
                swa_b += 1
            elif line[1] == "H":
                swa_h += 1
            elif line[1] == "P":
                swa_p += 1


# print(mvu_w)
# print(mvu_i)
# print(mvu_a)
# print(mvu_b)
# print(mvu_h)
# print(mvu_p)

fcs_total = fcs_h + fcs_i + fcs_a + fcs_b + fcs_p + fcs_w
hes_total = hes_h + hes_i + hes_a + hes_b + hes_p + hes_w
swa_total = swa_h + swa_i + swa_a + swa_b + swa_p + swa_w
mvu_total = mvu_h + mvu_i + mvu_a + mvu_b + mvu_p + mvu_w

df = pd.DataFrame(
    [
        (
            fcs_h,
            fcs_i,
            fcs_a,
            fcs_b,
            fcs_p,
            fcs_w,
            fcs_total,
        ),
        (
            hes_h,
            hes_i,
            hes_a,
            hes_b,
            hes_p,
            hes_w,
            hes_total,
        ),
        (
            swa_h,
            swa_i,
            swa_a,
            swa_b,
            swa_p,
            swa_w,
            swa_total,
        ),
        (
            mvu_h,
            mvu_i,
            mvu_a,
            mvu_b,
            mvu_p,
            mvu_w,
            mvu_total,
        ),
        (
            mvu_h + fcs_h + hes_h + swa_h,
            mvu_i + fcs_i + hes_i + swa_i,
            mvu_a + fcs_a + hes_a + swa_a,
            mvu_b + fcs_b + hes_b + swa_b,
            mvu_p + fcs_p + hes_p + swa_p,
            mvu_w + fcs_w + hes_w + swa_w,
            mvu_total + fcs_total + hes_total + swa_total,
        ),
    ],
    index=["FCS", "HES", "SWA", "MVU", "Total"],
    columns=(
        "Hispanic",
        "American Indian",
        "Asian",
        "Black",
        "Islander",
        "White",
        "Total",
    ),
)

print(df)
