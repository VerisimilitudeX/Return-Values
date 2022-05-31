def pm(t1, t2):
    print(t1 + " => " + t2)

  def hanoi(n, s, m, e):
    if n == 1:
        pm(s, e)
        return
      
    hanoi(n - 1, s, e, m)
    hanoi(1, s, m, e)
    hanoi(n - 1, m, s, e)

print("Welcome to towers of hanoi puzzle solver!")
n = int(input("How many disks start on tower A? "))
hanoi(n, "a", "b", "c")
