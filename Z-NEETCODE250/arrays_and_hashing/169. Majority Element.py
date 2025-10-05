

##boyer more algo, same paile bare na paile kome

def megority_element(arr):
    sei_item = None
    sei_count = None

    for index,item in enumerate(arr):
        if sei_item is None and sei_count is None:
            sei_item = item
            sei_count = 1
        else:
            if item == sei_item:
                sei_count +=1
            else:
                sei_count -=1

            if sei_count == 0:
                sei_item = item
                sei_count = 1

    return sei_item



print(megority_element([8,8,7,7,7]))