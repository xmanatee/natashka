const countDownDate = new Date("Dec 9, 2017 00:00:00").getTime();
// const countDownDate = new Date("Dec 3, 2017 00:00:00").getTime();

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
            document.getElementById(elemId).innerText = "EXPIRED";
        }
    };
};


window.onload = function() {
    var now = new Date().getTime();
    var distance = countDownDate - now;

    if (distance > 0) {
        console.log("biggaba");
        document.getElementById("qrframe").style.visibility = "hidden";
        document.getElementById("header_p").innerText = "The Game starts in...";
        const countdownFunc = getCountdown("countdown_p", countDownDate);
        countdownFunc();
        const x = setInterval(countdownFunc, 1000);
    } else {
        document.getElementById("header_p").innerText = "The Game is on";
        var qrcode_div = document.getElementById("qrcode");
        const link = "https://telegram.me/questmaster_bot";

        var qrcode = new QRCode(qrcode_div, {
            text: link,
            width: 200,
            height: 200,
            colorDark: "darkred",
            colorLight: "white",
            // colorDark: "#000000",
            // colorLight: "#ffffff",
            useSVG: true,
            correctLevel: QRCode.CorrectLevel.H
        });
    }
};

// window.onload = function() {
//     console.log("lalaka");
//     document.getElementById("title").style.visibility = "hidden"; //.setAttribute("visibility", "hidden");
//     setTimeout(function() {
//         console.log("lalakasa");
//         document.getElementById("title").style.visibility = "visible"; // .setAttribute("visibility", "visible");
//     }, 2000);
//
// };