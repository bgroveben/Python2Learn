export function randInt(low, high, weighted=false) {
  let rndDec = Math.random();
  if (!weighted) {
    return Math.floor(rndDec * (high - low + 1) + low);
  }
  let numList = [];
  for (let i=low; i<=high; i++) {
    numList.push(i);
    for (var j=0; j<=i; j++) {
      numList.push(i);
    }
  }
  let rndInt = numList[Math.floor(Math.random() * numList.length)];
  return rndInt;
}

  