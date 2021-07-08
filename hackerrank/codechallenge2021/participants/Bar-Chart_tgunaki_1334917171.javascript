function processData(input) {
    const lines = input.split("\n").map(line => line.split(",").map(n => Number(n)));
    lines.splice(-1, 1);
    const inputWidth = lines[0].length;
    
    const columns = [];
    let overallMaxValue = lines[0][0];
    for (let i = 0; i < inputWidth; i += 1) {
        let maxValue = lines[0][i];
        for (let x = 1; x < lines.length; x += 1) {
            if (maxValue < lines[x][i]) {
                maxValue = lines[x][i];
            }
        }
        if (maxValue > overallMaxValue) {
            overallMaxValue = maxValue;
        }
        columns.push(maxValue);
    }
    
    for (let currentRow = overallMaxValue; currentRow > 0; currentRow -= 1) {
        for (let currentCol = 0; currentCol < inputWidth; currentCol += 1) {
            if (columns[currentCol] >= currentRow) {
                process.stdout.write('+');
            } else {
                process.stdout.write(' ');
            }
        }
        process.stdout.write('\n');
    }
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});

