
function ledTurnOn(data) {
    fetch('http://localhost:8000/led_control/on', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json());
}

function ledTurnOff(data) {
    fetch('http://localhost:8000/led_control/off', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json());
}


function update_strip_status(brightness, color) {
    fetch('http://localhost:8000/led_control/strip_status', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({brightness: brightness, color: color}),
    })
    .then(response => response.json())
    .catch((error) => console.error('Error:', error));
}



document.getElementById("led_on").addEventListener("click", function() {
    ledTurnOn({data: "Turn on LED"});
});

document.getElementById("led_off").addEventListener("click", function() {
    ledTurnOff({data: "Turn off LED"});
});


var rangeSlider = document.getElementById("rs-range-line");
var rangeBullet = document.getElementById("rs-bullet");
var colorPicker = document.getElementById("colorPicker")

function manageColor() {
    update_strip_status(rangeSlider.value, colorPicker.value);
}

colorPicker.addEventListener("change", manageColor);


function manageSliderValue() {
    update_strip_status(rangeSlider.value, colorPicker.value);
    rangeBullet.innerHTML = rangeSlider.value;
    var bulletPosition = (rangeSlider.value /rangeSlider.max);
    rangeBullet.style.left = (bulletPosition * 578) + "px";
  }

rangeSlider.addEventListener("input", manageSliderValue, false);
