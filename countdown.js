function pad(n) {
    return (n < 10) ? ("0" + n) : n;
}

const getCountdown = function(elemId, countDownDate) {
    return function() {
        var now = new Date().getTime();

        var distance = countDownDate - now;

        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        document.getElementById(elemId).innerHTML =
            pad(days) + "D " +
            pad(hours) + "H " +
            pad(minutes) + "M " +
            pad(seconds) + "S";

        if (distance < 0) {
            clearInterval(x);
            document.getElementById(elemId).innerHTML = "EXPIRED";
        }
    };
};

const countDownDate = new Date("Dec 9, 2017 00:00:00").getTime();

const countdownFunc = getCountdown("countdown_p", countDownDate);


const x = setInterval(countdownFunc, 1000);

window.onreadystatechange = function() {
    countdownFunc();
};
