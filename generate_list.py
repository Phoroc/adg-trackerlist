import math
import re
import requests
import json
import os

trackerslist = [
    ["trackers_best", "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt"],
    ["trackers_all", "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt"]
]

output_dir = "./release"


def convert_trackers(list_info: list) -> str:
    r = requests.get(list_info[1])
    domain_list = []
    if r.status_code == 200:
        lines = r.text.splitlines()
        for line in lines:
            if not line.startswith("#") and line.strip():
                domain_list.append("|" + re.sub(r"^.*://(.*):\d.*", r"\1",line) + "^")
    result = "\n".join(list(dict.fromkeys(domain_list)))
    filepath = os.path.join(output_dir, list_info[0] + ".txt")
    with open(filepath, "w") as f:
        f.write(result)
    return filepath


def main():
    files = []
    os.mkdir(output_dir)
    for ls in trackerslist:
        filepath = convert_trackers(ls)
        files.append(filepath)
    print("list generated:")
    for filepath in files:
        print(filepath)


if __name__ == "__main__":
    main()
