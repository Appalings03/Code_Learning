let frames =360;
let a = 0;


function setup() {
  createCanvas(400,400);
  angleMode(DEGREES);
}


function draw() {
  background(220);
}

function keyPressed(){
  if(key === 's'){
    saveGif('mySketch',frames,{units: "frames"});
  }
}
