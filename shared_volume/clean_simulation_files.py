import os
import glob
import time

if __name__ == '__main__':
    files_to_delete = [
        "/shared_volume/netlogo_output/m1_output.txt",
        "/shared_volume/netlogo_output/m1_alive.txt",
        "/shared_volume/netlogo_output/m2_output.txt",
        "/shared_volume/netlogo_output/m2_alive.txt"
    ]

    file_path = "/shared_volume/jacamo/jacamo_model/src/agt/list/"
    
    for clean_up in glob.glob(file_path+'*.*'):
        if not clean_up.endswith('.gitkeep'):
            files_to_delete.append(clean_up)

    for filename in files_to_delete:
        if os.path.exists(filename):
            print("Deleting file: "+filename)
            os.remove(filename)
        else:
            print(filename + " does not exists")

    # filename = "/shared_volume/netlogo_output/m1_output.txt"
    # if os.path.exists(filename):
    #     print("Deleting file: "+filename)
    #     os.remove(filename)
    # else:
    #     print(filename + " does not exists")

    # filename = "/shared_volume/netlogo_output/m1_alive.txt"
    # if os.path.exists(filename):
    #     print("Deleting file: "+filename)
    #     os.remove(filename)
    # else:
    #     print(filename + " does not exists")

    # filename = "/shared_volume/netlogo_output/m2_output.txt"
    # if os.path.exists(filename):
    #     print("Deleting file: "+filename)
    #     os.remove(filename)
    # else:
    #     print(filename + " does not exists")

    # filename = "/shared_volume/netlogo_output/m2_alive.txt"
    # if os.path.exists(filename):
    #     print("Deleting file: "+filename)
    #     os.remove(filename)
    # else:
    #     print(filename + " does not exists")


    # filename = "/shared_volume/netlogo_output/errors.txt"
    # if os.path.exists(filename):
    #     print("Deleting file: "+filename)
    #     os.remove(filename)
    # else:
    #     print(filename + " does not exists")


    # file_path = "/shared_volume/jacamo/jacamo_model/src/agt/list/"
    # for clean_up in glob.glob(file_path+'*.*'):
    #     #print(clean_up)
    #     if not clean_up.endswith('.gitkeep'):
    #         print("Deleting file: "+clean_up) 
    #         os.remove(clean_up)
