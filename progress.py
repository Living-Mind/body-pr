from tabulate import tabulate
import datetime

#data = {"Part": ["Left arm", "Right arm"],
#        "Current": [35, 35],
#        "PR": [37, 37]}

data = {"Body part": ["Left forearm", "Right forearm", "Left arm", "Right arm", "Left calf", "Right calf", "Left leg", "Right leg", "Neck", "Waist"],
        "Current": [],
        "PR": []}
        #"PR": [32.5 ,32.5 ,38 ,38 ,36 ,36 ,55.5 ,55.5 ,40.5 , 78.5]}

def update_data():

    with open("file.txt", "r") as f:
        line = f.readlines()[-1:]
        pr_list = [float(num) for num in line[0].split(",")]
        f.close
    
    body_parts = ["Left forearm", "Right forearm", "Left arm", "Right arm", "Left calf", "Right calf", "Left leg", "Right leg", "Neck", "Waist"]
    #print(pr_list)
    for part in body_parts:
        data["Current"] += [float(input(f"{part}: "))]

    new_pr_list = []
    for (current_value, pr_value) in zip(data["Current"], pr_list):
        #print(current_value, pr_value)
        if current_value > pr_value:
            new_pr_list.append(current_value)
        else:
            new_pr_list.append(pr_value)
    pr_list = new_pr_list
    data["PR"] = pr_list

    with open("file.txt", "a") as f:
        formated_pr_list = str(pr_list).replace("[", "").replace("]", "")
        #print(formated_pr_list)
        f.write( "\r\n" + str(datetime.datetime.now().strftime("%b/%d/%Y")) + "\n" + tabulate(data, headers="keys", tablefmt="pretty") + "\n" + formated_pr_list)
        f.close

update_data()