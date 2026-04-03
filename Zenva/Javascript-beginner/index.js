//using the script in html 
//also work in the index.js if put in a html file
//alert('Hello World')
//variable declaration
let age;
//variable assignment
age = 50;
console.log(age)
let name = 'Pilot'
console.log(name)
let hasExperience = true;
console.log(hasExperience)
// number
let examResult = 50.5;
console.log(examResult);

// change the value of a variable by reassigning
examResult = 100;
console.log(examResult);

// not recommended
examResult = 'Some Text';
console.log(examResult);

// undefined variable
let something;
console.log(something);

//addition
let a = 1 + 1;
console.log(a);

let b = 10;
let c = a + b;
console.log(c);

b += 1;
console.log(b)

//soustraction
let x = 10 - 5;
console.log(x);

let y =  b + x;
console.log(y);

x -= 1;
console.log(x)

//multiplication

let unitPrice = 2;
let units = 10;
let total = unitPrice * units;
console.log(total)

//division
let n = 10;
let result = n / 2;

// modulus
let r = 5 % 2;
console.log(r);

// Challenge
let baseWeight = 10000;
let foodweight = 100;
let passengersWeight = 10;

let fuelUnitWeight = 2; // weight of 1 unit of fuel
let fuelUnits = 100; // total units of fuel we need

let fuelWeight = fuelUnitWeight * fuelUnits

let totalWeight = baseWeight + foodweight + passengersWeight + fuelWeight

console.log(totalWeight)

// condition
let direction = 'diagonal';

if(direction == 'left'){
    console.log('red planet');
}else if(direction == 'right'){
    console.log('purple planet');
}else if(direction == 'backwards'){
    console.log('back home');
}else{
    console.log('ship crash')
}

//comparaison operators

let item = 'window';

// checking inequality
if(item != 'engine') {
  console.log('not engine!');
}

let score = 5;

if(score >= 60) {
  console.log('pass');
}
else if(score < 10) {
  console.log('meet the teacher');
}
else {
    console.log('not pass');
}

// store comparison result in a variable
let isEngine = item == 'engine';
console.log(isEngine);

if(isEngine) {
  console.log('item is engine');
}

// Challenge
let balance = 100;
let itemPrice = 10;

// 1. check balance
// 2. if they buy, update balance


// solution
if(balance >= itemPrice) {
  // update balance
  //balance = balance - itemPrice;
  balance -= itemPrice;
  console.log('item purchased');
  console.log(balance);
}
else {
  console.log('not enough balance');
}

// challenge comparaison
let distance = 150;
let fuel = 100
let distanceCondition = distance <=200 && distance >= 100;
let isEngineFunctionning = true;
if (!isEngineFunctionning || distance > 200){
    console.log("won't make it"); 
}

else if (distanceCondition && fuel >= 100){
    console.log("All Good");
}

else if (distance < 100 && fuel >= 25){
    console.log("All Good");
}

// function
function  houtToMinutes(hours){
  let result =hours*60;
  console.log(result);
  return result;
}

let a1 = houtToMinutes(10);
let b1 = houtToMinutes(20);

let dayToHour = function (days) {
  return days*24;
};

let c1 = dayToHour(1);
console.log(c);

//let balance = 100;
let stock = 50;
let price = 5;
//let quantity = 100;
function sellitem(quantity){
    if(quantity <= stock){
        stock -= quantity;
        balance += price*quantity;
        console.log("Purchased Complete",balance, stock);
    }
    else{
        console.log("Not enough stock", stock);
    }
}
sellitem(10)
sellitem(10)
sellitem(10)
sellitem(10)
sellitem(10)
sellitem(10)
sellitem(10)
sellitem(10)
sellitem(10)
sellitem(10)

//java object properties

let player = {
  age: 22,
  name: 'Martin',
  isActive: true,
  outfit:{
      color: 'blue',
      size: 'M',
      cost: '100',
      isNew: true
      }
  };

console.log(player);
console.log(player.outfit.color);
player.outfit.size = 'L';
console.log(player.outfit.size);

/*console.log(player.name)
console.log(player['name']);

player.isActive = false;
console.log(player);

player.health = 100;
console.log(player);

delete player.health;
console.log(player.health);
*/

// Methode implementation

let player1 = {
  health: 100,
  fun: 0,
  /*
  eatApple: function (){
      console.log("Eat Apple");
      this.health += 10;
      console.log("Healh =",this.health);
  },
  eatCandy: function (){
      console.log("Eat Candy");
      this.health -= 5;
      this.fun += 5;
      console.log("Health =", this.health, "\nFun =", this.fun);
  },
  */
  play: function(){
      console.log("Play");
      this.fun += 10;
      console.log("Fun =", this.fun);
  },
  eat: function(food){
      if(food == 'apple'){
          this.health += 10;
          console.log("Healh =",this.health);
      }
      else if(food == 'candy'){
          this.health -= 5;
          this.fun += 5;
          console.log("Health =", this.health, "\nFun =", this.fun);
      }else{
          console.log("You can't eat that food");
      }
  }
};
//player.eatApple();
//player.eatCandy();
player1.play();
player1.eat('apple');
player1.eat('candy');
console.log(player1)

// while loop

function sendSignal(){
  console.log("HELP!");
};

let i = 0;

while(i<1000){
  sendSignal();
  i++;
};

let result1 = 0;

let j = 0;

while(j <= 10){
  result1 = result1 + j;
  j++;
};
console.log(result1);

//break and continue

let fuel1 = 1000;
let distance1 = 0;

while (fuel1 > 0){
    distance1++;

    if (distance1 >= 100 && distance1 < 200){
        continue;
    };
    fuel1 --;
    if (distance1 == 500){
        break;
    };
};

console.log(distance1);
console.log(fuel1);

//loop

let population = 100;

//population = population * 1.05;
//population *= 1.05;

let i1 = 0;
while (i1 < 10) {
    population *= 1.05
    i1++;
}

console.log(population);
i1 = 0;
population = 100;

for (let i = 0; i < 10; i++) {
    population *= 1.05;
}
console.log(population);

// DataBase

let database =['turtle', 'cat','dog', 'bird'];
console.log(database);
console.log(database.length);

let animal = database[0];
console.log(animal);
database[0] = 'dinosaur';
console.log(database);

let last = database[database.length - 1];
console.log(last);

database.push('lizard');
console.log(database);

database.pop();
console.log(database);

// Iteration on Array

let scores = [10, 20, 10];

let i2 = 0;
while (i2 < scores.length) {
    scores[i2]++;
    i2++;
}
console.log(scores);

for(let i = 0; i < scores.length; i++) {
    scores[i]++;
}
console.log(scores);

scores.forEach(function(entry, index){
console.log(entry,index);
//entry++; -> augmente une copie de la valeur
scores[index]++;    
});
console.log(scores);

let catalog = [
    {
        title: 'Js forBeginners',
        author: 'Zenva', 
        copies:1
    },
    {
        title: 'HTML forBeginners',
        author: 'XYZ', 
        copies: 1
    }
];

catalog.forEach(function(entry){
    if (entry.author == 'Zenva'){
        entry.copies++;
    }
});

console.log(catalog);

// Multidimensionnal Array

//2D Array
let a2 =[[1, 2, 3],[4, 5, 6, 7]];
console.log(a2);
console.log(a2[0][1]);
a2[1][2] = 100;
console.log(a2[1][2]);

let terrains = [
    ['desert', 'desert', 'grass', 'grass'],
    ['desert', 'grass', 'water', 'grass'],
    ['grass', 'grass', 'water', 'water'],
    ['grass', 'grass', 'grass', 'grass']
];