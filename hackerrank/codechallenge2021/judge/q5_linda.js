
class Data {
  constructor(isortval, iscore, iptype) {
    this.sortval = isortval;
    this.score = iscore;
    this.ptype = iptype; //0, 1, 2
  }
}

function max_ptype_0_or_2(arrdata) {
  return arrdata
    .filter(d => d.ptype != 1)
    .reduce((a, d) => Math.max(a, d.score), -1);
}

function min_ptype_0_or_1(arrdata) {
  return arrdata
    .filter(d => d.ptype != 2)
    .reduce((a, d) => Math.min(a, d.score), 20000000);
}

function sum_score(arrdata, startix, endix) {
  let total = 0;
  for (let i = startix; i < endix; i++) {
    total += arrdata[i].score;
  }
  return total;
}

function processData(input) {
  let lines = input.split("\n").filter(i => i !== '');
  const nums = lines[0].split(' ');
  const n = parseInt(nums[0]);
  const m = parseInt(nums[1]);

  lines.shift(); //remove first line
  lines.sort();
  let data = [];
  let partner_score;
  lines.forEach((line, i) => { 
    const words = line.split(' ');
    const lastchar = words[0].slice(-1);
    const score = parseInt(words[1]);
    if (lastchar === '0') {
      partner_score = score;
    } else if (lastchar === '1') {
      if (partner_score <= score) {
	data.push(new Data(partner_score*2.0, partner_score, 0));
	data.push(new Data(score*2.0, score, 0));
      } else {
	const sortval = score + partner_score + (score*1e-7) + (i*1e-8);
	data.push(new Data(sortval, partner_score, 1));
	data.push(new Data(sortval+2e-9, score, 2));
      }
    } else {
      data.push(new Data(score*2.0, score, 0));
    }
  })

  let answer;
  if (m === 1) {
    answer = min_ptype_0_or_1(data);
  } else if (m === n) {
    answer = sum_score(data, 0, n);
  } else {
    data.sort((a, b) => a.sortval - b.sortval);
    answer = sum_score(data, 0, m);
    if (data[m-1].ptype === 1) {
      const answer1 = answer - data[m-1].score + min_ptype_0_or_1(data.slice(m-1, n));
      const answer2 = answer + data[m].score - max_ptype_0_or_2(data.slice(0, m-1));
      answer = Math.min(answer1, answer2);
    }
  }
  console.log(answer);
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
