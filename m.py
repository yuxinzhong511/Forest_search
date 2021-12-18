from fetch_data import *
from reconstruct import *
import plotly.graph_objects as go


if __name__ == '__main__':
    #store_data()
    # cache_file = open(os.path.join(PATH, FORESTS_DATA) , 'r')
    # cache_file_contents = cache_file.read()
    # forests_dict = json.loads(cache_file_contents)
    # cache_file.close()
    forests_dict = recon()

    states = []
    forests_with_size = {}
    for k,v in forests_dict.items():
        #print(v["size"])
        if(v["size"] is None):
            pass
        else:
            forests_with_size[k] = v["size"]

        for s in v["state"]:
            if(s in states):
                pass
            else:
                states.append(s)

    size_nums = list(forests_with_size.values())
    #print(size_nums)
    #print(states)
    def interact():
        while(True):
            s = input("Which state's forests are you looking for?(or type \"states\" to see all the states that has national forest(s) in it)>")
            if(s == "break"):
                break
            while(s not in states):
                if(s == "states"):
                    print(states)
                else:
                    print("The name of the state is wrong or the state you searched does not have national forest in it according to our dataset.")
                s = input("Please try another state or type \"states\" to see all the states that has national forest(s) in it:")
                if(s == "break"):
                    return
                # if(s == 'states'):
                #     print(states)

            f = input("Do you want to go fishing in the forest?(yes/no)>")
            if(f == "break"):
                return
            while(f != 'yes' and f !='no'):
                f = input("Please answer yes or no >")

            c = input("Do you want to go camping in the forest?(yes/no)>")
            if(c == "break"):
                return
            while(c != 'yes' and c != 'no'):
                c = input("Please answer yes or no >")

            print("Searching...")
            s_forests = []
            fs_forests = []
            cs_forests = []
            fcs_forests = []
            for k,v in forests_dict.items():
                match = False
                try:
                    if(v['state'][0] == s):
                        match = True
                except:
                    pass
                try:
                    if(v['state'][1] == s):
                        match = True 
                except:
                    pass
                if(match == True):
                    s_forests.append(k)

                    if(f == 'yes'):
                        if(v["fishing"] > 0 ):
                            fs_forests.append(k)
                        else:
                            pass
                    else:
                        pass

                    if(c == 'yes'):
                        if(v["camping"] > 0 ):
                            cs_forests.append(k)
                        else:
                            pass
                    else:
                        pass

                    if(f == 'yes' and c == 'yes'):
                        if(v["fishing"] > 0 and v["camping"] > 0):
                            fcs_forests.append(k)
                        else:
                            pass
                    else:
                        pass


                else:
                    pass
            if(f == 'no' and c == 'no'):
                print("The forest(s) in " , s,"is(are):")
                l = len(s_forests)
                print(s_forests)

            if(f == 'yes' and c == 'no'):
                print("The forest(s) in " , s,"that allow(s) fishing is(are):")
                l = len(fs_forests)
                print(fs_forests)
            
            if(c == 'yes' and f == 'no'):
                print("The forest(s) in " , s,"that allow(s) camping is(are):", s)
                l = len(cs_forests)
                print(cs_forests)

            if(c == 'yes' and f == 'yes'):
                print("The forest(s) in" , s,"that allow(s) fishing and camping is(are):", s)
                l = len(fcs_forests)
                print(fcs_forests)

            op = input("Which format would you like to present the search outcomes?(1) command line (2) Plotly>")
            if(op == "break"):
                return
            while(op != "1" and op != "2"):
                op = input("Please choose between 1 and 2 >")
                if(s == "break"):
                    return

            if(op == "1"):
            #command line
                for i in range(l):
                    if(f == 'no' and c == 'no'):
                        print(s_forests[i],":")
                        print(" ","size:",forests_dict[s_forests[i]]["size"]," acre")
                        print(" ","fishing:",forests_dict[s_forests[i]]["fishing"] > 0)
                        print(" ","camping:",forests_dict[s_forests[i]]["camping"] > 0)
                        if(len(forests_dict[s_forests[i]]["state"]) == 1):
                            print(" ","state:",forests_dict[s_forests[i]]["state"][0])
                        elif(len(forests_dict[s_forests[i]]["state"]) == 2):
                            print(" ","state:",forests_dict[s_forests[i]]["state"][0], " ", forests_dict[s_forests[i]]["state"][1])
                        else:
                            print(" ","state:",forests_dict[s_forests[i]]["state"][0], " ", forests_dict[s_forests[i]]["state"][1]," ", forests_dict[s_forests[i]]["state"][2])

                    if(f == 'yes' and c == 'no'):
                        print(fs_forests[i],":")
                        print(" ","size:",forests_dict[fs_forests[i]]["size"]," acre")
                        print(" ","fishing:",forests_dict[fs_forests[i]]["fishing"] > 0)
                        print(" ","camping:",forests_dict[fs_forests[i]]["camping"] > 0)
                        if(len(forests_dict[fs_forests[i]]["state"]) == 1):
                            print(" ","state:",forests_dict[fs_forests[i]]["state"][0])
                        elif(len(forests_dict[fs_forests[i]]["state"]) == 2):
                            print(" ","state:",forests_dict[fs_forests[i]]["state"][0], " ", forests_dict[fs_forests[i]]["state"][1])
                        else:
                            print(" ","state:",forests_dict[fs_forests[i]]["state"][0], " ", forests_dict[fs_forests[i]]["state"][1]," ", forests_dict[fs_forests[i]]["state"][2])



                    if(c == 'yes' and f == 'no'):
                        print(cs_forests[i],":")
                        print(" ","size:",forests_dict[cs_forests[i]]["size"]," acre")
                        print(" ","fishing:",forests_dict[cs_forests[i]]["fishing"] > 0)
                        print(" ","camping:",forests_dict[cs_forests[i]]["camping"] > 0)
                        if(len(forests_dict[cs_forests[i]]["state"]) == 1):
                            print(" ","state:",forests_dict[cs_forests[i]]["state"][0])
                        elif(len(forests_dict[cs_forests[i]]["state"]) == 2):
                            print(" ","state:",forests_dict[cs_forests[i]]["state"][0], " ", forests_dict[cs_forests[i]]["state"][1])
                        else:
                            print(" ","state:",forests_dict[cs_forests[i]]["state"][0], " ", forests_dict[cs_forests[i]]["state"][1]," ", forests_dict[cs_forests[i]]["state"][2])



                    if(c == 'yes' and f == 'yes'):
                        print(fcs_forests[i],":")
                        print(" ","size:",forests_dict[fcs_forests[i]]["size"]," acre")
                        print(" ","fishing:",forests_dict[fcs_forests[i]]["fishing"] > 0)
                        print(" ","camping:",forests_dict[fcs_forests[i]]["camping"] > 0)
                        if(len(forests_dict[fcs_forests[i]]["state"]) == 1):
                            print(" ","state:",forests_dict[fcs_forests[i]]["state"][0])
                        elif(len(forests_dict[fcs_forests[i]]["state"]) == 2):
                            print(" ","state:",forests_dict[fcs_forests[i]]["state"][0], " ", forests_dict[fcs_forests[i]]["state"][1])
                        else:
                            print(" ","state:",forests_dict[fcs_forests[i]]["state"][0], " ", forests_dict[fcs_forests[i]]["state"][1]," ", forests_dict[fcs_forests[i]]["state"][2])


            else:
            #Plotly
                    if(f == 'no' and c == 'no'):
                        size_list = []
                        fishing_list = []
                        camping_list = []
                        state_list = []
                        for i in range(l):
                            size_list.append(forests_dict[s_forests[i]]["size"])
                            fishing_list.append(forests_dict[s_forests[i]]["fishing"] > 0)
                            camping_list.append(forests_dict[s_forests[i]]["camping"] > 0)
                            state_list.append(forests_dict[s_forests[i]]["state"])
                        fig = go.Figure(data=[go.Table(header=dict(values=['Forest Name', 'Size in acre', 'fishing', 'camping', 'state']),
                        cells=dict(values=[s_forests, size_list,fishing_list,camping_list,state_list]))
                            ])
                        fig.show()

                    if(f == 'yes' and c == 'no'):
                        size_list = []
                        fishing_list = []
                        camping_list = []
                        state_list = []
                        for i in range(l):
                            size_list.append(forests_dict[fs_forests[i]]["size"])
                            fishing_list.append(forests_dict[fs_forests[i]]["fishing"] > 0)
                            camping_list.append(forests_dict[fs_forests[i]]["camping"] > 0)
                            state_list.append(forests_dict[fs_forests[i]]["state"])
                        fig = go.Figure(data=[go.Table(header=dict(values=['Forest Name', 'Size in acre', 'fishing', 'camping', 'state']),
                        cells=dict(values=[fs_forests, size_list,fishing_list,camping_list,state_list]))
                            ])
                        fig.show()


                    if(c == 'yes' and f == 'no'):
                        size_list = []
                        fishing_list = []
                        camping_list = []
                        state_list = []
                        for i in range(l):
                            size_list.append(forests_dict[cs_forests[i]]["size"])
                            fishing_list.append(forests_dict[cs_forests[i]]["fishing"] > 0)
                            camping_list.append(forests_dict[cs_forests[i]]["camping"] > 0)
                            state_list.append(forests_dict[cs_forests[i]]["state"])
                        fig = go.Figure(data=[go.Table(header=dict(values=['Forest Name', 'Size in acre', 'fishing', 'camping', 'state']),
                        cells=dict(values=[cs_forests, size_list,fishing_list,camping_list,state_list]))
                            ])
                        fig.show()


                    if(c == 'yes' and f == 'yes'):
                        size_list = []
                        fishing_list = []
                        camping_list = []
                        state_list = []
                        for i in range(l):
                            size_list.append(forests_dict[fcs_forests[i]]["size"])
                            fishing_list.append(forests_dict[fcs_forests[i]]["fishing"] > 0)
                            camping_list.append(forests_dict[fcs_forests[i]]["camping"] > 0)
                            state_list.append(forests_dict[fcs_forests[i]]["state"])
                        fig = go.Figure(data=[go.Table(header=dict(values=['Forest Name', 'Size in acre', 'fishing', 'camping', 'state']),
                        cells=dict(values=[fcs_forests, size_list,fishing_list,camping_list,state_list]))
                            ])
                        fig.show()
            


    interact()
