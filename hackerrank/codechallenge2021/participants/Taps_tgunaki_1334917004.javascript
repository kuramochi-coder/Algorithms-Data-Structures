function processData(input) {
    const numbers = input.split('\n').map(n => Number(n));
    const numOfTaps = numbers[0];
    var totalPortion = 0;
    for (var i = 1; i < numOfTaps + 1; i += 1) {
        const portionPerMinute = 1 / numbers[i];
        totalPortion += portionPerMinute;
    }
    const timeFillMinutes = 1 / totalPortion;
    console.log(Math.round(timeFillMinutes * 60));
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

