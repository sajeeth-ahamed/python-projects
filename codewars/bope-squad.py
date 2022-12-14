from math import ceil
from typing import Tuple

weapons = {
    "PT92": 17,
    "M4A1": 30,
    "M16A2": 30,
    "PSG1": 5
}


def magazine_no(info: Tuple[str, int]) -> int:
    (weapon, streets) = info
    bullt_fire = streets * 3
    mag_cap = weapons[weapon]
    need_mag = bullt_fire / mag_cap

    return ceil(need_mag)


var1 = magazine_no(["PSG1", 6])
print(var1)

var2 = magazine_no(["M4A1", 11])
print(var2)

var3 = magazine_no(["PT92", 7])
print(var3)


# Second solution:

weapons_info = {"PT92": 17,
                "M4A1": 30,
                "M16A2": 30,
                "PSG1": 5}


def count_mag_no(n):
    return ceil(3 * n[1] / weapons_info[n[0]])


var4 = magazine_no(["PSG1", 9])
print("Second solution test:", var4)

var5 = magazine_no(["M4A1", 17])
print("Second solution test:", var5)

var6 = magazine_no(["PT92", 9])
print("Second solution test:", var6)
