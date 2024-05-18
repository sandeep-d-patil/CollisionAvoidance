# Collision Avoidance
## Problem Statement:
During the operation of picking up boxes from the pallet using a robot, decide the order of picking of boxes based on collision avoidance.

## Given:
1. Position of Robot (X, Y, Z) = (0,0,0)
2. Height of tallest item = 400mm
3. All objects are right parallelogram prism
4. Object (box) properties:		
 - Center of the object = [object.center.x, object.center.y, object.center.z]
 - X dimension = [object.x]
 - Y dimension = [object.y]
 - Maximum Z dimension: [object.z] ≤ 400mm
5. There is no restriction of number of boxes stacked.
6. Maximum height to which the robot can pick the object = 400mm from the object’s initial position.
7. The dimensions of the flat pallet (width, breadth, height) = (1000mm, 1000mm, 0mm)
8. Items can slide on top of each other.
9. Robot will go on top of the box at a height = 100mm from surface.

## Assumptions:

 1. Object centers [object.center.x, object.center.y, object.center.z] in mm are centers in the global coordinates (with (0,0,0) at the robot’s center).
 2. Vacuum gripper is used to pick up the boxes.
 3. There is no collision/interference between robot and other boxes during the gripping action.
 4. Boxes are assumed to be parallel to the coordinate axis.

## Methodology:
A simple solution could be given as first object in the sorted list of object.center.z of the objects. But there are two main edge case during which picking box with highest object.center.z will cause collision between the robot and the box.

 1. Consider three boxes as shown in the Figure below, the tallest object (right) and the next object (left) have at the same centers. But the length between the two objects’ top surfaces is 110mm which is greater than the height at which the robot traverses. This causes a collision between the robot and the topmost box.

![case_1](/diagrams/case_1.png)

 2. Consider three boxes as shown in the figure below, the tallest object’s (right) center is lower than the next object (left) by 10mm. Here picking the object which higher object.center.z causes collision with the tallest object during the robot’s movement in the picking motion.
Hence, an optimal solution should be able to predict objects which are at the topmost position and pick the box with highest height.

![case_2](/diagrams/case_2.png)

## General steps of solution:

 1. Get objects from computeObjects()
 2. Obtain a list of objects which are stacked on top each other.
 3. For the stack of objects, calculate the height of the box with respect to surface.
 4. For the objects which are at the topmost in their center -> (x,y) and obtain their heights.
 5. From the above objects find the object with highest height.
