
// Custom JavaScript function to modify an element
function changeTextColor() {
    var element = document.getElementById('dynamic_text');
    element.style.color = getRandomColor();
}

// Function to generate a random color
function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
