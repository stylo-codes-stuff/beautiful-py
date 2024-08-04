#! this is a hasbang!
// this is a line comment
/*
this is a multiline block comment
*/
//defining variables

var $1 = "hello";
var test = "test";
var sq = 'test';
const test2 = 1 ;
let test_3 = true ;
var $4test4 = test;
var _test = 1.4;
var signed_int = +2;
var signed_int2 = -2;
var signed_int3 = +2.3;
//defining a function with arguments
function test(arg1,arg2){
    //function using those arguments
    console.log(arg1+arg2);
}
test(1,2)
class test_Class{
constuctor(){
    this.property = null;
}
#privatemethod(){
    console.log("this comes from a private method")
}
}
const class_object = new test_Class();
class_object.privatemethod