boxes = 1250
truck_capacity = 12

full_trucks = boxes // truck_capacity

print("Full trucks: ", full_trucks)

remaining_boxes = boxes % truck_capacity

print("Remaining boxes: ", remaining_boxes)