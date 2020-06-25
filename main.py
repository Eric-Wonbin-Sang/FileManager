import os
import time

from General import Constants


def get_location_list(directories_txt):

    txt = open(directories_txt)
    location_list = []
    for line in txt:
        location = line.replace("\n", "")
        try:
            os.listdir(location)
            location_list.append(location)
            print("+ {} confirmed.".format(location))
        except FileNotFoundError:
            print("- {} does not exist.".format(location))
    txt.close()
    return location_list


def get_location_path_list_dict(location_list):
    location_path_list_dict = {}
    for location in location_list:
        location_path_list_dict[location] = os.listdir(location)
    return location_path_list_dict


def get_list_difference(list_a, list_b):
    if len(list_a) > len(list_b):
        return list(set(list_a) - set(list_b))
    else:
        return list(set(list_b) - set(list_a))


def get_change_status(location_key, curr_file_list, prev_file_list):

    print("{} changed".format(location_key))
    delta_list = get_list_difference(curr_file_list, prev_file_list)

    print("\t{}:".format("Added" if len(curr_file_list) > len(prev_file_list)
                         else "Removed"))
    for delta_file in delta_list:
        print("\t\t{}".format(delta_file))
    print("---------------------------")


def main():

    location_list = get_location_list(Constants.directories_txt)

    location_path_list_dict = get_location_path_list_dict(location_list)
    prev_location_path_list_dict = location_path_list_dict

    while True:

        location_path_list_dict = get_location_path_list_dict(location_list)

        for location_key in location_path_list_dict:

            curr_file_list = location_path_list_dict[location_key]
            prev_file_list = prev_location_path_list_dict[location_key]

            if curr_file_list != prev_file_list:
                get_change_status(location_key, curr_file_list, prev_file_list)

        prev_location_path_list_dict = location_path_list_dict
        time.sleep(.2)


main()
