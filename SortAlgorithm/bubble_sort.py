def main(input_list):
    # NotSorted = True
    while True:
        change_this_turn = False
        for i in range(len(input_list)-1):
            if input_list[i] > input_list[i+1]:
                plh = input_list[i+1]
                input_list[i+1] = input_list[i]
                input_list[i] = plh
                change_this_turn = True
            else:
                pass
        if not change_this_turn:
            return input_list

            
if __name__ == "__main__":
    input_list = input()
    input_list = [int(tmp) for tmp in input_list.split(' ')]
    # input thorugh space
    print(main(input_list))