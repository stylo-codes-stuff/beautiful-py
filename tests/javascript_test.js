#!/usr/bin/env node
// line comment
/* 
multiline block comment
*/
function test(arg1,arg2){
    console.log(arg1+arg2)
}
test();

const declaration = 1;
var dec = "1";
let c = true;
class clod {
    #priv = "value"
}

lbl: console.log(c)

while (true){
    break
}
try{
    test(1,2);
}catch{
    console.log("error.catch")
}
switch(declaration){
    case 'var':
        console.log("var")
        break
    case '2':
        console.log(3)
    

}