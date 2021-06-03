const getOnes = () => {
  return {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
  }
}

const getTens = () => {
  return {
    1: "ten",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninty",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "forteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "ninteen",
  }
}

const twoDigitsConverter = (nums) => {
  const ones = getOnes();
  const tens = getTens();
  
  if (nums[0] >= 2) {
    if (Number(nums[1]) === 0) return `${tens[nums[0]]}`;
    return `${tens[nums[0]]} ${ones[nums[1]]}`;
  } else {
    return tens[nums];
  }
}

const threeDigitsConverter = (nums) => {
  const ones = getOnes();
  const twoDigits = nums.slice(1);
  const twoDigitsConv = twoDigitsConverter(twoDigits);
  
  if (Number(nums[0]) === 0) return `and ${twoDigitsConv}`
  else return `${ones[nums[0]]} hundreds and ${twoDigitsConv}`;
}

const firstStrToUpperCase = (strs) => {
  const array = strs.split("");
  array[0] = array[0].toUpperCase();
  return array.join("");
}

const converter = (strs) => {
  const nums = strs.split("");
  let n = nums.length;
  const ones = getOnes();

  // check for invalid inputs
  const pattern = /^\d+$/;
  nums.forEach((num) => {
    const test = pattern.test(num);
    if (!test) n = "invalid";
  })

  let result = "";
  switch (n) {
    case 1:
      result = `${ones[strs]} only`;
      break;

    case 2:
      result = `${twoDigitsConverter(nums)} only`;
      break;

    case 3:
      result = `${threeDigitsConverter(nums)} only`;
      break;
    
    case 4:
      const threeDigits = nums.slice(1);
      const threeDigitsConv = threeDigitsConverter(threeDigits);
      result = `${ones[nums[0]]} thousands ${threeDigitsConv} only`;
      break;

    case 5: 
      const twoDigits = nums.slice(0,2);
      const twoDigitsConv = twoDigitsConverter(twoDigits);
      const threeDigits2 = nums.slice(2);
      const threeDigitsConv2 = threeDigitsConverter(threeDigits2);
      result = `${twoDigitsConv} thousands ${threeDigitsConv2} only`;
      break;
    
    case "invalid": 
      result = "invalid inputs";
      break;

    default:
      result = "error";
      break;
  }

  return firstStrToUpperCase(result);
}

// normal
console.log("9", converter("9"));
console.log("23", converter("23"));
console.log("979", converter("979"));
console.log("5979", converter("5979"));
console.log("75930", converter("75930"));

// zero case
console.log("0", converter("0"));
console.log("90", converter("90"));
console.log("5079", converter("5079"));
console.log("70933", converter("70933"));

// error
console.log("empty", converter(""));
console.log("7593022", converter("7593022"));

// invalid inputs
console.log("759e2", converter("759e2"));
console.log("asde", converter("asde"));
