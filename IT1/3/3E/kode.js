let todimensjonal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

let gangetabell = [[], [], [], [], [], [], [], [], [], [], []];

for (let i = 0; i <= 10; i++) {
    for (let j = 0; j <= 10; j++) {
        gangetabell[i][j] = i * j;
    }
}