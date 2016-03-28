import index
import view

view.output_start()
x = int(input())

if x == 1:
    view.output_var("consumption")
    consumption = int(input())
    view.output_var("distance")
    distance = int(input())
    view.output(index.volume_calc(consumption, distance), "Volume")
elif x == 2:
    view.output_var("consumption")
    consumption = int(input())
    view.output_var("volume")
    volume = int(input())
    view.output(index.distance_calc(consumption, volume), "Distance")
else:
    print("Error number")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
