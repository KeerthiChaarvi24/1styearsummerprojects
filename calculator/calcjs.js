// Calculator Program
const display = document.getElementById("display");
function appendToDisplay(input) {
    display.value += input;
}
function clearDisplay(){
    display.value="";
}
function calculate() {
    try {
        display.value = q(display.value);
    }
    catch(error) {
        display.value = "Error";
    }
}