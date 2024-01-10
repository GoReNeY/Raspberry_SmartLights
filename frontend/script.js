document.getElementById("button1").addEventListener("click", function() {
    LED_Turn_On({data: "Turn on LED"});
});

document.getElementById("button2").addEventListener("click", function() {
    LED_Turn_Off({data: "Turn off LED"});
});

function LED_Turn_On(data) {
    fetch('http://localhost:8000/led_control/on', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json());
}

function LED_Turn_Off(data) {
    fetch('http://localhost:8000/led_control/off', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json());
}