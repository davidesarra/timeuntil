function getCountdown(timestamp) {
    var start = new Date().getTime();
    var end = new Date(timestamp);
    var delta = end - start;
    var days = Math.floor(delta / (1000 * 60 * 60 * 24));
    var hours = Math.floor((delta % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((delta % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((delta % (1000 * 60)) / 1000);
    return days + "d " + hours + "h " + minutes + "m " + seconds + "s ";
}
