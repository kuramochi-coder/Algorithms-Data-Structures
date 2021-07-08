// start from https://gist.github.com/jpillora/7382441
function solve(graph, s) {
  var solutions = {};
  solutions[s] = [];
  solutions[s].dist = 0;
  
  while(true) {
    var parent = null;
    var nearest = null;
    var dist = Infinity;
    
    //for each existing solution
    for(var n in solutions) {
      if(!solutions[n])
        continue
      var ndist = solutions[n].dist;
      var adj = graph[n];
      //for each of its adjacent nodes...
      for(var a in adj) {
        //without a solution already...
        if(solutions[a])
          continue;
        //choose nearest node with lowest *total* cost
        var d = adj[a] + ndist;
        if(d < dist) {
          //reference parent
          parent = solutions[n];
          nearest = a;
          dist = d;
        }
      }
    }
    
    //no more solutions
    if(dist === Infinity) {
        break;
    }
    
    //extend parent's solution path
    solutions[nearest] = parent.concat(nearest);
    //extend parent's cost
    solutions[nearest].dist = dist;
  }
  
  return solutions;
}
// end from https://gist.github.com/jpillora/7382441

// start from https://stackoverflow.com/a/24392281/126039
function intersects(a,b,c,d,p,q,r,s) {
  var det, gamma, lambda;
  det = (c - a) * (s - q) - (r - p) * (d - b);
  if (det === 0) {
    return false;
  }
  lambda = ((s - q) * (r - a) + (p - r) * (s - b)) / det;
  gamma = ((b - d) * (r - a) + (c - a) * (s - b)) / det;
  return (0 < lambda && lambda < 1) && (0 < gamma && gamma < 1);
}
// end from https://stackoverflow.com/a/24392281/126039

function lineIntersectsPolygon(line, polygon) {
  for (let i = 0; i < polygon.length; i += 1) {
    for (let j = i + 1; j < polygon.length; j += 1) {
      if (intersects(...line, ...polygon[i], ...polygon[j])) {
        return true;
      }
    }
  }
  return false;
}

function distance_square(a, b, c, d) {
  return (a - c) * (a - c) + (b - d) * (b - d);
}

// idea from https://www.codingame.com/playgrounds/39380/finding-shortest-path-in-the-plane-with-obstacles
function query(queries, polygonPoints) {
  const queriesToPoints = queries
    .map(([startX, startY, endX, endY]) => [[startX, startY], [endX, endY]])
    .reduce((a, b) => {
      if (a.some((tx, ty) => tx === b[0] && ty === b[1])) {
        return a;
      }
      return [...a, ...b];
    }, []);

  const allNodes = [...queriesToPoints, ...polygonPoints];

  const graph = {};
  allNodes.forEach((node1, idx1) => {
    allNodes.forEach((node2, idx2) => {
      if (idx1 === idx2) {
        return;
      }
      const thisLine = [...node1, ...node2];
      if (lineIntersectsPolygon(thisLine, polygonPoints)) {
        return;
      }
      const key1 = `${node1[0]} ${node1[1]}`;
      const key2 = `${node2[0]} ${node2[1]}`;
      if (!graph[key1]) {
        graph[key1] = {};
      }
      graph[key1][key2] = Math.sqrt(distance_square(...thisLine));
    });
  });

  queries.forEach(([startX, startY, endX, endY]) => {
    const startKey = `${startX} ${startY}`
    const endKey = `${endX} ${endY}`;
    const solns = solve(graph, startKey);
    console.log((solns[endKey].dist).toFixed(2));
  })
}

function processData(input) {
  const lines = input.split('\n');
  const polygonNumLines = Number(lines[0]);

  const polygonPoints = [];
  for (let i = 1; i <= polygonNumLines; i += 1) {
    polygonPoints.push(lines[i].split(' ').map(n => Number(n)));
  }

  const numQueries = Number(lines[polygonNumLines + 1]);
  const queries = []
  for (let i = 0; i < numQueries; i += 1) {
    const queryLine = lines[polygonNumLines + i + 2].split(' ').map(n => Number(n));
    queries.push(queryLine);
  }
  query(queries, polygonPoints);
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

