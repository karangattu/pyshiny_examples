
// Sample JavaScript function
function showAlert() {
    alert('Hello from included JavaScript!');
}

function changeBackgroundColor() {
    document.body.style.backgroundColor = 
        '#' + Math.floor(Math.random()*16777215).toString(16);
}

console.log('JavaScript file loaded successfully!');
