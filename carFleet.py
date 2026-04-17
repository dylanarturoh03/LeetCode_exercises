class Solution:
    def carFleet(
        self,
        target: int,
        position: list[int],
        speed: list[int]
    ) -> int:
        def step(car: tuple[int, int]) -> float:
            pos, spd = car
            return (target - pos) / spd if pos < target else 0

        cars: list[tuple[int, int]] = ([
            (position[i], speed[i]) for i in range(len(position))
        ])
        fleets: list[list[int]] = []

        cars.sort(key=lambda x: x[0])

        while cars:
            fleet: list[int] = []
            fleet.append(cars.pop())
            lead_steps: float = step(fleet[-1])
            while cars and step(cars[-1]) <= lead_steps:
                fleet.append(cars.pop())

            fleets.append(fleet)
        print(fleets)
        return len(fleets)

    def carFleet_monotonic(
        self, target: int,
        position: list[int],
        speed: list[int]
    ) -> int:
        def step(car: tuple[int, int]) -> float:
            pos, spd = car
            return (target - pos) / spd if pos < target else 0

        cars: list[tuple[int, int]] = ([
            (position[i], speed[i]) for i in range(len(position))
        ])
        n_fleet: int = 0

        cars.sort(key=lambda x: x[0])

        # Invariant:
        # lead_car is the current bottleneck for
        # the current fleet. If a car cannot catch up
        # to bottleneck, then it becomes the next fleet.
        while cars:
            n_fleet += 1
            lead_steps: float = step(cars.pop())
            while cars and step(cars[-1]) <= lead_steps:
                cars.pop()

        return n_fleet


sol = Solution()
print(sol.carFleet(15, [12, 10, 8, 5, 3], [2, 4, 1, 1, 3]))
