def tower_of_honai(n , sou , aux , des):
    if n == 1:
        print(f"Disk 1 is moved from source {sou} to destination {des}")
        return
    tower_of_honai(n-1 , sou , des , aux)
    print(f"Disk {n} is moved from source {sou} to destination {des}")
    tower_of_honai(n-1 , aux , des , sou)



n = int(input("Enter the number of disks : "))
tower_of_honai(n , "A" , "B" , "C")