three_pts_apple = int(input("Enter the amount of three point shots for apple:"))
one_pts_apple = int(input("Enter the amount of one point shots for apple:"))
two_pts_apple = int(input("Enter the amount of two point shots for apple:"))

three_pts_bannana = int(input("Enter the amount of three point shots for bannana:"))
two_pts_bannana = int(input("Enter the amount of two point shots for bannana:"))
one_pts_bannana = int(input("Enter the amount of one point shots for bannana:"))

total_pts_apple = (three_pts_apple * 3) + (two_pts_apple * 2) + one_pts_apple
total_pts_bannana = (three_pts_bannana * 3) + (two_pts_bannana * 2) + one_pts_bannana

if total_pts_bannana > total_pts_apple:
    winner = "B"

elif total_pts_bannana < total_pts_apple:
    winner = "A"

elif total_pts_apple == total_pts_bannana:
    winner = "T"

print(winner)

