function getCountdown(timestamp) {
    var start = moment();
    var end = moment(timestamp);
    var delta = moment.duration(end.diff(start));
    var days = Math.floor(delta.asDays());
    delta.subtract(days, "days");
    var hours = Math.floor(delta.asHours());
    delta.subtract(hours, "hours");
    var minutes = Math.floor(delta.asMinutes());
    delta.subtract(minutes, "minutes");
    var seconds = Math.floor(delta.asSeconds());
    return `${days}d ${hours}h ${minutes}m ${seconds}s`;
}
