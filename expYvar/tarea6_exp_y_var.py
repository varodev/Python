def main():
    grados_celsius = 0
    grados_fahrenheit = 0

    grados_celsius = int(input("Intro grados celsius: "))
    grados_fahrenheit = (grados_celsius * 1.8) + 32

    print(f"{grados_celsius} grados celsius son {grados_fahrenheit} grados fahrenheit")

if __name__ == "__main__":
    main()