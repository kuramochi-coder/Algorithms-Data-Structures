use std::io;
use std::str;
use std::cmp;
use std::cmp::Ordering::Equal;

struct Data {
  sortval: f64,
  score: i32,
  ptype: i32,
}
impl Data {
  pub fn new(isortval: f64, iscore: i32, iptype: i32) -> Data {
    Data { sortval: isortval, score: iscore, ptype: iptype } 
  }
}

fn max_ptype_0_or_2(arrdata: &Vec<Data>, startix: usize, endix: usize) -> i64 {
  let mut ans: i32 = -1;
  for i in startix..endix {
    if arrdata[i].ptype != 1 {
      ans = cmp::max(ans, arrdata[i].score);  
    }
  }
  return ans as i64;
}

fn min_ptype_0_or_1(arrdata: &Vec<Data>, startix: usize, endix: usize) -> i64 {
  let mut ans: i32 = 20000000;
  for i in startix..endix {
    if arrdata[i].ptype != 2 {
      ans = cmp::min(ans, arrdata[i].score);  
    }
  }
  return ans as i64;
}

fn sum_score(arrdata: &Vec<Data>, startix: usize, endix: usize) -> i64 {
  let mut total: i64 = 0;
  for i in startix..endix {
    total += arrdata[i].score as i64;
  }
  return total;
}

fn readline() -> String {
    let mut input_buffer = String::new();
    io::stdin().read_line(&mut input_buffer).expect("readline err");
    return input_buffer; //.trim().to_string();
}
fn readints() -> Vec<i32> {
    let line = readline();
    return line.split_whitespace().map(|s| s.parse().unwrap()).collect::<Vec<i32>>();
}

fn main() {
  let nums: Vec<i32> = readints();
  let n = nums[0] as usize;
  let m = nums[1] as usize;
  let mut lines: Vec<String> = vec!["".to_string(); n];
  for i in 0..n { 
    io::stdin().read_line(&mut lines[i]).expect("!");
  }
  lines.sort();
  let mut data: Vec<Data> = Vec::new();
  let mut partner_score: i32 = 0;
  for i in 0..n { 
    let words: Vec<&str> = lines[i].split_whitespace().collect();
    let lastchar = words[0].chars().last().unwrap();
    let score = words[1].parse::<i32>().unwrap();
    if lastchar == '0' {
      partner_score = score;
    } else if lastchar == '1' {
      if partner_score <= score {
    	data.push(Data::new(partner_score as f64 *2.0, partner_score, 0));
	    data.push(Data::new(score as f64 *2.0, score, 0));
      } else {
     	let sortval = (score + partner_score) as f64 +
            (score as f64 *1e-7) + (i as f64 *1e-8);
    	data.push(Data::new(sortval, partner_score, 1));
    	data.push(Data::new(sortval+2e-9, score, 2));
      }
    } else {
      data.push(Data::new(score as f64 *2.0, score, 0));
    }
  }

  let mut answer: i64;
  if m == 1 {
    answer = min_ptype_0_or_1(&data, 0, n);
  } else if m == n {
    answer = sum_score(&data, 0, n);
  } else {
    data.sort_by(|l, r| l.sortval.partial_cmp(&r.sortval).unwrap_or(Equal));
    answer = sum_score(&data, 0, m);
    if data[m-1].ptype == 1 {
      let answer1 = answer - data[m-1].score as i64 + min_ptype_0_or_1(&data, m-1, n);
      let answer2 = answer + data[m].score as i64 - max_ptype_0_or_2(&data, 0, m-1);
      answer = cmp::min(answer1, answer2);
    }
  }
  println!("{}", answer);
}
